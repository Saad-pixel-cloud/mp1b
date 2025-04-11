import tkinter as tk
import webbrowser

def open_learn_ds(parent_window):
    parent_window.withdraw()
    learn_window = tk.Toplevel()
    learn_window.title("Learn Data Structures")
    learn_window.geometry("800x600")
    learn_window.configure(bg="#1e1e2e")

    topics = {
        "Stack": "https://youtu.be/_6COl6V6mng",
        "Queue": "https://youtu.be/okr-XE8yTO8",
        "Linked List": "https://youtu.be/6s1YQDfKq1A",
        "Doubly Linked List": "https://youtu.be/JdQeNxWCguQ",
        "Circular Linked List": "https://youtu.be/BzRnNc9NYuU",
        "Binary Tree": "https://youtu.be/_Lr3dOub7vU",
        "AVL Tree": "https://youtu.be/jDM6_TnYIqE",
        "Heap": "https://youtu.be/HqPJF2L5h9U",
        "Graph": "https://youtu.be/gXgEDyodOJU",
        "Hash Table": "https://youtu.be/2Ti5yvumFTU",
        "Trie": "https://youtu.be/zIjfhVPRZCg",
        "Sorting Algorithms": "https://youtu.be/kgBjXUE_Nwc"
    }

    def open_video(url):
        webbrowser.open_new_tab(url)

    frame = tk.Frame(learn_window, bg="#1e1e2e")
    frame.pack(expand=True)

    row = 0
    col = 0
    for topic, link in topics.items():
        btn = tk.Button(
            frame, text=topic, width=25, height=2,
            bg="#4dd0e1", fg="black", font=("Arial", 12, "bold"),
            command=lambda url=link: open_video(url)
        )
        btn.grid(row=row, column=col, padx=15, pady=15)
        col += 1
        if col > 2:
            col = 0
            row += 1

    def go_back():
        learn_window.destroy()
        parent_window.deiconify()

    back_btn = tk.Button(
        learn_window, text="Back", command=go_back,
        bg="red", fg="white", font=("Arial", 12, "bold")
    )
    back_btn.pack(pady=10)
