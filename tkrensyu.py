#  GUIで動くアプリを作ってみるよ

import tkinter as tk

root = tk.Tk()
root.geometry("1500x1000")  #　運動のサイズを決める
root.title("ハローアプリ") #　タイトルを決める
lbl = tk.Label(text="こんにちは世界")
lbl.pack()





root.mainloop()
