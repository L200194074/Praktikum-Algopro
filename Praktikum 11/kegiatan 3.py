from tkinter import (Tk, Label, Entry, Button, StringVar)
from tkinter import (LEFT, RIGHT)

my_app = Tk(className = 'Bangunan Geometri')

L1 = Label(my_app, text = 'Nama Bangunan')
L1.grid(row=0, column=0, sticky='w')

str1 = StringVar(value = 'Prisma Segiempat')
E1 = Label(my_app, textvariable = str1)
E1.grid(row=0, column=2, sticky='w')

L2 = Label(my_app, text = ':')
L2.grid(row=0, column=1)

L3 = Label(my_app, text = 'Dimensi Bangunan')
L3.grid(row=1, column=0, sticky='w')

str3 = StringVar(value = 'Prisma')
E3 = Label(my_app, textvariable = str3)
E3.grid(row=1, column=2, sticky='w')

L4 = Label(my_app, text =':')
L4.grid(row=1, column=1, sticky='w')

L5 = Label(my_app, text = 'contoh benda')
L5.grid(row=2,  cplumn=0, sticky='w')

str5 = StringVar(value = 'Tenda')
E5 = Label(my_app, textvariable = str5)
E5.grid(row=2, column=2, sticky='w')

L6 = Label(my_app, text = ':')
L6.grid(row=2, column=1, sticky='w')

L7 = Label(my_app, text = 'parameter panjang')
L7.grid(row=4, column=0, sticky='w')

str7 = StringVar(value = '0')
E7 = Entry(my_app, textvariable = str7)
E7.grid(row=4, column=2, sticky='w')

L8 = Label(my_app, text = ':')
L8.grid(row=4, column=1, sticky='w')

L9 = Label(my_app, text = 'parameter lebar')
L9.grid(row=5, column=0, sticky='w')

str9 = StringVar(value = '0')
E9 = Entry(my_app, textvariable = str9)
E9.grid(row=5, column=2, sticky='w')

L10 = Label(my_app, text = ':')
L10.grid(row=5, column=1, sticky='w')

L11 = Label(my_app, text = 'parameter tinggi')
L11.grid(row=6, column=0, sticky='w')

str11 = StringVar(value = '0')
E11 = Entry(my_app, textvariable = str11)
E11.grid(row=6, column=2, sticky='w')

L12 = Label(my_app, text = ':')
L12.grid(row=6, column=1, sticky='w')

L13 = Label(my_app, text = 'result')
L13.grid(row=8, column=0, sticky='w')

L14 = Label(my_app, text = '=')
L14.grid(row=8, column=1, sticky='w')

L15 = Label(my_app, text = '')
L15.grid(row=8, column=2, sticky='w')

def hitung():
    a = float(str7.get)
    b = float(str9.get)
    c = float(str11.get)
    result = (a*b*c)
    L15.config(text=result)

B1 = Button(my_app, text+'hitung', command=hitung)
B1.grid(row7, column=0)

my_app.mainloop()
