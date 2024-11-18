import tkinter

root = tkinter.Tk()
root.title("Frame")
root.iconbitmap()
root.geometry("550x550")
root.resizable(0, 0)

# tkinter.Label(root, text="test").pack()
# tkinter.Button(root, text="test").grid(row=0, column=0)


frame_1 = tkinter.Frame(root, bg="yellow")
frame_2 = tkinter.Frame(root, bg="green")
frame_3 = tkinter.LabelFrame(root, text="ラベルフレーム", borderwidth=5)

frame_1.pack(fill="both", expand=True)
frame_2.pack(fill="both", expand=True)
frame_3.pack(fill="both", expand=True)

tkinter.Label(frame_1, text="テスト").pack()
tkinter.Label(frame_1, text="テスト").pack()
tkinter.Label(frame_1, text="テスト").pack()

tkinter.Label(frame_2, text="テスト").grid(row=0, column=0)
tkinter.Label(frame_2, text="テスト").grid(row=1, column=1)
tkinter.Label(frame_2, text="テスト").grid(row=2, column=2)
# tkinter.Label(frame_2, text="gggggggggggggggggggggggggggggg").grid(row=3, column=0)

tkinter.Label(frame_3, text="gggggggggggggggggggggggggggggg").grid(row=0, column=0)

root.mainloop()