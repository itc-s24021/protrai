#s24021
#現在の時刻を表示するアプリを作る

import datetime
import tkinter as tk

def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text=current_time)
    root.after(1000, update_time)
root = tk.Tk()
root.title("現在の時刻")
lbl = tk.Label()
lbl.config(text="test", font=("Helvetica", 20))
lbl.pack()

update_time()

root.mainloop()
