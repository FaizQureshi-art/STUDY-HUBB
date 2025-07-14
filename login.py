import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import search_screen

def init_db():
    conn = sqlite3.connect("studyhub.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 email TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL)""")
    c.execute("INSERT OR IGNORE INTO users VALUES (NULL, 'admin@study.com', '1234')")
    conn.commit()
    conn.close()

def validate_login(email, password):
    conn = sqlite3.connect("studyhub.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def show_login_screen():
    init_db()

    window = ctk.CTk()
    window.title("Login - Study Hub")
    window.geometry("400x600")
    window.configure(fg_color="#1a1a2e")

    ctk.CTkLabel(window, text="Login", font=("Arial", 32, "bold"), text_color="white").pack(pady=40)
    ctk.CTkLabel(window, text="Sign in to continue.", font=("Arial", 12), text_color="white").pack()

    ctk.CTkLabel(window, text="EMAIL", text_color="white").pack(pady=(30, 5))
    email_entry = ctk.CTkEntry(window, width=240)
    email_entry.pack()

    ctk.CTkLabel(window, text="PASSWORD", text_color="white").pack(pady=(20, 5))
    password_entry = ctk.CTkEntry(window, show="*", width=240)
    password_entry.pack()

    def login_action():
        email = email_entry.get()
        password = password_entry.get()
        if validate_login(email, password):
            window.destroy()
            search_screen.show_search_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    ctk.CTkButton(window, text="Login", command=login_action).pack(pady=30)
    window.mainloop()