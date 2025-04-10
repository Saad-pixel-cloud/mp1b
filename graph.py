import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class GraphVisualizer:
    def __init__(self, root, parent_window):
        self.root = root
        self.parent_window = parent_window
        self.root.title("Graph Visualizer")
        self.root.geometry("1000x600")
        self.root.config(bg="#1e1e2e")

        self.canvas = tk.Canvas(root, bg="white", width=950, height=500)
        self.canvas.pack(pady=10)

        self.nodes = {}
        self.edges = []
        self.node_count = 0

        control_frame = tk.Frame(root, bg="#1e1e2e")
        control_frame.pack()

        tk.Button(control_frame, text="Add Node", command=self.add_node, bg="green", fg="white").pack(side="left", padx=5)
        tk.Button(control_frame, text="Add Edge", command=self.add_edge, bg="blue", fg="white").pack(side="left", padx=5)
        tk.Button(control_frame, text="DFS", command=self.dfs_ui, bg="purple", fg="white").pack(side="left", padx=5)
        tk.Button(control_frame, text="BFS", command=self.bfs_ui, bg="orange", fg="black").pack(side="left", padx=5)
        tk.Button(control_frame, text="Clear", command=self.clear, bg="gray", fg="white").pack(side="left", padx=5)
        tk.Button(control_frame, text="Back", command=self.go_back, bg="red", fg="white").pack(side="left", padx=5)

    def add_node(self):
        name = chr(65 + self.node_count)
        x = random.randint(50, 900)
        y = random.randint(50, 450)
        self.nodes[name] = (x, y)
        self.node_count += 1
        self.draw()

    def add_edge(self):
        start = simpledialog.askstring("Start Node", "From node:")
        end = simpledialog.askstring("End Node", "To node:")
        if start in self.nodes and end in self.nodes:
            self.edges.append((start, end))
            self.draw()
        else:
            messagebox.showerror("Error", "Invalid node names")

    def draw(self):
        self.canvas.delete("all")
        for start, end in self.edges:
            x1, y1 = self.nodes[start]
            x2, y2 = self.nodes[end]
            self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, width=2)
        for name, (x, y) in self.nodes.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="skyblue")
            self.canvas.create_text(x, y, text=name, font=("Arial", 12, "bold"))

    def dfs_ui(self):
        start = simpledialog.askstring("DFS Start", "Enter start node:")
        visited = self.dfs(start)
        messagebox.showinfo("DFS Order", " → ".join(visited))

    def bfs_ui(self):
        start = simpledialog.askstring("BFS Start", "Enter start node:")
        visited = self.bfs(start)
        messagebox.showinfo("BFS Order", " → ".join(visited))

    def dfs(self, start):
        visited, stack = [], [start]
        while stack:
            node = stack.pop()
            if node in self.nodes and node not in visited:
                visited.append(node)
                neighbors = [end for s, end in self.edges if s == node]
                stack.extend(reversed(neighbors))
        return visited

    def bfs(self, start):
        visited, queue = [], [start]
        while queue:
            node = queue.pop(0)
            if node in self.nodes and node not in visited:
                visited.append(node)
                neighbors = [end for s, end in self.edges if s == node]
                queue.extend(neighbors)
        return visited

    def clear(self):
        self.nodes.clear()
        self.edges.clear()
        self.node_count = 0
        self.canvas.delete("all")

    def go_back(self):
        self.root.destroy()
        self.parent_window.deiconify()

def open_graph_visualizer(parent_window):
    parent_window.withdraw()
    graph_win = tk.Toplevel()
    GraphVisualizer(graph_win, parent_window)
