import tkinter as tk
from tkinter import messagebox
import time
import math

class TimerApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("计时器")
        self.geometry("300x200")

        self.timer_label = tk.Label(self, text="00:00:00", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self, text="开始", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self, text="停止", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.record_button = tk.Button(self, text="记录时间", command=self.record_time)
        self.record_button.pack(pady=10)

        self.is_running = False
        self.start_time = 0

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False

    def update_timer(self):
        if self.is_running:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            self.after(1000, self.update_timer)

    def record_time(self):
        if self.is_running:
            elapsed_time = int(time.time() - self.start_time)
            messagebox.showinfo("记录时间", f"记录的时间: {elapsed_time} 秒")

class CalculatorApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("计算器")

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '⌫',
            '1', '2', '3', '-', '√',
            '0', '.', '=', '+', '^'
        ]

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=4, width=14,
                              justify='right')
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.grid_propagate(False)  # Disable grid propagation

        for row_val in range(5):
            self.button_frame.grid_rowconfigure(row_val, weight=1)
            self.button_frame.grid_columnconfigure(row_val, weight=1)

        for row_val in range(5):
            for col_val in range(5):
                button_index = row_val * 5 + col_val
                if button_index < len(buttons):
                    tk.Button(self.button_frame, text=buttons[button_index], padx=20, pady=20,
                              font=("Arial", 16), bd=8, command=lambda b=buttons[button_index]: self.button_click(b)) \
                        .grid(row=row_val, column=col_val, sticky="nsew")

    def button_click(self, value):
        current = self.result_var.get()

        if value == "=":
            try:
                # Use ** for exponentiation
                result = eval(current.replace("^", "**"))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("错误")
        elif value == "√":
            try:
                result = math.sqrt(float(current))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("错误")
        elif value == "^":
            self.result_var.set(current + "^")
        elif value == "⌫":
            self.result_var.set(current[:-1])
        elif value == "C":
            self.result_var.set("0")
        else:
            if current == "0" and value != ".":
                current = ""
            current += value
            self.result_var.set(current)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("主界面")
        self.state('zoomed')  # 最大化窗口
        self.geometry("300x150")

        tool_button_width = self.winfo_screenwidth() // 4  # 大约屏幕宽度的25%
        self.tool_button = tk.Button(self, text="工具", command=self.open_tool, width=tool_button_width, font=("Arial", 16))
        self.tool_button.pack(side=tk.LEFT, padx=10)

        calculator_button_width = self.winfo_screenwidth() // 4  # 大约屏幕宽度的25%
        self.calculator_button = tk.Button(self, text="计算器", command=self.open_calculator, width=calculator_button_width, font=("Arial", 16))
        self.calculator_button.pack(side=tk.LEFT, padx=10)

        ai_button_width = self.winfo_screenwidth() // 4  # 大约屏幕宽度的25%
        self.ai_button = tk.Button(self, text="人工智能", command=self.open_ai, width=ai_button_width, font=("Arial", 16))
        self.ai_button.pack(side=tk.RIGHT, padx=10)

        entertainment_button_width = self.winfo_screenwidth() // 4  # 大约屏幕宽度的25%
        self.entertainment_button = tk.Button(self, text="娱乐", command=self.open_entertainment,
                                              width=entertainment_button_width, font=("Arial", 16))
        self.entertainment_button.pack(side=tk.RIGHT, padx=10)

        self.dark_mode_button = tk.Button(self, text="切换暗黑模式", command=self.toggle_dark_mode, font=("Arial", 12))
        self.dark_mode_button.place(relx=0.95, rely=0.95, anchor="se")

        self.dark_mode = False
        self.update_time()

    def open_tool(self):
        tool_window = TimerApp(self)

    def open_calculator(self):
        calculator_window = CalculatorApp(self)

    def open_entertainment(self):
        # 在这里实现娱乐界面的逻辑（可选）
        pass

    def open_ai(self):
        # 在这里实现人工智能界面的逻辑（占位符）
        pass

    def toggle_dark_mode(self):
        current_bg = self.cget("bg")

        if self.dark_mode:
            self.configure(bg="white")
            self.tool_button.configure(bg="white")
            self.calculator_button.configure(bg="white")
            self.ai_button.configure(bg="white")
            self.entertainment_button.configure(bg="white")
            self.dark_mode_button.configure(bg="white", fg="black")
        else:
            self.configure(bg="black")
            self.tool_button.configure(bg="black")
            self.calculator_button.configure(bg="black")
            self.ai_button.configure(bg="black")
            self.entertainment_button.configure(bg="black")
            self.dark_mode_button.configure(bg="black", fg="white")

        self.dark_mode = not self.dark_mode

    def update_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.time_label = tk.Label(self, text=current_time, font=("Arial", 12), fg="white", bg="black")
        self.time_label.place(relx=0.5, rely=0.1, anchor="n")
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
