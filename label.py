import tkinter

root = tkinter.Tk()

root.title("Label practice!")
root.iconbitmap("icon.ico")
root.geometry("550x550")
root.resizable(0, 0)
root.config(bg="red")

label_1 = tkinter.Label(root, text="よろしく")
label_1.pack()

label_2 = tkinter.Label(root, text="よろしく", font=("Arial", 10, "bold"))
label_2.pack()

label_3 = tkinter.Label(root, text="よろしく", font=("Arial", 10, "bold"), bg="gray")
label_3.pack(padx=10, pady=10)

label_4 = tkinter.Label(root)
label_4.config(text="よろしゅう")
label_4.config(bg="gray")
label_4.pack()

root.mainloop()