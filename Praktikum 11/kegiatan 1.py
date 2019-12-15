from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

my_app = Tk(className = 'Data diri Mahasiswa')
my_app.geometry('400x200+100+200')

L1 = Label(my_app, text = 'Data diri', font = ('Arial',24))
L1.grid(row=0, column=0)

L2 = Label(my_app, text = 'Nama', font = ('Ariall',14))
L2.grid(row=1, column=0)

str2 = StringVar(value = 'muhammad iqbal')
E2 = Label(my_app, textvariable = str2)
E2.grid(row=1, column=1)

L3 = Label(my_app, text = 'NIM', font = ('Arial',14))
L3.grid(row=2, column=0)

str3 = StringVar(value = 'L200194074')
E3 = Label(my_app, textvariable = str3)
E3.grid(row=2, column=1)

L4 = Label(my_app, text = 'Buku favorit', font = ('Arial',14))
L4.grid(row=3, column=0)

str4 = StringVar(value = 'Buku kosong')
E4 = Label(my_app, textvariable = str4)
E4.grid(row=3, column=1)

L5 = Label(my_app, text = 'Motto', font = ('Arial',14))
L5.grid(row=4, column=0)

str5 = StringVar(value = 'ok')
E5 = Label(my_app, textvariable = str5)
E5.grid(row=4, column=1)

def tutup():
    my_app.destroy()

B1 = Button(my_app.quit(),text = 'close', command = tutup)
B1.grid(row=5, column=1)

my_app.mainloop()

