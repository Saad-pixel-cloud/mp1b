import tkinter as tk
from tkinter import ttk
import random
import time
import threading

def open_advanced_sort_visualizer(parent_window):
    parent_window.withdraw()
    window = tk.Toplevel()
    window.title("Advanced Sorting Algorithm Visualizer")
    window.config(bg="#0D2137")

    def bubble_sort(data, draw_data, speed):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    draw_data(data, ["yellow" if x == j or x == j+1 else "red" for x in range(len(data))])
                    time.sleep(speed)
        draw_data(data, ["green"] * len(data))

    def quick_sort(data, draw_data, speed):
        def partition(low, high):
            pivot = data[high]
            i = low - 1
            for j in range(low, high):
                if data[j] < pivot:
                    i += 1
                    data[i], data[j] = data[j], data[i]
                    draw_data(data, ["yellow" if x == j or x == i else "red" for x in range(len(data))])
                    time.sleep(speed)
            data[i+1], data[high] = data[high], data[i+1]
            draw_data(data, ["yellow" if x == i+1 or x == high else "red" for x in range(len(data))])
            time.sleep(speed)
            return i+1

        def quick_sort_recursive(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_recursive(low, pi - 1)
                quick_sort_recursive(pi + 1, high)

        quick_sort_recursive(0, len(data) - 1)
        draw_data(data, ["green"] * len(data))

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
    }

    def generate_data():
        nonlocal data
        size = int(size_slider.get())
        data = [random.randint(5, 100) for _ in range(size)]
        draw_data(data, ["yellow"] * len(data))

    def draw_data(data, colors):
        canvas.delete("all")
        canvas_height = 300
        canvas_width = 600
        bar_width = canvas_width / len(data)
        max_value = max(data)

        for i, value in enumerate(data):
            x0 = i * bar_width + 5
            y0 = canvas_height - (value / max_value) * (canvas_height - 20)
            x1 = (i + 1) * bar_width - 5
            y1 = canvas_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
            canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(value), fill="white")

        window.update_idletasks()

    def start_sorting():
        algo = algo_menu.get()
        speed = speed_slider.get()
        threading.Thread(target=sorting_algorithms[algo], args=(data, draw_data, speed), daemon=True).start()

    def get_time_complexity(algo):
        if algo == "Bubble Sort":
            return (
                "Bubble Sort:\n"
                "- Best Case: O(n)\n"
                "- Average/Worst Case: O(n²)\n"
                "- Space: O(1)\n"
                "- Stable: Yes\n"
            )
        elif algo == "Quick Sort":
            return (
                "Quick Sort:\n"
                "- Best/Average Case: O(n log n)\n"
                "- Worst Case: O(n²)\n"
                "- Space: O(log n)\n"
                "- Stable: No\n"
            )
        return "No info available"

    def compare_algorithms():
        nonlocal data
        algo1 = compare_algo1.get()
        algo2 = compare_algo2.get()
        speed = speed_slider.get()

        data1 = data.copy()
        data2 = data.copy()

        threading.Thread(target=lambda: sorting_algorithms[algo1](data1, lambda d, c: draw_data_compare(d, c, compare_canvas1), speed), daemon=True).start()
        threading.Thread(target=lambda: sorting_algorithms[algo2](data2, lambda d, c: draw_data_compare(d, c, compare_canvas2), speed), daemon=True).start()

        theory_text.config(state="normal")
        theory_text.delete("1.0", tk.END)
        theory_text.insert(tk.END, f"Comparison: {algo1} vs {algo2}\n\n")
        theory_text.insert(tk.END, get_time_complexity(algo1) + "\n")
        theory_text.insert(tk.END, get_time_complexity(algo2) + "\n")
        theory_text.config(state="disabled")

    def draw_data_compare(data, colors, canvas):
        canvas.delete("all")
        canvas_height = 150
        canvas_width = 300
        bar_width = canvas_width / len(data)
        max_value = max(data)

        for i, value in enumerate(data):
            x0 = i * bar_width + 5
            y0 = canvas_height - (value / max_value) * (canvas_height - 20)
            x1 = (i + 1) * bar_width - 5
            y1 = canvas_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])

        window.update_idletasks()

    def go_back():
        window.destroy()
        parent_window.deiconify()

    data = []

    # UI Components
    algo_menu = ttk.Combobox(window, values=list(sorting_algorithms.keys()))
    algo_menu.grid(row=0, column=0, padx=10, pady=5)
    algo_menu.current(0)

    speed_slider = tk.Scale(window, from_=0.1, to=5.0, resolution=0.1, orient="horizontal", label="Speed")
    speed_slider.grid(row=0, column=1)

    size_slider = tk.Scale(window, from_=5, to=50, resolution=1, orient="horizontal", label="Size")
    size_slider.grid(row=0, column=2)

    tk.Button(window, text="Generate", command=generate_data, bg="green").grid(row=0, column=3)
    tk.Button(window, text="Start", command=start_sorting, bg="orange").grid(row=0, column=4)

    # Back Button
    tk.Button(window, text="Back", command=go_back, bg="red", fg="white").grid(row=0, column=5, padx=10)

    canvas = tk.Canvas(window, width=600, height=300, bg="black")
    canvas.grid(row=1, column=0, columnspan=6)

    compare_algo1 = ttk.Combobox(window, values=list(sorting_algorithms.keys()))
    compare_algo1.grid(row=2, column=0)

    compare_algo2 = ttk.Combobox(window, values=list(sorting_algorithms.keys()))
    compare_algo2.grid(row=2, column=1)

    tk.Button(window, text="Compare", command=compare_algorithms, bg="orange").grid(row=2, column=2)

    compare_canvas1 = tk.Canvas(window, width=300, height=150, bg="black")
    compare_canvas1.grid(row=3, column=0)

    compare_canvas2 = tk.Canvas(window, width=300, height=150, bg="black")
    compare_canvas2.grid(row=3, column=1)

    theory_text = tk.Text(window, height=10, width=50, state="disabled", bg="#0D2137", fg="white")
    theory_text.grid(row=1, column=6, rowspan=3)
