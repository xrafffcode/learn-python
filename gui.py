import tkinter

main_window = tkinter.Tk()

label = tkinter.Label(main_window, text="Program Kasir Toko Gerabah")

e1 = input(str)
e1.pack()
e1.insert("Masukan Nama Pembeli : ")

label.pack()
main_window.mainloop()