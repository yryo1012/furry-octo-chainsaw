import tkinter as tk
from tkinter import messagebox

# 閉じるボタンがクリックされたときの処理
def App_Close():
    # 画面を閉じる
    root.quit()

# 表示ボタンがクリックされたときの処理
def On_Click():
    
    # テキストの内容を取得
    msg = txtEntry.get()
    
    # メッセージを表示
    if msg == "":
        messagebox.showerror("サンプル", "何も書かれてません")
    else:
        messagebox.showinfo("サンプル", msg)

def WindowMain():
    global root, txtEntry
    
    # 画面構成
    root = tk.Tk()
    root.title("サンプル")
    root.geometry("300x200")
    
    # Wedgetを設置
    # テキスト
    txtEntry = tk.Entry(root, font=("",10))
    txtEntry.place(x=50, y=20, width=200, height=35)
    # ボタン
    btnHello = tk.Button(root, text="表示", width=10, command=On_Click)
    btnHello.place(x=110, y=70)
    btnClose = tk.Button(root, text="閉じる", width=10, command=App_Close)
    btnClose.place(x=110, y=150)
    
    # 画面に表示
    root.mainloop()

if __name__ == '__main__':
    WindowMain()

