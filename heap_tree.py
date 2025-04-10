import tkinter as tk
import heapq

class HeapVisualizer:
    def __init__(self, root_window, parent_window):
        self.root = root_window
        self.parent_window = parent_window
        self.root.title("Heap Tree Visualization")
        self.root.geometry("1000x650")
        self.root.config(bg="#1e1e2e")

        self.heap = []

        # Canvas
        self.canvas = tk.Canvas(self.root, width=950, height=400, bg="black")
        self.canvas.pack(pady=20)

        # Entry
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=5)

        # Button Row Frame
        button_row = tk.Frame(self.root, bg="#1e1e2e")
        button_row.pack(pady=10)

        btn_style = {"font": ("Arial", 12, "bold"), "bg": "yellow", "fg": "black", "padx": 10, "pady": 5}

        tk.Button(button_row, text="Insert", command=self.insert, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Extract Min", command=self.extract_min, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Clear Screen", command=self.clear_screen, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Back to Visualize", bg="red", fg="white", font=("Arial", 12, "bold"),
                  command=self.on_close).pack(side="left", padx=5)

        # Message Label
        self.message_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
        self.message_label.pack(pady=10)

        # Close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()
        self.parent_window.deiconify()

    def insert(self):
        values = self.entry.get().strip().split()
        valid_values = [int(v) for v in values if v.isdigit() and 0 <= int(v) <= 999]
        if valid_values:
            for value in valid_values:
                heapq.heappush(self.heap, value)
            self.entry.delete(0, tk.END)
            self.message_label.config(text=f"Inserted: {', '.join(map(str, valid_values))}")
            self.animate()

    def extract_min(self):
        if self.heap:
            min_value = heapq.heappop(self.heap)
            self.message_label.config(text=f"Extracted Min: {min_value}")
            self.animate()
        else:
            self.message_label.config(text="Heap is empty.")

    def clear_screen(self):
        self.heap = []
        self.canvas.delete("all")
        self.message_label.config(text="Screen Cleared.")

    def animate(self):
        self.canvas.delete("all")
        self.draw_heap()
        self.root.update()

    def draw_heap(self):
        if not self.heap:
            return
        
        positions = {}
        queue = [(0, 475, 50, 200)]

        while queue:
            i, x, y, offset = queue.pop(0)
            positions[i] = (x, y)
            if 2 * i + 1 < len(self.heap):
                queue.append((2 * i + 1, x - offset, y + 80, offset // 2))
            if 2 * i + 2 < len(self.heap):
                queue.append((2 * i + 2, x + offset, y + 80, offset // 2))

        for i in positions:
            x, y = positions[i]
            if 2 * i + 1 in positions:
                x2, y2 = positions[2 * i + 1]
                self.canvas.create_line(x, y, x2, y2, fill="white")
            if 2 * i + 2 in positions:
                x2, y2 = positions[2 * i + 2]
                self.canvas.create_line(x, y, x2, y2, fill="white")
            
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="white")
            self.canvas.create_text(x, y, text=str(self.heap[i]), font=("Arial", 14, "bold"), fill="black")

# Function to be used from visualize menu
def open_heap_visualizer(parent_window):
    parent_window.withdraw()
    new_window = tk.Toplevel(parent_window)
    HeapVisualizer(new_window, parent_window)
