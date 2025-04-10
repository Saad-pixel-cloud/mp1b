from tkinter import *

class BSTVisualizer:
    def __init__(self, root, prev_window):
        self.root = root
        self.prev_window = prev_window

        self.main_frame = Frame(root, bg="#1e1e2e")
        self.main_frame.pack(fill=BOTH, expand=True)

        Label(self.main_frame, text="Binary Search Tree Visualization", font=("Arial", 18, "bold"), fg="white", bg="#1e1e2e").pack(pady=10)

        self.entry = Entry(self.main_frame, font=("Arial", 14))
        self.entry.pack(pady=10)

        btn_frame = Frame(self.main_frame, bg="#1e1e2e")
        btn_frame.pack(pady=5)

        Button(btn_frame, text="Insert", font=("Arial", 12), bg="green", fg="white", command=self.insert).grid(row=0, column=0, padx=10)
        Button(btn_frame, text="Search", font=("Arial", 12), bg="blue", fg="white", command=self.search).grid(row=0, column=1, padx=10)
        Button(btn_frame, text="Back", font=("Arial", 12), bg="gray", fg="white", command=self.go_back).grid(row=0, column=2, padx=10)

        self.canvas = Canvas(self.main_frame, bg="black", width=800, height=400)
        self.canvas.pack(pady=20)

        self.message_label = Label(self.main_frame, text="", font=("Arial", 12), fg="yellow", bg="#1e1e2e")
        self.message_label.pack()

        self.tree = None

    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def insert(self):
        value = self.entry.get().strip()
        if value:
            try:
                num = int(value)
                self.tree = self._insert(self.tree, num)
                self.entry.delete(0, END)
                self.message_label.config(text=f"Inserted {num}")
                self.draw_tree()
            except ValueError:
                self.message_label.config(text="Enter a valid integer")

    def _insert(self, root, key):
        if root is None:
            return self.Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self):
        value = self.entry.get().strip()
        if value:
            try:
                num = int(value)
                found = self._search(self.tree, num)
                self.message_label.config(text=f"{'Found' if found else 'Not Found'} {num}")
            except ValueError:
                self.message_label.config(text="Enter a valid integer")

    def _search(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_node(self.tree, 400, 30, 200)

    def _draw_node(self, node, x, y, offset):
        if node:
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.key), font=("Arial", 12, "bold"))

            if node.left:
                self.canvas.create_line(x, y, x - offset, y + 60, fill="white")
                self._draw_node(node.left, x - offset, y + 60, offset // 2)

            if node.right:
                self.canvas.create_line(x, y, x + offset, y + 60, fill="white")
                self._draw_node(node.right, x + offset, y + 60, offset // 2)

    def go_back(self):
        self.root.destroy()
        self.prev_window.deiconify()

def open_bst_visualizer(prev_window):
    prev_window.withdraw()
    bst_root = Toplevel()
    bst_root.title("BST Tree Visualizer")
    bst_root.geometry("900x600")
    BSTVisualizer(bst_root, prev_window)
