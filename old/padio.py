import tkinter
from tkinter import IntVar

def print_number():
    if number.get() == 1:
        lavel_number = tkinter.Label(frame_2, text="1が選択されました")
    elif number.get() == 2:
        lavel_number = tkinter.Label(frame_2, text="2が選択されました")
    lavel_number.pack()


root = tkinter.Tk()
root.title("Radio")
root.iconbitmap()
root.geometry("550x550")
root.resizable(0, 0)

frame_1 = tkinter.LabelFrame(root, text="テキスト")
frame_2 = tkinter.Frame(root)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0, 10))

number = IntVar()
number.set(1)

radio_1 = tkinter.Radiobutton(frame_1, text="1を出す", variable=number, value=1)
radio_2 = tkinter.Radiobutton(frame_1, text="2を出す", variable=number, value=2)
radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)

button_1 = tkinter.Button(frame_1, text="出力", command=print_number)
button_1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()