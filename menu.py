import tkinter

root = tkinter.Tk()
root.title("Menu")
root.geometry("260x200")
root.resizable(0, 0)

def open_setting():
    subwindow = tkinter.Toplevel()
    subwindow.title("設定")
    subwindow.geometry("200x100")

    subwindow_label = tkinter.Label(subwindow, text="設定画面です！")
    subwindow_label.pack()

menubar = tkinter.Menu(root)
root.config(menu=menubar)

setting_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="設定", menu=setting_menu)

file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="ファイル", menu=setting_menu)

setting_menu.add_command(label="環境設定", command=open_setting)
setting_menu.add_command(label="終了")

file_menu.add_command(label="新規ファイル")



button_1 = tkinter.Button(root, text="テスト")
button_1.grid(row=0, column=0, padx=100, pady=70, ipadx=10)

root.mainloop()