import tkinter as tk
from tkinter import messagebox

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        notes_2000 = amount //2000
        remainder =  amount %2000

        notes_500 = remainder //500
        remainder= remainder %500

        notes_100 = remainder //100
        leftover = remainder %100

        lbl_2000.cofing(text=f"2000 Notes: {notes_2000}")
        lbl_500.cofing(text=f"500 Notes: {notes_500}")
        lbl_100.cofing(text=f"100 Notes: {notes_100}")

        if leftover > 0:
            messagebox.showinfo("note", f"remaining ammount that couldent be converted:{leftover}")
    except ValueError:
        messagebox.showerror("Error", "please enter a valid whole number")


root=tk.TK()
root.title("cash Counter")
root.geometry("300x500")

tk.label(root,text="enter amount:, font=("Arial",12)).pack(pady=10)
entry_amount = tk.Entry(root, font=("Arial",12))
entry_amount.pack(pady=5)
btnc_calc = tk.Button(root, text="calculate notes",command= calculate_denominations,bg="green", fg="white")
lbl_200 =tk.Button