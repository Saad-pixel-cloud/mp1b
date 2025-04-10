from tkinter import *
import heapq

class HeapVisualizer:
    """Class to visualize a Heap (Min-Heap by default) with insertion and deletion."""
    def __init__(self, root):
        self.root = root
        self.root.title("Heap Tree Visualization")
        self.root.geometry("1000x600")
        self.root.config(bg="#1e1e2e")

        self.canvas = Canvas(root, width=900, height=500, bg="black")
        self.canvas.pack(pady=20)

        self.heap = []  # List representing a Min-Heap

        # UI Elements
        self.entry = Entry(root, font=("Arial", 14))
        self.entry.pack()

        Button(root, text="Insert", font=("Arial", 12), bg="blue", fg="white", command=self.insert).pack(pady=5)
        Button(root, text="Extract Min", font=("Arial", 12), bg="red", fg="white", command=self.extract_min).pack(pady=5)
        Button(root, text="Clear Screen", font=("Arial", 12), bg="gray", fg="white", command=self.clear_screen).pack(pady=5)

        self.message_label = Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
        self.message_label.pack(pady=10)

    def insert(self):
        """Insert multiple values into the heap."""
        values = self.entry.get().strip().split()
        valid_values = [int(v) for v in values if v.isdigit() and 0 <= int(v) <= 999]
        
        if valid_values:
            for value in valid_values:
                heapq.heappush(self.heap, value)
            self.entry.delete(0, END)
            self.message_label.config(text=f"Inserted {', '.join(map(str, valid_values))} into Heap")
            self.animate()

    def extract_min(self):
        """Extract the minimum element from the heap."""
        if self.heap:
            min_value = heapq.heappop(self.heap)
            self.message_label.config(text=f"Extracted Min: {min_value}")
            self.animate()
        else:
            self.message_label.config(text="Heap is empty.")

    def clear_screen(self):
        """Clear the heap visualization and reset the heap."""
        self.heap = []
        self.canvas.delete("all")
        self.message_label.config(text="Screen Cleared.")

    def animate(self):
        """Animate the heap drawing process."""
        self.canvas.delete("all")
        self.draw_heap()
        self.root.update()

    def draw_heap(self):
        """Draw the heap as a complete binary tree."""
        if not self.heap:
            return
        
        level = 0
        index = 0
        x_start = 450
        y_start = 50
        x_offset = 200

        positions = {}
        queue = [(0, x_start, y_start, x_offset)]

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

# Main execution
if __name__ == "__main__":
    root = Tk()
    app = HeapVisualizer(root)
    root.mainloop()
