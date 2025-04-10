from tkinter import *
import time

class StackVisualizer:
    def __init__(self, root, main_window_ref):
        self.root = root
        self.main_window_ref = main_window_ref  # Reference to visualize menu

        self.stack_frame = Frame(root, bg="#1e1e2e")
        self.stack_frame.pack(fill=BOTH, expand=True)

        Label(self.stack_frame, text="Stack Visualization", font=("Arial", 16, "bold"),
              bg="#1e1e2e", fg="white").pack(pady=10)

        self.stack = []
        self.stack_items = []

        self.canvas = Canvas(self.stack_frame, width=800, height=500, bg="black")
        self.canvas.pack(pady=20)

        self.entry = Entry(self.stack_frame, font=("Arial", 14))
        self.entry.pack(pady=10)

        button_frame = Frame(self.stack_frame, bg="#1e1e2e")
        button_frame.pack()

        Button(button_frame, text="Push", font=("Arial", 14), bg="green", fg="white",
               command=self.push).grid(row=0, column=0, padx=10, pady=5)
        Button(button_frame, text="Pop", font=("Arial", 14), bg="red", fg="white",
               command=self.pop).grid(row=0, column=1, padx=10, pady=5)
        Button(button_frame, text="Peek", font=("Arial", 14), bg="blue", fg="white",
               command=self.peek).grid(row=0, column=2, padx=10, pady=5)
        Button(button_frame, text="Is Empty?", font=("Arial", 14), bg="purple", fg="white",
               command=self.is_empty).grid(row=0, column=3, padx=10, pady=5)
        Button(button_frame, text="Clear Stack", font=("Arial", 14), bg="orange", fg="white",
               command=self.clear_stack).grid(row=0, column=4, padx=10, pady=5)
        Button(button_frame, text="Back", font=("Arial", 14), bg="gray", fg="white",
               command=self.go_back).grid(row=0, column=5, padx=10, pady=5)

    def draw_stack(self):
        self.canvas.delete("all")
        x, y = 400, 450
        box_height = 50

        for value in self.stack:
            self.canvas.create_rectangle(x-50, y-box_height, x+50, y, fill="lightblue")
            self.canvas.create_text(x, y - 25, text=str(value), font=("Arial", 14, "bold"))
            y -= box_height + 5

    def push(self):
        value = self.entry.get().strip()
        if value:
            self.stack.append(value)
            self.entry.delete(0, END)
            self.show_message(f"Element pushed:", "blue")
            self.draw_stack()
        else:
            self.show_message("Enter a value to push!", "red")

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.show_message(f"Element poped:", "blue")
            self.draw_stack()
        else:
            self.show_message("Stack is Empty! Nothing to pop", "red")

    def peek(self):
        if self.stack:
            self.show_message(f"Top element: {self.stack[-1]}", "blue")
        else:
            self.show_message("Stack is Empty! Nothing to peek", "red")

    def is_empty(self):
        if not self.stack:
            self.show_message("Stack is Empty!", "red")
        else:
            self.show_message("Stack is NOT Empty!", "green")

    def clear_stack(self):
        self.stack.clear()
        self.canvas.delete("all")

    def show_message(self, message, color):
        label = Label(self.stack_frame, text=message, font=("Arial", 14), bg="#1e1e2e", fg=color)
        label.pack(pady=5)
        self.root.after(2000, label.destroy)

    def go_back(self):
        self.root.destroy()                 # Close current window
        self.main_window_ref.deiconify()   # Show the visualize menu again

def open_stack_visualizer(prev_window):
    prev_window.withdraw()                     # Hide the visualize window
    stack_root = Toplevel()
    stack_root.title("Stack Visualizer")
    stack_root.geometry("900x600")
    StackVisualizer(stack_root, prev_window)
