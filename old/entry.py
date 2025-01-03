import tkinter
from tkinter.constants import END

def print_text():
    text = tkinter.Label(frame_2, text=entry_1.get())
    text.pack()

    entry_1.delete(0, END)

def count(number):
    global value

    text = tkinter.Label(frame_2, text=number, bg="#499499")
    text.pack()
    value = number + 1

root = tkinter.Tk()
root.title("entry")
root.iconbitmap()
root.geometry("550x550")
root.resizable(0, 0)


frame_1 = tkinter.Frame(root, bg="green", width=500, height=200)
frame_2 = tkinter.Frame(root, bg="pink", width=500, height=300)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0, 10))
frame_2.pack_propagate(0)

entry_1 = tkinter.Entry(frame_1, width=30)
entry_1.grid(row=0, column=0, padx=5, pady=5)
frame_1.grid_propagate(0)

button_1 = tkinter.Button(frame_1, text="出力", command=print_text)
button_1.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

value = 0
button_2 = tkinter.Button(frame_1, text="カウント", command=lambda:count(value))
button_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

root.mainloop()