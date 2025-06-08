
import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Encryption key saved as secret.key")

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        messagebox.showerror("Error", "secret.key file not found. Generate it first.")
        return None

def encrypt_file():
    key = load_key()
    if not key:
        return
    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if not file_path:
        return
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)
    messagebox.showinfo("Success", f"{os.path.basename(file_path)} encrypted.")

def decrypt_file():
    key = load_key()
    if not key:
        return
    file_path = filedialog.askopenfilename(title="Select File to Decrypt")
    if not file_path:
        return
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        decrypted = f.decrypt(data)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        messagebox.showinfo("Success", f"{os.path.basename(file_path)} decrypted.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt file.\n" + str(e))

def run_gui():
    root = Tk()
    root.title("File Encryption Tool")
    root.geometry("300x250")
    Label(root, text="🔐 File Encryption Tool", font=("Arial", 14)).pack(pady=15)
    Button(root, text="Generate Key", command=generate_key, width=25).pack(pady=5)
    Button(root, text="Encrypt File", command=encrypt_file, width=25).pack(pady=5)
    Button(root, text="Decrypt File", command=decrypt_file, width=25).pack(pady=5)
    Button(root, text="Exit", command=root.destroy, width=25).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
