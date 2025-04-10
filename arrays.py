import tkinter as tk
from PIL import Image, ImageTk

def open_arrays(prev_window):
    """Opens the Arrays visualization window and hides the previous one."""
    
    # Hide previous window if it exists
    if prev_window.winfo_exists():
        prev_window.withdraw()

    print(f"Inside arrays.py: prev_window is {type(prev_window)}")  # Debugging
    print("Opening Arrays Visualization")

    # Create Arrays visualization window
    arr_root = tk.Toplevel()
    arr_root.title("Arrays Visualization")
    arr_root.geometry("900x550")
    arr_root.configure(bg="white")

    # Function to return to previous window
    def back_to_visualize():
        arr_root.destroy()  # Close Arrays window
        if prev_window.winfo_exists():
            prev_window.deiconify()  # Show previous window again


    # Load and Resize Background Image
    try:
        bg_img = Image.open("images/frontpage.png")  # Update path if needed
        bg_img = bg_img.resize((900, 550))  # Resize to fit window
        bg_image = ImageTk.PhotoImage(bg_img)

        # Set Image as Background
        bg_label = tk.Label(arr_root, image=bg_image)
        bg_label.pack(fill="both", expand=True)  # Cover full window
        bg_label.image = bg_image  # Store reference to prevent garbage collection
    except Exception as e:
        bg_label = tk.Label(arr_root, text="[Image Not Found]", font=("Arial", 12), bg="white")
        bg_label.pack(fill="both", expand=True)

    # Overlay Frame
    overlay_frame = tk.Frame(bg_label, bg="")
    overlay_frame.pack(fill="both", expand=True)

    # Title Label
    title_label = tk.Label(
        overlay_frame, text="Arrays Visualization", 
        font=("Arial", 18, "bold"), bg="yellow", fg="red", padx=10, pady=5
    )
    title_label.pack(pady=20)

    # Back Button
    back_btn = tk.Button(overlay_frame, text="Back to Visualize",
                         font=("Arial", 12, "bold"), bg="red", fg="white",
                         padx=20, pady=10, bd=3, relief="raised",
                         command=back_to_visualize)
    back_btn.pack(pady=20)
