from tkinter import *
from tkinter import ttk
import random
import time
import threading

def open_sorting_comparator(parent=None):
    data1 = []
    data2 = []
    speed = 0.1

    def show_theory(label_widget, text):
        label_widget.config(state=NORMAL)
        label_widget.delete("1.0", END)
        label_widget.insert(END, text)
        label_widget.config(state=DISABLED)

    def bubble_sort(data, draw_data, speed, label_widget):
        for i in range(len(data) - 1):
            for j in range(len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    draw_data(data, ['yellow' if x == j or x == j + 1 else '#A90042' for x in range(len(data))])
                    time.sleep(speed)
        draw_data(data, ['yellow' for _ in range(len(data))])
        show_theory(label_widget, "Bubble Sort:\nTime: O(n²), Best: O(n), Stable: Yes, In-place: Yes")

    def selection_sort(data, draw_data, speed, label_widget):
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
                draw_data(data, ['yellow' if x == j or x == min_idx else '#A90042' for x in range(len(data))])
                time.sleep(speed)
            data[i], data[min_idx] = data[min_idx], data[i]
            draw_data(data, ['green' if x <= i else '#A90042' for x in range(len(data))])
        show_theory(label_widget, "Selection Sort:\nTime: O(n²), Best: O(n²), Stable: No, In-place: Yes")

    def insertion_sort(data, draw_data, speed, label_widget):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
                draw_data(data, ['yellow' if x == j or x == j + 1 else '#A90042' for x in range(len(data))])
                time.sleep(speed)
            data[j + 1] = key
            draw_data(data, ['green' if x <= i else '#A90042' for x in range(len(data))])
        show_theory(label_widget, "Insertion Sort:\nTime: O(n²), Best: O(n), Stable: Yes, In-place: Yes")

    def merge_sort(data, draw_data, speed, label_widget):
        def merge_sort_recursive(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_recursive(arr, left, mid)
                merge_sort_recursive(arr, mid + 1, right)
                merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            left_part = arr[left:mid + 1]
            right_part = arr[mid + 1:right + 1]
            i = j = 0
            k = left
            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    arr[k] = left_part[i]
                    i += 1
                else:
                    arr[k] = right_part[j]
                    j += 1
                draw_data(data, ['yellow' if x == k else '#A90042' for x in range(len(data))])
                time.sleep(speed)
                k += 1
            while i < len(left_part):
                arr[k] = left_part[i]
                draw_data(data, ['yellow' if x == k else '#A90042' for x in range(len(data))])
                time.sleep(speed)
                i += 1
                k += 1
            while j < len(right_part):
                arr[k] = right_part[j]
                draw_data(data, ['yellow' if x == k else '#A90042' for x in range(len(data))])
                time.sleep(speed)
                j += 1
                k += 1

        merge_sort_recursive(data, 0, len(data) - 1)
        draw_data(data, ['yellow' for _ in range(len(data))])
        show_theory(label_widget, "Merge Sort:\nTime: O(n log n), Best: O(n log n), Stable: Yes, In-place: No")

    def quick_sort(data, draw_data, speed, label_widget, low, high):
        if low < high:
            pi = partition(data, draw_data, speed, low, high)
            quick_sort(data, draw_data, speed, label_widget, low, pi - 1)
            quick_sort(data, draw_data, speed, label_widget, pi + 1, high)

    def partition(data, draw_data, speed, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                draw_data(data, ['yellow' if x == i or x == j else '#A90042' for x in range(len(data))])
                time.sleep(speed)
        data[i + 1], data[high] = data[high], data[i + 1]
        draw_data(data, ['yellow' if x == i + 1 or x == high else '#A90042' for x in range(len(data))])
        time.sleep(speed)
        return i + 1

    def quick_sort_wrapper(data, draw_data, speed, label_widget):
        quick_sort(data, draw_data, speed, label_widget, 0, len(data) - 1)
        draw_data(data, ['yellow' for _ in range(len(data))])
        show_theory(label_widget, "Quick Sort:\nTime: O(n log n), Worst: O(n²), Stable: No, In-place: Yes")

    def StartAlgorithms():
        threading.Thread(target=lambda: run_sort(selected_algorithm1.get(), data1, draw_data1, theory_label1), daemon=True).start()
        threading.Thread(target=lambda: run_sort(selected_algorithm2.get(), data2, draw_data2, theory_label2), daemon=True).start()

    def run_sort(algo, dataset, draw_func, label_widget):
        if algo == "Bubble Sort":
            bubble_sort(dataset, draw_func, speed, label_widget)
        elif algo == "Quick Sort":
            quick_sort_wrapper(dataset, draw_func, speed, label_widget)
        elif algo == "Selection Sort":
            selection_sort(dataset, draw_func, speed, label_widget)
        elif algo == "Insertion Sort":
            insertion_sort(dataset, draw_func, speed, label_widget)
        elif algo == "Merge Sort":
            merge_sort(dataset, draw_func, speed, label_widget)

    def draw_data1(data, color_array):
        draw_on_canvas(canvas1, data, color_array)

    def draw_data2(data, color_array):
        draw_on_canvas(canvas2, data, color_array)

    def draw_on_canvas(canvas, data, color_array):
        canvas.delete("all")
        c_height = 300
        c_width = 420
        bar_width = c_width / (len(data) + 1)
        offset = 10
        spacing = 5
        max_val = max(data) if data and max(data) != 0 else 1
        normalized_data = [i / max_val for i in data]
        for i, height in enumerate(normalized_data):
            x0 = i * bar_width + offset + spacing
            y0 = c_height - height * 290
            x1 = (i + 1) * bar_width + offset
            y1 = c_height
            canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), fill="white")
        win.update_idletasks()

    def set_speed(val):
        nonlocal speed
        speed = float(val)

    def generate_data():
        nonlocal data1, data2
        min_val = int(minvalue.get())
        max_val = int(maxvalue.get())
        size = int(sizevalue.get())
        array = [random.randint(min_val, max_val) for _ in range(size)]
        data1 = array.copy()
        data2 = array.copy()
        draw_data1(data1, ["blue" for _ in range(len(data1))])
        draw_data2(data2, ["blue" for _ in range(len(data2))])
        show_theory(theory_label1, "")
        show_theory(theory_label2, "")

    win = Toplevel(parent)
    win.title("Sorting Algorithm Comparator")
    win.geometry("950x750+200+50")
    win.config(bg="#082A46")

    back_button = Button(
        win, 
        text="← Back", 
        command=win.destroy, 
        bg="#34495E", 
        fg="white", 
        font=("arial", 12, "bold")
    )
    back_button.place(x=20, y=700)

    selected_algorithm1 = StringVar(value="Bubble Sort")
    selected_algorithm2 = StringVar(value="Quick Sort")

    Label(win, text="Algorithm A:", font=("new roman", 14, "italic bold"), bg="#05897A").place(x=20, y=10)
    ttk.Combobox(win, textvariable=selected_algorithm1, state="readonly",
                 values=["Bubble Sort", "Quick Sort", "Selection Sort", "Insertion Sort", "Merge Sort"], font=("arial", 14)).place(x=150, y=10)

    Label(win, text="Algorithm B:", font=("new roman", 14, "italic bold"), bg="#05897A").place(x=500, y=10)
    ttk.Combobox(win, textvariable=selected_algorithm2, state="readonly",
                 values=["Bubble Sort", "Quick Sort", "Selection Sort", "Insertion Sort", "Merge Sort"], font=("arial", 14)).place(x=630, y=10)

    Label(win, text="Speed:", bg="#0E6DA5", font=("new roman", 12, "italic bold")).place(x=20, y=50)
    Scale(win, from_=0.1, to=5.0, resolution=0.1, orient=HORIZONTAL, command=set_speed).place(x=100, y=40)

    Label(win, text="Size:", bg="#0E6DA5", font=("new roman", 12, "italic bold")).place(x=250, y=50)
    sizevalue = Scale(win, from_=5, to=30, orient=HORIZONTAL)
    sizevalue.place(x=320, y=40)

    Label(win, text="Min Val:", bg="#0E6DA5", font=("new roman", 12, "italic bold")).place(x=450, y=50)
    minvalue = Scale(win, from_=0, to=50, orient=HORIZONTAL)
    minvalue.place(x=530, y=40)

    Label(win, text="Max Val:", bg="#0E6DA5", font=("new roman", 12, "italic bold")).place(x=670, y=50)
    maxvalue = Scale(win, from_=50, to=150, orient=HORIZONTAL)
    maxvalue.place(x=760, y=40)

    Button(win, text="Generate", command=generate_data, bg="#28B463", font=("arial", 12)).place(x=300, y=90)
    Button(win, text="Start Comparison", command=StartAlgorithms, bg="#C0392B", font=("arial", 12)).place(x=420, y=90)

    canvas1 = Canvas(win, width=420, height=300, bg="black")
    canvas1.place(x=20, y=140)

    canvas2 = Canvas(win, width=420, height=300, bg="black")
    canvas2.place(x=500, y=140)

    theory_label1 = Text(win, height=6, width=60, font=("arial", 10), wrap=WORD, bg="#F9E79F")
    theory_label1.place(x=20, y=470)
    theory_label1.config(state=DISABLED)

    theory_label2 = Text(win, height=6, width=60, font=("arial", 10), wrap=WORD, bg="#AED6F1")
    theory_label2.place(x=500, y=470)
    theory_label2.config(state=DISABLED)
