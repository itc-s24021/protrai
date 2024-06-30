#s24021


import tkinter as tk

def dispLabel():
    lbl.config(text="こんにちは")

root = tk. Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20))

lbl.pack()
btn.pack()
tk.mainloop()
