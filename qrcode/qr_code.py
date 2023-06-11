from tkinter import *
import qrcode

tk = Tk()
tk.title("QR CODE")
title = Label(text="QR Code", font="Stencil 20", fg="tan")
title.pack()

link_var = StringVar()
rasm_var = StringVar()

def qr():
	rasm = qrcode.make(link_var.get())
	type(rasm)
	rasm.save(rasm_var.get()+".png")

link = Entry(width="34",textvariable=link_var)
link.place(relx=0.02, rely=0.25)

rasm_nom = Entry(textvariable=rasm_var)
rasm_nom.place(relx=0.4,rely=0.34)

havola_l = Label(text="Enter the link",font="Arial 10")
havola_l.place(relx=0.27,rely=0.19)

qr_button = Button(text="Create a QR code",bg="blue",fg="white",activebackground="aqua",command=qr)
qr_button.place(relx=0.35, rely=0.44)

rasm_l = Label(text="Name the picture: ",font="Arial 8")
rasm_l.place(relx=0.1, rely=0.34)

tk.mainloop()

