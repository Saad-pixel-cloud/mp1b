import tkinter as tk
import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeVisualizer:
    def __init__(self, root_window, parent_window):
        self.root = root_window
        self.parent_window = parent_window
        self.root.title("Binary Tree Visualization")
        self.root.geometry("1000x650")
        self.root.config(bg="#1e1e2e")

        self.tree = None

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
        tk.Button(button_row, text="Preorder", command=self.preorder, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Inorder", command=self.inorder, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Postorder", command=self.postorder, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Clear Screen", command=self.clear_screen, **btn_style).pack(side="left", padx=5)
        tk.Button(button_row, text="Back to Visualize", bg="red", fg="white", font=("Arial", 12, "bold"),
                  command=self.on_close).pack(side="left", padx=5)

        # Message Label
        self.message_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="white", bg="#1e1e2e")
        self.message_label.pack(pady=10)

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()
        self.parent_window.deiconify()

    def insert(self):
        values = self.entry.get().strip().split()
        valid_values = [int(v) for v in values if v.isdigit() and 0 <= int(v) <= 999]
        if valid_values:
            for value in valid_values:
                self.tree = self._insert_node(self.tree, value)
            self.entry.delete(0, tk.END)
            self.message_label.config(text=f"Inserted: {', '.join(map(str, valid_values))}")
            self.animate()

    def _insert_node(self, root, value):
        if root is None:
            return TreeNode(value)
        if random.choice([True, False]):
            root.left = self._insert_node(root.left, value)
        else:
            root.right = self._insert_node(root.right, value)
        return root

    def clear_screen(self):
        self.tree = None
        self.canvas.delete("all")
        self.message_label.config(text="Screen Cleared.")

    def animate(self):
        self.draw_tree(self.tree, 475, 50, 200)
        self.root.update()

    def draw_tree(self, root, x, y, x_offset):
        self.canvas.delete("all")
        if root is not None:
            self._draw_node(root, x, y, x_offset)

    def _draw_node(self, node, x, y, x_offset):
        if node.left is not None:
            self.canvas.create_line(x, y, x - x_offset, y + 80, fill="white")
            self._draw_node(node.left, x - x_offset, y + 80, x_offset // 2)
        if node.right is not None:
            self.canvas.create_line(x, y, x + x_offset, y + 80, fill="white")
            self._draw_node(node.right, x + x_offset, y + 80, x_offset // 2)

        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="white")
        self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 14, "bold"), fill="black")

    def preorder(self):
        result = []
        self._preorder_traversal(self.tree, result)
        self.message_label.config(text="Preorder: " + " -> ".join(map(str, result)))

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def inorder(self):
        result = []
        self._inorder_traversal(self.tree, result)
        self.message_label.config(text="Inorder: " + " -> ".join(map(str, result)))

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def postorder(self):
        result = []
        self._postorder_traversal(self.tree, result)
        self.message_label.config(text="Postorder: " + " -> ".join(map(str, result)))

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

# Function to be called from visualize menu
def open_bt_tree_visualizer(parent_window):
    parent_window.withdraw()
    new_window = tk.Toplevel(parent_window)
    BinaryTreeVisualizer(new_window, parent_window)
