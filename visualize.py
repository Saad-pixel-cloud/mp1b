import tkinter as tk
from tkinter import *

from PIL import Image, ImageTk
import linkedlist1
import arrays
from stack import StackVisualizer 
from BST import open_bst_visualizer
from BT import open_bt_tree_visualizer
from heap_tree import open_heap_visualizer
from avl_tree import open_avl_visualizer
from queue_vis import QueueVisualizer
from graph import open_graph_visualizer
from sort_gui import open_sorting_comparator


def open_visualize(main_window):
    """Opens the visualize window and allows returning to the main window."""
    vis_root = tk.Toplevel()
    vis_root.title("Visualize Data Structure")
    vis_root.geometry("900x550")
    vis_root.configure(bg="white")

    # Go back to main menu
    def back_to_main():
        vis_root.destroy()
        main_window.deiconify()

    # Open Queue visualizer
    def open_queue_visualizer():
        queue_root = Toplevel()
        QueueVisualizer(queue_root)
    # Open Stack visualizer
    def open_stack_visualizer(parent_window):
        parent_window.withdraw()
        stack_window = tk.Toplevel(parent_window)
        stack_window.title("Stack Visualization")
        stack_window.geometry("900x700")
        stack_window.configure(bg="#1e1e2e")

        StackVisualizer(stack_window, parent_window)
        stack_window.protocol("WM_DELETE_WINDOW", lambda: back_to_visualize(parent_window, stack_window))

    # Back to visualize screen
    def back_to_visualize(parent_window, current_window):
        current_window.destroy()
        parent_window.deiconify()

    # Resize background
    def resize_bg(event=None, label=None, img=None):
        new_width = label.winfo_width()
        new_height = label.winfo_height()
        resized_img = img.resize((new_width, new_height))
        new_bg_image = ImageTk.PhotoImage(resized_img)
        label.config(image=new_bg_image)
        label.image = new_bg_image

    # Load background image
    try:
        bg_img = Image.open("images/frontpage.png")
        bg_img = bg_img.resize((900, 550))
        bg_image = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(vis_root, image=bg_image)
        bg_label.pack(fill="both", expand=True)
    except Exception as e:
        bg_label = tk.Label(vis_root, text="[Image Not Found]", font=("Arial", 12), bg="white")
        bg_label.pack(fill="both", expand=True)

    vis_root.bind("<Configure>", lambda event: resize_bg(event, bg_label, bg_img))

    overlay_frame = tk.Frame(bg_label, bg="")
    overlay_frame.pack(fill="both", expand=True)

    # Title
    title_label = tk.Label(
        overlay_frame,
        text="Visualize Data Structure",
        font=("Arial", 20, "bold"),
        bg="yellow",
        fg="red",
        padx=15,
        pady=8
    )
    title_label.pack(pady=20)

    # Buttons frame
    button_frame = tk.Frame(overlay_frame, bg="")
    button_frame.pack(pady=20)

    # Actions dictionary
    actions = {
        # "Arrays": lambda: arrays.open_arrays(vis_root),
        "Linked Lists": lambda: linkedlist1.open_linkedlist(vis_root, lambda: open_visualize(main_window)), 
        "Stacks": lambda: open_stack_visualizer(vis_root),
        "Queues": lambda: open_queue_visualizer(),
        "AVL Tree": lambda: open_avl_visualizer(vis_root),
        "BT Tree": lambda: open_bt_tree_visualizer(vis_root),
        "bst Tree": lambda: open_bst_visualizer(vis_root),
        "Heap Tree": lambda: open_heap_visualizer(vis_root),
        "Graphs": lambda: open_graph_visualizer(vis_root),
        "Advanced Sort": lambda: open_sorting_comparator(vis_root),
    }

    # Dynamically create buttons in rows (3 per row)
    buttons = list(actions.keys())
    rows = (len(buttons) + 2) // 3  # Total rows needed

    for i in range(rows):
        row_frame = tk.Frame(button_frame)
        row_frame.pack(pady=5)
        for j in range(3):
            index = i * 3 + j
            if index >= len(buttons):
                break
            btn_text = buttons[index]
            btn = tk.Button(
                row_frame,
                text=btn_text,
                font=("Arial", 12, "bold"),
                bg="yellow",
                fg="black",
                padx=30,
                pady=10,
                bd=3,
                relief="raised",
                width=15,
                height=2,
                command=actions[btn_text]
            )
            btn.pack(side="left", padx=20)

    # Back button
    back_btn = tk.Button(
        overlay_frame,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        bg="red",
        fg="white",
        padx=20,
        pady=10,
        bd=3,
        relief="raised",
        command=back_to_main
    )
    back_btn.pack(pady=20)

    vis_root.mainloop()
