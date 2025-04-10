import tkinter as tk
from PIL import Image, ImageTk
import visualize

# Function to open visualize window
def open_visualize_window():
    root.withdraw()  # Hide main window
    visualize.open_visualize(root)

# Create main window
root = tk.Tk()
root.title("Data Structure Visualization")
root.geometry("900x550")  # Initial window size
root.configure(bg="white")

# Function to Resize Background Image Dynamically
def resize_bg(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    
    # Resize image to fit new window size
    resized_img = bg_img.resize((new_width, new_height))
    new_bg_image = ImageTk.PhotoImage(resized_img)
    
    # Update background label
    bg_label.config(image=new_bg_image)
    bg_label.image = new_bg_image  # Keep reference

# Load Initial Background Image
try:
    bg_img = Image.open("images/frontpage.png")  # Update path if needed
    bg_img = bg_img.resize((900, 550))  # Resize to fit initial window size
    bg_image = ImageTk.PhotoImage(bg_img)

    # Set Image as Background
    bg_label = tk.Label(root, image=bg_image)
    bg_label.pack(fill="both", expand=True)  # Cover full window
except Exception as e:
    bg_label = tk.Label(root, text="[Image Not Found]", font=("Arial", 12), bg="white")
    bg_label.pack(fill="both", expand=True)

# Bind Window Resize Event to Adjust Background Image
root.bind("<Configure>", resize_bg)

# Transparent Overlay Frame (To Hold Buttons and Title)
overlay_frame = tk.Frame(bg_label, bg="")
overlay_frame.pack(fill="both", expand=True)

# Title Label (Foreground)
title_label = tk.Label(
    overlay_frame, text="Data STRUCTURE VISUALIZATION", 
    font=("Arial", 20, "bold"), bg="yellow", fg="red", padx=15, pady=8
)
title_label.pack(pady=20)

# Bottom Button Frame (For Left & Right Buttons)
button_frame = tk.Frame(overlay_frame, bg="")
button_frame.pack(side="bottom", fill="both", expand=True, pady=40, padx=40)

# Left Button (Bigger size)
btn1 = tk.Button(button_frame, text=" Learn Data Structure and Algorithms", 
                 font=("Arial", 12, "bold"), bg="yellow", fg="black", 
                  bd=3, relief="raised", width=30, height=2)
btn1.pack(side="left", anchor="w", padx=40)

# Right Button (Bigger size)
btn2 = tk.Button(button_frame, text="Visualize Data Structure", 
                 font=("Arial", 12, "bold"), bg="yellow", fg="black", 
                  bd=3, relief="raised", width=30, height=2,command=open_visualize_window)
btn2.pack(side="right", anchor="e", padx=40)

# Run Tkinter event loop
root.mainloop()
