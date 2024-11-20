import tkinter

root = tkinter.Tk()
root.title("window practice!")
root.iconbitmap("icon.ico")
root.geometry("300x800")
root.resizable(0, 0)
root.config(bg="red")

sub_window = tkinter.Toplevel()
sub_window.title("second Window")
sub_window.config(bg="#123123")
sub_window.geometry("200x300+500+500")

root.mainloop()
