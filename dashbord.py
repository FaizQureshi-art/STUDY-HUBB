import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------- database ----------
def init_db():
    conn = sqlite3.connect("studyhub.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   grade TEXT)""")
    seeds = [("F2023105071","FAIZ QURESHI","A+"),
             ("F2023105125","AYESHA AKHTAR","A"),
             ("F2023105065","HAMZA AZHAR","B")]
    cur.executemany("INSERT OR IGNORE INTO students VALUES (?,?,?)", seeds)
    conn.commit(); conn.close()

def fetch_by_id(sid:str):
    conn = sqlite3.connect("studyhub.db")
    cur = conn.cursor()
    cur.execute("SELECT id,name,grade FROM students WHERE LOWER(id)=?", (sid.lower(),))
    row = cur.fetchone(); conn.close(); return row

# ---------- UI ----------
def show_search_screen():
    init_db()
    history=[]

    def update_display():
        result_var.set("\n".join(history[:10]))
        if history:
            result_lbl.place(relx=0.5,y=300,anchor="center")
            copy_btn.place(relx=0.5,y=440,anchor="center")
        else:
            result_lbl.place_forget(); copy_btn.place_forget()

    def do_search():
        sid=entry.get().strip()
        if not sid:
            messagebox.showinfo("Empty","Enter Student ID"); return
        row=fetch_by_id(sid)
        if row is None:
            messagebox.showwarning("Not Found","Student not found."); return
        rec=f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]}"
        if rec not in history: history.insert(0,rec)
        update_display()

    # -------- window --------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    win=ctk.CTk(); win.geometry("420x560"); win.title("Dashboard – Study Hub")
    win.configure(fg_color="#0F2027")

    card=ctk.CTkFrame(win,width=350,height=520,corner_radius=20,
                      fg_color="#1e1e1e",border_color="#00ffff",border_width=2)
    card.place(relx=0.5,rely=0.5,anchor="center")

    ctk.CTkLabel(card,text="DASHBOARD",font=("Impact",28),
                 text_color="#00FFFF").place(relx=0.5,y=40,anchor="center")

    ctk.CTkLabel(card,text="Search Student by ID",font=("Arial",12),
                 text_color="#ccc").place(relx=0.5,y=80,anchor="center")

    # search bar
    bar=ctk.CTkFrame(card,fg_color="white",corner_radius=30,width=280,height=50)
    bar.place(relx=0.5,y=135,anchor="center"); bar.pack_propagate(False)

    ctk.CTkLabel(bar,text="🔍",text_color="black",font=("Arial",20)
                 ).pack(side="left",padx=8)
    entry=ctk.CTkEntry(bar,placeholder_text="ID",width=170,fg_color="white",
                       text_color="black",border_width=0)
    entry.pack(side="left",pady=5)
    ctk.CTkButton(bar,text="×",width=22,height=22,fg_color="#ff5555",
                  hover_color="#cc0000",corner_radius=10,
                  command=lambda:entry.delete(0,tk.END)
                  ).pack(side="right",padx=5)

    ctk.CTkButton(card,text="Search",width=240,height=40,fg_color="#00ffff",
                  hover_color="#33ffff",text_color="black",
                  command=do_search).place(relx=0.5,y=190,anchor="center")

    # results / history
    result_var=tk.StringVar()
    result_lbl=ctk.CTkLabel(card,textvariable=result_var,font=("Consolas",11),
                            text_color="white",justify="left",width=320)
    copy_btn=ctk.CTkButton(card,text="Copy History",width=180,height=30,
                           fg_color="#222244",hover_color="#4444ff",
                           text_color="white",
                           command=lambda:(win.clipboard_clear(),
                                           win.clipboard_append(result_var.get())))
    # footer
    ctk.CTkLabel(card,text="© Study Hub",font=("Arial",10),
                 text_color="#888").place(relx=0.5,y=490,anchor="center")

    win.mainloop()

# For standalone test
if __name__=="__main__":
    show_search_screen()