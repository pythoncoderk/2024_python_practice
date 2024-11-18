import tkinter

root = tkinter.Tk()
root.title("csv格納ツール")
root.geometry("300x800")
root.resizable(0, 0)

sub_window = tkinter.Toplevel()
sub_window.title("second")
sub_window.config(bg="#123123")
sub_window.geometry("200x300+500+500")

root.mainloop()