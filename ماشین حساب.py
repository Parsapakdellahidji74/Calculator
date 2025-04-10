import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        self.entry = tk.Entry(root, width=15, borderwidth=3, font=("Arial", 18), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "=", "C", "+"]
        ]

        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                if char == "=":
                    btn = tk.Button(self.root, text=char, width=4, height=1, font=("Arial", 14),
                                    bg="green", fg="white", command=self.calculate)
                elif char == "C":
                    btn = tk.Button(self.root, text=char, width=4, height=1, font=("Arial", 14),
                                    bg="red", fg="white", command=self.clear)
                else:
                    btn = tk.Button(self.root, text=char, width=4, height=1, font=("Arial", 14))
                    btn.bind("<Button-1>", self.click)

                btn.grid(row=i+1, column=j, padx=4, pady=4)

    def click(self, event):
        current = str(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(event.widget["text"]))

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.resizable(False, False)
    root.mainloop()