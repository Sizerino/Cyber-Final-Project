import sys
import customtkinter
from PIL import Image
from libs import fuzzer


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.eval("tk::PlaceWindow . center")
        self.geometry("600x300")
        self.title("brainrot app")
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
        self.imagelabel.grid(sticky="n", padx=5, pady=5, row=0, column=0)

        self.button1 = customtkinter.CTkButton(
            master=self,
            text="brainrot"
        )
        self.button1.grid(padx=5, pady=5, row=1, column=0)

        self.button2 = customtkinter.CTkButton(
            master=self,
            text="more brainrot"
        )
        self.button2.grid(padx=5, pady=5, row=2, column=0)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure(0, weight=1)


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(
            master=self,
            text="W.I.P",
            command=lambda: fuzzer.fuzz()
        )
        self.button.grid(padx=5, pady=5, row=0, column=0)

        self.console = customtkinter.CTkTextbox(
            master=self
        )
        self.console.grid(sticky="nswe", padx=5, pady=5, row=1, column=0)

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        def consoleoutput(stdout):
            self.console.insert(customtkinter.INSERT, stdout)
            self.console.see(customtkinter.END)

        sys.stdout.write = consoleoutput


app = App()
app.mainloop()
