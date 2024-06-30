#24021
#標準入力で受けてた金額を税込み（10%)価格として出力するプログラムを作成してください

import tkinter as tk

def dispLabel():
    a = entry.get()
    print(f"aは{type(a)}")
    lbl.config(text=f"{a}")

root = tk.Tk()
root.title("エントリーヴィジェット")
root.geometry("400x200")
lbl = tk.Label(text="金額を入力", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()
                
tk.mainloop()
