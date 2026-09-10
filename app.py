import tkinter as tk


class Calculator(tk.Tk):
    """A small, keyboard-friendly desktop calculator."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg="#1f2937")
        self.expression = ""
        self.display_text = tk.StringVar(value="0")
        self._build_ui()
        self._bind_keyboard()

    def _build_ui(self):
        container = tk.Frame(self, bg="#1f2937", padx=18, pady=18)
        container.grid()

        display = tk.Label(
            container,
            textvariable=self.display_text,
            anchor="e",
            bg="#111827",
            fg="#f9fafb",
            font=("Helvetica", 28, "bold"),
            padx=16,
            pady=20,
            width=16,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 14))

        keys = [
            ("C", self.clear, "#ef4444"), ("÷", lambda: self.append("/"), "#f59e0b"),
            ("×", lambda: self.append("*"), "#f59e0b"), ("−", lambda: self.append("-"), "#f59e0b"),
            ("7", lambda: self.append("7"), "#374151"), ("8", lambda: self.append("8"), "#374151"),
            ("9", lambda: self.append("9"), "#374151"), ("+", lambda: self.append("+"), "#f59e0b"),
            ("4", lambda: self.append("4"), "#374151"), ("5", lambda: self.append("5"), "#374151"),
            ("6", lambda: self.append("6"), "#374151"), ("=", self.calculate, "#10b981"),
            ("1", lambda: self.append("1"), "#374151"), ("2", lambda: self.append("2"), "#374151"),
            ("3", lambda: self.append("3"), "#374151"), ("0", lambda: self.append("0"), "#374151"),
        ]
        for position, (label, command, color) in enumerate(keys):
            row, column = divmod(position, 4)
            button = tk.Button(
                container,
                text=label,
                command=command,
                bg=color,
                fg="white",
                activebackground=color,
                activeforeground="white",
                relief="flat",
                bd=0,
                font=("Helvetica", 18, "bold"),
                width=5,
                height=2,
                cursor="hand2",
            )
            button.grid(row=row + 1, column=column, padx=4, pady=4)

    def _bind_keyboard(self):
        for character in "0123456789+-*/":
            self.bind(character, lambda event, char=character: self.append(char))
        self.bind("<Return>", lambda event: self.calculate())
        self.bind("<Escape>", lambda event: self.clear())
        self.bind("<BackSpace>", lambda event: self.backspace())

    def append(self, value):
        if self.display_text.get() == "Error":
            self.clear()
        self.expression += value
        self.display_text.set(self.expression.replace("*", "×").replace("/", "÷"))

    def clear(self):
        self.expression = ""
        self.display_text.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        shown = self.expression.replace("*", "×").replace("/", "÷")
        self.display_text.set(shown or "0")

    def calculate(self):
        try:
            if not self.expression or any(char not in "0123456789+-*/." for char in self.expression):
                raise ValueError
            result = eval(self.expression, {"__builtins__": {}}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.display_text.set(self.expression)
        except (ArithmeticError, SyntaxError, ValueError):
            self.expression = ""
            self.display_text.set("Error")


if __name__ == "__main__":
    Calculator().mainloop()
