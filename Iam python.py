Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
w = "こんにちは。" + "私はパイソンです。"
print(w)
こんにちは。私はパイソンです。
len(w)
15
print(w[6:12])
私はパイソン
print(w[-3:])
です。
print(w[8:12])
パイソン
print(w[6:6])

>>> print(w[6:15] + [0:6])
SyntaxError: invalid syntax
>>> print(w[6:15] + w[0:6])
私はパイソンです。こんにちは。
>>> print(w[8:12] + w[9] + w[-9:-11])
パイソンイ
>>> print(w[8:12] + w[7] + w[-9] + w[-10])
パイソンは私。
>>> a = "100"
>>> print(a+23)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a+23)
TypeError: can only concatenate str (not "int") to str
>>> print(int(a) + 23)
123
>>> a = 100
>>> a = "100"
>>> b = "こんにちは"
>>> print(a.isdigit())
True
>>> print(b.isdigit())
False
>>> print("数値じゃないよ")
数値じゃないよ
>>> lunch = ["おにぎり","パスタ","ハンバーガー","カレー","定食"]
>>> print(2)
2
>>> print(lunch[2])
ハンバーガー
