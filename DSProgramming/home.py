import tkinter as tk
from csv import DictWriter
import os
import time
import pandas as pd
from tkinter import messagebox
from tkinter import *
import csv
from PIL import Image,ImageTk
from tkinter import ttk

   def bill():
        window2=Tk()
        window2.geometry("1000x1000")
        window2.configure(background='#7ea7fe')
        window2.resizable(width=False, height=False)
        window2.title("ELECTRICAL BILLS")


        with open("combine_record.csv", "r", newline="") as passfile:
            reader = csv.reader(passfile)
            data = list(reader)

        entrieslist = []
        for i, row in enumerate(data, start=4):
            entrieslist.append(row[0])
            for col in range(0, 8):
                tk.Label(window2, text=row[col],fg='black',bg='#7ea7fe',height=1,font=("Times New Roman",12)).grid(row=i, column=col)

    billP = Button(Reportwindow, text="All Bills", fg='black',bg='#7ea7fe',width=30,height=1,font=("Times New Roman",12), command=bill).place(x=-15, y=300)
#UNTUK TAMATKAN PENGUNAAN WINDOW
    Statement1 = Button(Reportwindow, text="End Calculated", fg='black',bg='#7ea7fe',width=500, height=1,font=("Times New Roman",12), command=Reportwindow.destroy).pack(side=BOTTOM)

#UNTUKKEMBALI KE MAIN WINDOW
    backtomain_window=Button(Reportwindow, text="Add New Payment", fg='black',bg='#7ea7fe',width=500,height=1,font=("Times New Roman",12), command=Bill_window).pack(side=BOTTOM)

mainwindow= Tk()
mainwindow.title("Electric Bill Management System")
mainwindow.geometry("750x600")
mainwindow.configure(background="#7ea7fe")
greeting=Label(mainwindow,text="Welcome to the Electric Bill Management System!\n"
                                "\nMain Menu\n"
                                "\nPlease click one of the button below:", fg="black", bg="#7ea7fe",
                                font=("Times New Roman",15,"bold"))
greeting.pack()

image=Image.open('C:\\Users\\user\\Downloads\\menu.jpeg')
resize_image=image.resize((150,150))
img=ImageTk.PhotoImage(resize_image)
Label1=ttk.Label(image=img)
Label1.image=img
Label1.place(x=10,y=15)

window4 = Button(mainwindow, text="Cancel", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command=mainwindow.destroy)
window4.pack(side=BOTTOM)
window3 = Button(mainwindow, text="Bill Report", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"),command=Reportwindow)
window3.pack(side=BOTTOM)
window2 = Button(mainwindow, text="Bill", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command=Bill_window)
window2.pack(side=BOTTOM)
window1 = Button(mainwindow, text="User Details", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command= User_window)
window1.pack(side=BOTTOM)

mainwindow.mainloop()