import tkinter

root = tkinter.Tk()
root.title("label practice")
root.iconbitmap()
root.geometry("550x550")
root.resizable(0, 0)
root.config(bg="red")

label_1 = tkinter.Label(root, text="よろしく～")
label_1.pack()

label_2 = tkinter.Label(root, text="よろしく～", font=("Arial", 10, "bold"))
label_2.pack()

label_3 = tkinter.Label(root, text="よろしく～", font=("Arial", 10, "bold"), bg="gray", fg="green")
label_3.pack(padx=10, pady=10)

label_4 = tkinter.Label(root)
label_4.config(text="yoroshiku!")
label_4.config(bg="gray")
label_4.pack(padx=10, pady=10, ipadx=50, ipady=20, anchor="e")

label_5 = tkinter.Label(root, text="よろしく～", font=("Arial", 10, "bold"), bg="gray", fg="green")
label_5.pack(padx=10, pady=10, fill="both", expand=True)



root.mainloop()