import customtkinter as ctk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# Initialize customtkinter with a specific theme and color mode
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

# Function to generate QR code and display it in a new window
def generate_qr():
    text = input_text.get()
    if not text:
        ctk.CTkMessagebox.show_warning("Input Error", "Please enter some text or a URL")
        return
    
    qr = qrcode.make(text)

    # Open a new window to display the QR code
    qr_window = ctk.CTkToplevel(root)
    qr_window.title("QR Code")

    # Convert QR code to a format suitable for customtkinter
    img = ImageTk.PhotoImage(qr)
    qr_label = ctk.CTkLabel(qr_window, image=img)
    qr_label.image = img  # Keep a reference to prevent garbage collection
    qr_label.pack(pady=10)

    # Save QR code as PNG
    save_button = ctk.CTkButton(qr_window, text="Save QR Code", command=lambda: save_qr(qr))
    save_button.pack(pady=10)

    # Button to go back to the main window
    back_button = ctk.CTkButton(qr_window, text="Back", command=qr_window.destroy)
    back_button.pack(pady=10)

# Function to save the QR code to a PNG file
def save_qr(qr):
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                           filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if filename:
        qr.save(filename)

# Create the main window
root = ctk.CTk()
root.title("QR Code Generator")

# Entry field for input
label = ctk.CTkLabel(root, text="Enter text or URL:")
label.pack(pady=10)

input_text = ctk.CTkEntry(root, width=300)
input_text.pack(pady=10)

# Button to generate QR code
generate_button = ctk.CTkButton(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
