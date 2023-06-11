import random
import customtkinter


class GeneratorGUI:
    def __init__(self):
        self.width, self.height = 400, 200
        self.root = customtkinter.CTk()

        self.setup_root()
        self.labels()

        self.root.mainloop()

    def setup_root(self):
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Password Generator")
        self.root.resizable(False, False)




    def labels(self):
        label1 = customtkinter.CTkLabel(self.root, text="Password Generator", font=("Century Gothic", 20))
        label1.place(x=90, y=10)

        entry1 = customtkinter.CTkEntry(self.root, width=200)
        entry1.place(x=90, y=60)


if __name__ == "__main__":
    GeneratorGUI()
