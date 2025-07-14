import customtkinter as ctk
import tkinter as tk
import sign_in

def open_login():
    window.destroy()
    sign_in.show_login_screen()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Welcome – Study Hub")
window.geometry("400x600")
window.resizable(False, False)
window.configure(fg_color="#0F2027")

card = ctk.CTkFrame(window, width=320, height=420, corner_radius=20,
                    fg_color="#1e1e1e", border_color="#00ffff", border_width=2)
card.place(relx=0.5, rely=0.5, anchor="center")

ctk.CTkLabel(card, text="WELCOME", font=("Impact", 28), text_color="#FF4444").place(relx=0.5, y=60, anchor="center")
ctk.CTkLabel(card, text="TO", font=("Impact", 26), text_color="#FF4444").place(relx=0.5, y=100, anchor="center")
ctk.CTkLabel(card, text="STUDY HUB", font=("Helvetica", 34, "bold"), text_color="#00FFFF").place(relx=0.5, y=160, anchor="center")
ctk.CTkLabel(card, text="Time to study", font=("Cursive", 18, "italic"), text_color="white").place(relx=0.5, y=210, anchor="center")

ctk.CTkButton(card, text="Start", width=220, height=40, corner_radius=12,
              font=("Arial", 14, "bold"), fg_color="#00ffff", hover_color="#33ffff",
              text_color="black", command=open_login).place(relx=0.5, y=280, anchor="center")

ctk.CTkLabel(card, text="OSSD PROJECT", font=("Arial", 12, "bold"),
             text_color="#888888").place(relx=0.5, y=380, anchor="center")
window.mainloop()