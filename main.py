import tkinter
from tkinter import *

root = Tk()
root.geometry("1300x700")
root.title("Welcome to Samsung Specification Unit")

bgf = PhotoImage(file = "bg.png")
background_label = Label(root, image = bgf)
background_label.place(x=0, y = 0, relwidth=1, relheight=1)


Mobile = Label(root,text = "Choose Here",bg = "black",fg="white", font="bold", width=15, height=2, relief=RIDGE,borderwidth=5,)
Mobile.place(relx = 1, x =-200, y = 200, anchor = NE)



def a11():
    global samsungs7
    global s7click
    s7click = True
    samsungs7 = Canvas(root, width=446, height=415,bg='black')
    samsungs7.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung a11.png")
    samsungs7.create_image(0, 50, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/a11.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def a12():
    global samsungs8
    samsungs8 = Canvas(root, width=446, height=415,bg='black')
    samsungs8.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung a12.png")
    samsungs8.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12,bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/a12.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def a21():
    global samsungs9
    samsungs9 = Canvas(root, width=446, height=415,bg='black')
    samsungs9.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung a21.png")
    samsungs9.create_image(80, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/a21.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def a51():
    global samsungs10
    samsungs10 = Canvas(root, width=446, height=415,bg='black')
    samsungs10.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung a51.png")
    samsungs10.create_image(140, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/a51.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()




def S7():
    global samsungs7
    global s7click
    s7click = True
    samsungs7 = Canvas(root, width=446, height=415,bg='black')
    samsungs7.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s7.png")
    samsungs7.create_image(0, 50, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s7.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S8():
    global samsungs8
    samsungs8 = Canvas(root, width=446, height=415,bg='black')
    samsungs8.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s8.png")
    samsungs8.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12,bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s8.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S9():
    global samsungs9
    samsungs9 = Canvas(root, width=446, height=415,bg='black')
    samsungs9.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s9.png")
    samsungs9.create_image(80, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s9.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S10():
    global samsungs10
    samsungs10 = Canvas(root, width=446, height=415,bg='black')
    samsungs10.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s10.png")
    samsungs10.create_image(140, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s10.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S2():
    global samsungs2
    samsungs2 = Canvas(root, width=446, height=415,bg='black')
    samsungs2.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s2.png")
    samsungs2.create_image(80, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s2.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S3():
    global samsungs3
    samsungs3 = Canvas(root, width=446, height=415,bg='black')
    samsungs3.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s3.png")
    samsungs3.create_image(20, 10, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s3.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S4():
    global samsungs4
    samsungs4 = Canvas(root, width=446, height=415,bg='black')
    samsungs4.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s4.png")
    samsungs4.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s4.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S6():
    global samsungs6
    samsungs6 = Canvas(root, width=446, height=415,bg='black')
    samsungs6.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s6.png")
    samsungs6.create_image(80, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s6.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def S20():
    global samsungs20
    samsungs20 = Canvas(root, width=446, height=415,bg='black')
    samsungs20.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s20.png")
    samsungs20.create_image(30, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s20.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def sfold():
    global samsungss
    samsungss = Canvas(root, width=446, height=415,bg='black')
    samsungss.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung sfold.png")
    samsungss.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/sfold.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def s10n():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung s10n.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/s10n.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def m11():
    global samsungss
    samsungss = Canvas(root, width=446, height=415,bg='black')
    samsungss.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung m11.png")
    samsungss.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/m11.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def m31():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung m31.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/m31.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def zfold2():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung zfold2.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/zfold2.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()

def m42():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung m42.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/m42.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()

def f41():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung f41.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/f41.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()

def f12():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung f12.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/f12.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()



def j3pro():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung j3pro.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/j3pro.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()


def j7duo():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung j7duo.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/j7duo.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()

def j7plus():
    global samsungs10n
    samsungs10n = Canvas(root, width=446, height=415,bg='black')
    samsungs10n.grid(row=3, column=3)
    img = PhotoImage(file="mobile_gallery/samsung j7plus.png")
    samsungs10n.create_image(0, 0, anchor=NW, image=img)


    textReceipt = Text( width=46, height=12, bg='black',fg = 'white', bd=5, font=('arial', 16, ))
    textReceipt.grid(row=5, column=3,  padx=10, pady=1,ipadx=40, ipady = 100)
    text_file = open("features/j7plus.txt", 'r')
    stuff = text_file.read()
    textReceipt.insert(END, stuff)
    text_file.close()
    mainloop()




a11 = Button(root,text = "A11",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = a11)
a11.place(relx = 1, x =-340, y = 340, anchor = NE)

a12 = Button(root,text = "A12",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = a12)
a12.place(relx = 1, x =-130, y = 340, anchor = NE)

a21 = Button(root,text = "A21",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = a21)
a21.place(relx = 1, x =-270, y = 340, anchor = NE)

a51 = Button(root,text = "A51",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = a51)
a51.place(relx = 1, x =-200, y = 340, anchor = NE)

s7 = Button(root,text = "S7",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S7)
s7.place(relx = 1, x =-340, y = 400, anchor = NE)


s8 = Button(root,text = "S8",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S8)
s8.place(relx = 1, x =-270, y = 400, anchor = NE)

s9 = Button(root,text = "S9",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S9)
s9.place(relx = 1, x =-200, y = 400, anchor = NE)

s10 = Button(root,text = "S10",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S10)
s10.place(relx = 1, x =-130, y = 400, anchor = NE)


s2 = Button(root,text = "S2",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S2)
s2.place(relx = 1, x =-340, y = 520, anchor = NE)


s3 = Button(root,text = "S3",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S3)
s3.place(relx = 1, x =-270, y = 460, anchor = NE)

s4 = Button(root,text = "S4",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S4)
s4.place(relx = 1, x =-200, y = 460, anchor = NE)

s6 = Button(root,text = "S6",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S6)
s6.place(relx = 1, x =-130, y = 460, anchor = NE)

s20 = Button(root,text = "S20",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = S20)
s20.place(relx = 1, x =-340, y = 460, anchor = NE)

sfold = Button(root,text = "Galaxy Fold",bg = "black",fg="white", font="bold", width=10, height=2, relief=RIDGE,borderwidth=5,command = sfold)
sfold.place(relx = 1, x =-225, y = 520, anchor = NE)

s10n = Button(root,text = "S10 Note",bg = "black",fg="white", font="bold", width=8, height=2, relief=RIDGE,borderwidth=5,command = s10n)
s10n.place(relx = 1, x =-130, y = 520, anchor = NE)

m11 = Button(root,text = "M11",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = m11)
m11.place(relx = 1, x =-270, y = 580, anchor = NE)

m31 = Button(root,text = "S20",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = m31)
m31.place(relx = 1, x =-340, y = 580, anchor = NE)

zfold2= Button(root,text = "Z Fold 2",bg = "black",fg="white", font="bold", width=7, height=2, relief=RIDGE,borderwidth=5,command = zfold2)
zfold2.place(relx = 1, x =-130, y = 580, anchor = NE)

m42 = Button(root,text = "M42",bg = "black",fg="white", font="bold", width=4, height=2, relief=RIDGE,borderwidth=5,command = m42)
m42.place(relx = 1, x =-213, y = 580, anchor = NE)

f41 = Button(root,text = "F41",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = f41)
f41.place(relx = 1, x =-340, y = 640, anchor = NE)

f12 = Button(root,text = "f12",bg = "black",fg="white", font="bold", width=5, height=2, relief=RIDGE,borderwidth=5,command = f12)
f12.place(relx = 1, x =-270, y = 640, anchor = NE)

j3pro = Button(root,text = "J3 Pro",bg = "black",fg="white", font="bold", width=6, height=2, relief=RIDGE,borderwidth=5,command = j3pro)
j3pro.place(relx = 1, x =-195, y = 640, anchor = NE)

j7duo = Button(root,text = "J3 Pro",bg = "black",fg="white", font="bold", width=6, height=2, relief=RIDGE,borderwidth=5,command = j7duo)
j7duo.place(relx = 1, x =-195, y = 640, anchor = NE)

j7plus = Button(root,text = "J3 Pro",bg = "black",fg="white", font="bold", width=6, height=2, relief=RIDGE,borderwidth=5,command = j7plus)
j7plus.place(relx = 1, x =-195, y = 640, anchor = NE)

mainloop()