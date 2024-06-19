# import pwn
import sys
import customtkinter
from libs import fuzzer


def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    root = customtkinter.CTk()
    root.geometry("400x240")

    label = customtkinter.CTkLabel(
        master=root, text="label wow yay"
    )
    label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    root.mainloop()


if __name__ == "__main__":
    main()
