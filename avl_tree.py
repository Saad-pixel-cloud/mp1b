from tkinter import *
import math
import tkinter as tk

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
        self.entry.pack(pady=5)

        btn_frame = Frame(root, bg="#1e1e2e")
        btn_frame.pack()

        Button(btn_frame, text="Insert", font=("Arial", 12), bg="blue", fg="white", command=self.insert).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Delete", font=("Arial", 12), bg="red", fg="white", command=self.delete).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Search", font=("Arial", 12), bg="green", fg="white", command=self.search).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Clear", font=("Arial", 12), bg="gray", fg="white", command=self.clear_screen).pack(side=LEFT, padx=5)
        Button(btn_frame, text="Back", font=("Arial", 12), bg="orange", fg="black", command=root.destroy).pack(side=LEFT, padx=5)

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

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def _insert_node(self, node, value):
        if not node:
            return AVLNode(value)
        elif value < node.value:
            node.left = self._insert_node(node.left, value)
        elif value > node.value:
            node.right = self._insert_node(node.right, value)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # LL
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        # RR
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        # LR
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # RL
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def _delete_node(self, root, key):
        if not root:
            return root
        elif key < root.value:
            root.left = self._delete_node(root.left, key)
        elif key > root.value:
            root.right = self._delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._get_min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete_node(root.right, temp.value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Balance cases
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

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
        if node:
            if node.left:
                self.canvas.create_line(x, y, x - spacing, y + 60, fill="white")
                self._draw_tree(node.left, x - spacing, y + 60, spacing // 2)
            if node.right:
                self.canvas.create_line(x, y, x + spacing, y + 60, fill="white")
                self._draw_tree(node.right, x + spacing, y + 60, spacing // 2)
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 14, "bold"))

def open_avl_visualizer(parent_window):
    parent_window.withdraw()
    avl_window = tk.Toplevel()
    avl_window.title("AVL Tree Visualizer")
    avl_window.geometry("1000x600")
    avl_window.config(bg="#1e1e2e")

    AVLTreeVisualizer(avl_window)

    def on_close():
        avl_window.destroy()
        parent_window.deiconify()

    avl_window.protocol("WM_DELETE_WINDOW", on_close)
