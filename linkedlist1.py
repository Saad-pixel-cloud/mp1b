import tkinter as tk
from PIL import Image, ImageTk
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Visualization")
        self.root.geometry("900x600")
        self.root.config(bg="#1e1e2e")
        
        self.canvas = tk.Canvas(root, width=880, height=300, bg="black")
        self.canvas.pack(pady=20)

        self.head = None
        self.nodes = []

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack()

        button_frame = tk.Frame(root, bg="#1e1e2e")
        button_frame.pack()

        tk.Button(button_frame, text="Create Linked List", font=("Arial", 12), bg="green", fg="white", command=self.create_linked_list).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Insert at Beginning", font=("Arial", 12), bg="blue", fg="white", command=self.insert_at_beginning).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Insert at End", font=("Arial", 12), bg="blue", fg="white", command=self.insert_at_end).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(button_frame, text="Delete Node", font=("Arial", 12), bg="red", fg="white", command=self.delete_node).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(button_frame, text="Search Node", font=("Arial", 12), bg="orange", fg="white", command=self.search_node).grid(row=0, column=4, padx=10, pady=5)

    

        self.message_label = tk.Label(root, text="", font=("Arial", 14), bg="black", fg="white", width=80, height=2)
        self.message_label.pack(pady=10)

    def update_message(self, message):
        self.message_label.config(text=message)

    def draw_linked_list(self, highlight_index=None):
        self.canvas.delete("all")
        x, y = 50, 150
        spacing = 100

        for i, (node, _, _) in enumerate(self.nodes):
            color = "yellow" if i == highlight_index else "lightblue"
            self.canvas.create_rectangle(x, y, x + 70, y + 50, fill=color)
            self.canvas.create_text(x + 35, y + 25, text=str(node.value), font=("Arial", 14, "bold"))
            
            if node.next:
                self.canvas.create_line(x + 70, y + 25, x + spacing, y + 25, arrow=tk.LAST, fill="white")
            
            x += spacing
        
        self.root.update()

    def create_linked_list(self):
        self.update_message("Creating Linked List")
        input_str = self.entry.get().strip()
        if input_str:
            self.head = None
            self.nodes.clear()
            numbers = input_str.split()
            for num in numbers:
                new_node = Node(num)
                if not self.head:
                    self.head = new_node
                else:
                    temp = self.head
                    while temp.next:
                        temp = temp.next
                    temp.next = new_node
                
                self.nodes.append((new_node, 50 + len(self.nodes) * 100, 150))
                self.animate_insert()
            self.update_message("Linked List Created")

    def animate_insert(self):
        for _ in range(10):
            for i in range(len(self.nodes)):
                node, x, y = self.nodes[i]
                self.nodes[i] = (node, x + 5, y)
            self.draw_linked_list()
            time.sleep(0.05)

    def insert_at_beginning(self):
        self.update_message("Insert at Beginning")
        value = self.entry.get().strip()
        if value:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.nodes.insert(0, (new_node, 50, 150))
            self.animate_insert()
            self.update_message(f"Node {value} inserted at beginning")

    def insert_at_end(self):
        self.update_message("Insert at End")
        value = self.entry.get().strip()
        if value:
            new_node = Node(value)
            if not self.head:
                self.head = new_node
                self.nodes.append((new_node, 50, 150))
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
                self.nodes.append((new_node, 50 + len(self.nodes) * 100, 150))
                self.update_message(f"Node {value} inserted at end")
            self.animate_insert()

    def delete_node(self):
        self.update_message("Deleting Node")
        value = self.entry.get().strip()
        if value and self.head:
            if self.head.value == value:
                self.head = self.head.next
                self.nodes.pop(0)
                self.animate_insert()
                self.update_message(f"Node {value} deleted")
                return

            temp = self.head
            found = False
            while temp.next:
                if temp.next.value == value:
                    temp.next = temp.next.next
                    found = True
                    break
                temp = temp.next

            if found:
                for i in range(len(self.nodes)):
                    if self.nodes[i][0].value == value:
                        self.nodes.pop(i)
                        break
                self.animate_insert()
                self.update_message(f"Node {value} deleted")
            else:
                self.update_message(f"Node {value} not found")
        else:
            self.update_message(f"Node {value} not found")

    def search_node(self):
        self.update_message("Searching Node")
        value = self.entry.get().strip()
        temp = self.head
        index = 0
        found = False

        while temp:
            if temp.value == value:
                found = True
                self.highlight_node(index)
                self.update_message(f"Node {value} found at position {index + 1}")
                break
            temp = temp.next
            index += 1

        if not found:
            self.update_message(f"Node {value} not found")

    def highlight_node(self, index):
        self.draw_linked_list(highlight_index=index)

    def back_to_menu(self):
        self.root.destroy()

def open_linkedlist(prev_window, reopen_visualize_fn=None):
    prev_window.withdraw()
    ll_root = tk.Toplevel()
    ll_root.title("Linked List")
    app = LinkedListVisualizer(ll_root)

    def back_to_visualize():
        ll_root.destroy()
        if reopen_visualize_fn:
            reopen_visualize_fn()

    # Add a back button inside the linked list window
    back_btn = tk.Button(ll_root, text="Back to Visualize Menu", font=("Arial", 12), bg="red", fg="white", command=back_to_visualize)
    back_btn.pack(pady=10)

    ll_root.mainloop()
