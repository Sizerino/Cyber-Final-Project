import re
import sys
import threading
import customtkinter
from PIL import Image
from scripts import fuzzer, buffer, payload


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.eval("tk::PlaceWindow . center")
        self.geometry("900x450")
        self.title("Stack Buffer Overflow")
        # self.wm_iconbitmap("./assets/")

        self.sidebar = SidebarFrame(self)
        self.sidebar.configure(fg_color="grey")
        self.sidebar.grid(sticky="nsw", padx=5, pady=5, row=0, column=0)

        self.mainbar = MainFrame(self)
        self.mainbar.configure(fg_color="grey")
        self.mainbar.grid(sticky="nswe", padx=5, pady=5, row=0, column=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1), weight=1)


class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.image = customtkinter.CTkImage(
            Image.open("./assets/Cyber Final Project Logo White.png"),
            size=(150, 150)
        )
        self.imagelabel = customtkinter.CTkLabel(
            master=self,
            image=self.image,
            text=""
        )
        self.imagelabel.grid(padx=5, pady=5, row=0, column=0)

        self.button1 = customtkinter.CTkButton(
            master=self,
            text="Control Panel"
        )
        self.button1.grid(padx=5, pady=5, row=1, column=0)

        self.button2 = customtkinter.CTkButton(
            master=self,
            text="Live Terminal",
            # command=lambda: switch(text)
        )
        self.button2.grid(padx=5, pady=5, row=2, column=0)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure(0, weight=1)

        # def switch():


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(
            master=self,
            text="Start Stage 1",
            command=lambda: action(1, [None])
        )
        self.button.grid(padx=5, pady=5, row=0, column=0, columnspan=2)

        self.label = customtkinter.CTkLabel(
            master=self,
            text=(
                "STATUS: Waiting For User Action..."  # \n
                # "Enter The Following Values: [Server IP | Server Port]\n"
                # "After That, Start Stage 1."
            )
        )
        self.label.grid(padx=5, row=1, column=0, columnspan=2)

        self.input1 = customtkinter.CTkEntry(
            master=self
        )
        # self.input1.grid(sticky="we", padx=5, pady=5, row=2, column=0)

        self.input2 = customtkinter.CTkEntry(
            master=self
        )
        # self.input2.grid(sticky="we", padx=5, pady=5, row=2, column=1)

        self.console = customtkinter.CTkTextbox(
            master=self
        )
        self.console.grid(sticky="nswe", padx=5, pady=5, row=3, column=0, columnspan=2)

        self.rowconfigure(3, weight=1)
        self.columnconfigure((0, 1), weight=1)

        def action(stage, args):
            if stage == 1:
                threadedfunction(fuzzer.fuzz, ("192.168.31.128", 9999))
                self.button.configure(state=customtkinter.DISABLED)

                self.label.configure(
                    text="STATUS: Fuzzing..."
                )

            if stage == 2:
                threadedfunction(buffer.buff, ("192.168.31.128", 9999, args[0]))

                self.button.configure(
                    state=customtkinter.DISABLED,
                    text="Running Stage..."
                )

                self.label.configure(
                    text="STATUS: Sending Unique Buffer..."
                )

            if stage == 3:
                threadedfunction(
                    payload.exploit,
                    (
                        "192.168.31.128",
                        9999,
                        args[0],
                        args[1],
                        args[2]
                    )
                )

                self.button.configure(
                    state=customtkinter.DISABLED,
                    text="Running Stage..."
                )

                self.label.configure(
                    text="STATUS: Sending Special Payload Execution..."
                )

                self.input1.delete(0, customtkinter.END)
                self.input2.delete(0, customtkinter.END)

        def threadedfunction(function, arguments):
            threading.Thread(target=function, args=arguments).start()

        def consoleoutput(stdout):
            self.console.insert(customtkinter.INSERT, stdout)
            self.console.see(customtkinter.END)

            if "Couldn't" in stdout:
                self.button.configure(
                    state=customtkinter.NORMAL,
                    text="Stage Stopped, Retry?"
                )

                self.label.configure(
                    text="ERROR: Stage Cannot Proceed."
                )

            if "end of life" in stdout:
                fuzzsize = int(
                    re.findall(r'\d+', stdout)[0]
                )

                self.button.configure(
                    state=customtkinter.NORMAL,
                    text="Start Stage 2",
                    command=lambda: action(2, [fuzzsize])
                )

                self.label.configure(
                    text=(
                        "INFO: Fuzzing Complete!\n"
                        "Restart The Server And Continue To The Next Stage."
                    )
                )

            if "Aa0A" in stdout:
                fuzzsize = int(
                    re.findall(r'\d+', stdout)[0]
                )

                self.button.configure(
                    state=customtkinter.NORMAL,
                    text="Start Stage 3",
                    command=lambda: action(3, [fuzzsize, self.input1.get(), self.input2.get()])
                )

                self.label.configure(
                    text=(
                        "INFO: Unique Buffer Sent!\n"
                        "Enter The Following Values From The Debugger: [EIP | JMP ESP] \n"
                        "After That, Restart The Server And Continue To The Next Stage."
                    )
                )

                self.input1.grid(sticky="we", padx=5, pady=5, row=2, column=0)
                self.input2.grid(sticky="we", padx=5, pady=5, row=2, column=1)

        sys.stdout.write = consoleoutput


app = App()
app.mainloop()
