import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# Function to encrypt the image
def encrypt_image(input_image_path, output_image_path, key):
    try:
        with Image.open(input_image_path) as img:
            img = img.convert('RGB')
            pixels = img.load()  # Load pixel data
            width, height = img.size
            
            # Encrypt by manipulating pixel values
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    encrypted_r = (r + key) % 256
                    encrypted_g = (g + key) % 256
                    encrypted_b = (b + key) % 256
                    pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
            
            img.save(output_image_path)
            messagebox.showinfo("Success", f"Encrypted image saved as {output_image_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to decrypt the image
def decrypt_image(input_image_path, output_image_path, key):
    try:
        with Image.open(input_image_path) as img:
            img = img.convert('RGB')
            pixels = img.load()
            width, height = img.size
            
            # Decrypt by reversing the encryption
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    decrypted_r = (r - key) % 256
                    decrypted_g = (g - key) % 256
                    decrypted_b = (b - key) % 256
                    pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)
            
            img.save(output_image_path)
            messagebox.showinfo("Success", f"Decrypted image saved as {output_image_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to browse and select a file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if filename:
        input_file_var.set(filename)

# Function to encrypt the selected image
def encrypt():
    input_image = input_file_var.get()
    if not input_image:
        messagebox.showerror("Error", "Please select an image file.")
        return

    key = key_var.get()
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid encryption key.")
        return

    output_image = os.path.splitext(input_image)[0] + "_encrypted.png"
    encrypt_image(input_image, output_image, key)

# Function to decrypt the selected image
def decrypt():
    input_image = input_file_var.get()
    if not input_image:
        messagebox.showerror("Error", "Please select an image file.")
        return

    key = key_var.get()
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid decryption key.")
        return

    output_image = os.path.splitext(input_image)[0] + "_decrypted.png"
    decrypt_image(input_image, output_image, key)

# GUI Setup
root = tk.Tk()
root.title("Image Encryption and Decryption")
root.geometry("400x200")

# Input file label and browse button
input_file_var = tk.StringVar()
tk.Label(root, text="Select Image:").pack(pady=10)
tk.Entry(root, textvariable=input_file_var, width=50).pack()
tk.Button(root, text="Browse", command=browse_file).pack()

# Encryption key label and entry
tk.Label(root, text="Enter Key (integer):").pack(pady=10)
key_var = tk.StringVar()
tk.Entry(root, textvariable=key_var, width=20).pack()

# Encrypt and Decrypt buttons
tk.Button(root, text="Encrypt", command=encrypt, bg="lightblue").pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt, bg="lightgreen").pack(pady=5)

# Start the GUI loop
root.mainloop()
