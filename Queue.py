from tkinter import *
import time

class QueueVisualizer:
    """Class to visualize a queue with enqueue, dequeue, and utility operations."""
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Visualization")
        self.root.geometry("1000x600")
        self.root.config(bg="#1e1e2e")
        
        self.queue = []
        self.queue_size = 5  # Default size, can be changed by user

        # UI Elements
        Label(root, text="Queue Size:", font=("Arial", 12), bg="#1e1e2e", fg="white").pack()
        self.size_entry = Entry(root, font=("Arial", 12))
        self.size_entry.pack()
        Button(root, text="Set Size", font=("Arial", 12), bg="purple", fg="white", command=self.set_queue_size).pack(pady=5)
        
        self.entry = Entry(root, font=("Arial", 14))
        self.entry.pack()

        button_frame = Frame(root, bg="#1e1e2e")
        button_frame.pack()

        Button(button_frame, text="Enqueue", font=("Arial", 12), bg="blue", fg="white", command=self.enqueue).grid(row=0, column=0, padx=10, pady=5)
        Button(button_frame, text="Dequeue", font=("Arial", 12), bg="red", fg="white", command=self.dequeue).grid(row=0, column=1, padx=10, pady=5)
        Button(button_frame, text="Peek Front", font=("Arial", 12), bg="orange", fg="white", command=self.peek).grid(row=0, column=2, padx=10, pady=5)
        Button(button_frame, text="Rear", font=("Arial", 12), bg="brown", fg="white", command=self.rear).grid(row=0, column=3, padx=10, pady=5)
        Button(button_frame, text="Is Full?", font=("Arial", 12), bg="purple", fg="white", command=self.isFull).grid(row=0, column=4, padx=10, pady=5)
        Button(button_frame, text="Is Empty?", font=("Arial", 12), bg="gray", fg="white", command=self.isEmpty).grid(row=0, column=5, padx=10, pady=5)
        Button(button_frame, text="Size", font=("Arial", 12), bg="green", fg="white", command=self.size).grid(row=0, column=6, padx=10, pady=5)

        self.message_label = Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
        self.message_label.pack(pady=10)

        self.canvas = Canvas(root, width=900, height=300, bg="black")
        self.canvas.pack(pady=20)

    def set_queue_size(self):
        """Set the queue size from user input."""
        try:
            self.queue_size = int(self.size_entry.get())
            self.message_label.config(text=f"Queue size set to {self.queue_size}")
        except ValueError:
            self.message_label.config(text="Invalid queue size")
    
    def draw_queue(self):
        """Draw the queue elements on the canvas."""
        self.canvas.delete("all")
        x, y = 50, 150
        spacing = 90

        for i, value in enumerate(self.queue):
            self.canvas.create_rectangle(x, y, x + 70, y + 50, fill="lightblue")
            self.canvas.create_text(x + 35, y + 25, text=str(value), font=("Arial", 14, "bold"))
            if i == 0:
                self.canvas.create_text(x + 35, y + 70, text="Front", font=("Arial", 12, "bold"), fill="white")
            if i == len(self.queue) - 1:
                self.canvas.create_text(x + 35, y - 20, text="Rear", font=("Arial", 12, "bold"), fill="white")
            x += spacing

    def enqueue(self):
        """Insert an element into the queue."""
        value = self.entry.get().strip()
        if self.isFull():
            self.message_label.config(text="Queue is full!")
            return
        elif not value:
            self.message_label.config(text="Please enter a value.")
        elif value:
            self.queue.append(value)
            self.entry.delete(0, END)
            self.message_label.config(text="Enqueue successful.")
            self.draw_queue()

    def dequeue(self):
        """Remove the front element from the queue."""
        if self.isEmpty():
            self.message_label.config(text="Queue is empty!")
            return
        else:
            self.queue.pop(0)
            self.message_label.config(text="Dequeue successful.")
            self.draw_queue()

    def peek(self):
        """Return the front element without removing it."""
        if self.isEmpty():
            self.message_label.config(text="Queue is empty!")
        else:
            self.message_label.config(text=f"Front element: {self.queue[0]}")
    
    def rear(self):
        """Return the rear element without removing it."""
        if self.isEmpty():
            self.message_label.config(text="Queue is empty!")
        else:
            self.message_label.config(text=f"Rear element: {self.queue[-1]}")

    def isFull(self):
        """Check if the queue is full."""
        if len(self.queue) >= self.queue_size:
            self.message_label.config(text="Queue is Full!", fg="red")
            return True
        else:
            self.message_label.config(text="Queue is NOT Full", fg="white")
            return False

    def isEmpty(self):
        """Check if the queue is empty."""
        if not self.queue:
            self.message_label.config(text="Queue is Empty!", fg="red")
            return True
        else:
            self.message_label.config(text="Queue is NOT Empty", fg="white")
            return False
    
    def size(self):
        """Return the current size of the queue."""
        self.message_label.config(text=f"Current queue size: {len(self.queue)}")

if __name__ == "__main__":
    root = Tk()
    app = QueueVisualizer(root)
    root.mainloop()
