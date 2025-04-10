from tkinter import *
import time
import math

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("AVL Tree Visualization")
        self.root.geometry("1000x600")
        self.root.config(bg="#1e1e2e")

        self.canvas = Canvas(root, width=900, height=500, bg="black")
        self.canvas.pack(pady=20)

        self.tree = None

        self.entry = Entry(root, font=("Arial", 14))
        self.entry.pack()

        Button(root, text="Insert", font=("Arial", 12), bg="blue", fg="white", command=self.insert).pack(pady=5)
        Button(root, text="Delete", font=("Arial", 12), bg="red", fg="white", command=self.delete).pack(pady=5)
        Button(root, text="Search", font=("Arial", 12), bg="green", fg="white", command=self.search).pack(pady=5)
        Button(root, text="Clear Screen", font=("Arial", 12), bg="gray", fg="white", command=self.clear_screen).pack(pady=5)

        self.message_label = Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
        self.message_label.pack(pady=10)

    def clear_screen(self):
        self.tree = None
        self.canvas.delete("all")
        self.message_label.config(text="Screen Cleared.")

    def insert(self):
        values = self.entry.get().strip().split()
        valid_values = [int(v) for v in values if v.isdigit() and 0 <= int(v) <= 999]
        
        if valid_values:
            for value in valid_values:
                self.tree = self._insert_node(self.tree, value)
            self.entry.delete(0, END)
            self.message_label.config(text=f"Inserted {', '.join(map(str, valid_values))} into AVL Tree")
            self.animate()
    
    def delete(self):
        value = self.entry.get().strip()
        if value.isdigit():
            self.tree = self._delete_node(self.tree, int(value))
            self.entry.delete(0, END)
            self.message_label.config(text=f"Deleted {value} from AVL Tree")
            self.animate()
    
    def search(self):
        value = self.entry.get().strip()
        if value.isdigit():
            found = self._search_node(self.tree, int(value))
            if found:
                self.message_label.config(text=f"{value} found in AVL Tree")
            else:
                self.message_label.config(text=f"{value} not found in AVL Tree")
    
    # Placeholder AVL tree operations
    def _insert_node(self, node, value):
        if node is None:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert_node(node.left, value)
        else:
            node.right = self._insert_node(node.right, value)
        return node  # Balance logic needs to be added

    def _delete_node(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
        return node  # Balance logic needs to be added

    def _search_node(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_node(node.left, value)
        return self._search_node(node.right, value)

    def animate(self):
        self.canvas.delete("all")
        self._draw_tree(self.tree, 450, 50, 200)
    
    def _draw_tree(self, node, x, y, spacing):
        if node is not None:
            if node.left:
                self.canvas.create_line(x, y, x - spacing, y + 50, fill="white")
                self._draw_tree(node.left, x - spacing, y + 50, spacing // 2)
            if node.right:
                self.canvas.create_line(x, y, x + spacing, y + 50, fill="white")
                self._draw_tree(node.right, x + spacing, y + 50, spacing // 2)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 14, "bold"))

if __name__ == "__main__":
    root = Tk()
    app = AVLTreeVisualizer(root)
    root.mainloop()
