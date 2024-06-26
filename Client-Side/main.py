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
        self.geometry("950x550")
        self.title("Stack Buffer Overflow")
        customtkinter.set_appearance_mode("dark")

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

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label = customtkinter.CTkLabel(
            master=self,
            text=(
                "INFO: Waiting For User Action...\n"
                "Enter The Following Server Values: [IP | Port]\n"
                "After That, Start The First Stage."
            )
        )
        self.label.grid(padx=5, pady=5, row=0, column=0, columnspan=2)

        self.input1 = customtkinter.CTkEntry(
            master=self,
            justify="center"
        )
        self.input1.grid(sticky="we", padx=5, pady=5, row=1, column=0)

        self.input2 = customtkinter.CTkEntry(
            master=self,
            justify="center"
        )
        self.input2.grid(sticky="we", padx=5, pady=5, row=1, column=1)

        self.button = customtkinter.CTkButton(
            master=self,
            text="Start Stage 1",
            command=lambda: action(1, [self.input1.get(), self.input2.get()])
        )
        self.button.grid(padx=5, pady=5, row=2, column=0, columnspan=2)

        self.console = customtkinter.CTkTextbox(
            master=self
        )
        self.console.grid(sticky="nswe", padx=5, pady=5, row=3, column=0, columnspan=2)

        self.rowconfigure(3, weight=1)
        self.columnconfigure((0, 1), weight=1)

        def action(stage, args):
            global ip
            global port

            if stage == 1:
                ip = args[0]
                port = int(args[1])

                threadedfunction(
                    fuzzer.fuzz,
                    (
                        ip,
                        port
                    )
                )

                self.button.configure(state=customtkinter.DISABLED)

                self.label.configure(
                    text="STATUS: Fuzzing..."
                )

                self.button.configure(
                    state=customtkinter.DISABLED,
                    text="Running Stage..."
                )

                self.input1.grid_forget()
                self.input2.grid_forget()

            if stage == 2:
                threadedfunction(
                    buffer.buff,
                    (
                        ip,
                        port,
                        args[0]
                    )
                )

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
                        ip,
                        port,
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
                    text=(
                        "STATUS: Generating Reverse Shell Payload...\n"
                        "Estimated Time To Finish Generating: 5 - 30 Seconds"
                    )
                )

                self.input1.grid_forget()
                self.input2.grid_forget()

            if stage == 4:
                threading.Thread(target=payload.terminal).start()

        def threadedfunction(function, arguments):
            threading.Thread(target=function, args=arguments).start()

        def consoleoutput(stdout):
            self.console.insert(customtkinter.INSERT, stdout)
            self.console.see(customtkinter.END)

            if "Couldn't" in stdout:
                self.button.configure(
                    state=customtkinter.NORMAL,
                    text="Retry Previous Stage"
                )

                self.label.configure(
                    text="ERROR: Stage Could Not Proceed."
                )

                self.input1.grid(sticky="we", padx=5, pady=5, row=1, column=0)
                self.input2.grid(sticky="we", padx=5, pady=5, row=1, column=1)

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

                self.input1.grid(sticky="we", padx=5, pady=5, row=1, column=0)
                self.input1.delete(0, customtkinter.END)
                self.input2.grid(sticky="we", padx=5, pady=5, row=1, column=1)
                self.input2.delete(0, customtkinter.END)

            if "CCCC" in stdout:
                self.button.configure(
                    state=customtkinter.NORMAL,
                    text="Live Terminal",
                    command=lambda: action(4, [None])
                )

                self.label.configure(
                    text=(
                        "INFO: All Stages Complete!\n"
                        "Head Over To The Live Terminal To Have Access Into\n"
                        "The Server That Executed The Payload."
                    )
                )

        sys.stdout.write = consoleoutput


ip: str
port: int

app = App()
app.mainloop()
