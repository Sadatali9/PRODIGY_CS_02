import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def process_image(image_path, key, operation, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        # Process each pixel based on the specified operation (encryption or decryption)
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                if operation == 'encrypt':
                    r, g, b = (r + key) % 256, (g + key) % 256, (b + key) % 256
                elif operation == 'decrypt':
                    r, g, b = (r - key) % 256, (g - key) % 256, (b - key) % 256
                pixels[x, y] = (r, g, b)

        # Save the processed image
        img.save(output_path)
        messagebox.showinfo("Success", f"Image {operation}ed and saved as {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select an Image",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*"))
    )
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, filename)

def perform_operation():
    operation = operation_var.get()
    if operation not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Invalid operation selected.")
        return

    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer.")
        return

    image_path = image_path_entry.get().strip()
    if not image_path:
        #you can set your own path
        image_path = "C:\\Users\\Dell\\Desktop\\Prodigy\\download.jpg"#you can set your default path

    output_path = "encrypted_image.png" if operation == 'encrypt' else "decrypted_image.png"

    process_image(image_path, key, operation, output_path)

# Create the main window
root = tk.Tk()
root.title("Image Encrypter/Decrypter")

# Create and place the widgets
tk.Label(root, text="Operation:").grid(row=0, column=0, padx=10, pady=10)
operation_var = tk.StringVar()
tk.Radiobutton(root, text="Encrypt", variable=operation_var, value='encrypt').grid(row=0, column=1)
tk.Radiobutton(root, text="Decrypt", variable=operation_var, value='decrypt').grid(row=0, column=2)

tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1, columnspan=2)

tk.Label(root, text="Image Path:").grid(row=2, column=0, padx=10, pady=10)
image_path_entry = tk.Entry(root, width=40)
image_path_entry.grid(row=2, column=1, columnspan=2)
tk.Button(root, text="Browse", command=browse_file).grid(row=2, column=3)

tk.Button(root, text="Execute", command=perform_operation).grid(row=3, column=1, columnspan=2, pady=20)

# Start the main loop
root.mainloop()
