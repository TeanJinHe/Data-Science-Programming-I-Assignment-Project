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

    Reportwindow=Tk()
    Reportwindow.geometry("500x400")
    Reportwindow.configure(background='#7ea7fe')
    Reportwindow.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
    greeting=Label(Reportwindow,text="BILL REPORT",fg='blue',bg='#7ea7fe',font=("Times New Roman",20,"bold")).pack()

#UNTUK IMAGE #yg ini kene downlod gambar simpankat mana2file.. pastu tengok ropetic gambar tu coppy locationletakkan kat sini last sekali kene letak nama gamber tu and ,(nama file gambo like .jpeg )
    image=Image.open('C:\\Users\\user\\Downloads\\report.jpeg')
    resize_image=image.resize((250,250))
    img=ImageTk.PhotoImage(resize_image)
    Label1=tk.Label(image=img)
    Label1.image = img
    Label1.place(x=120,y=40)


#UNTUK USER PUNYA DATA KESELURUHAN TERMASUK TOTAL PAYMENT
    def getUser_FullStatement(): #full information of user bill
        window1 = Tk()
        window1.geometry("800x400")
        window1.configure(background='#7ea7fe')
        window1.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
        Label_01 = Label(window1, text="FULL REPORT", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold")).pack()

        csv.path = r"combine_record.csv"
        def sumbit2():
            search_name = namebx.get()
            search_month = monthbx.get()
            search_year = yearbx.get()

            icbx.configure(state=tk.NORMAL)
            emailbx.configure(state=tk.NORMAL)
            addressbx.configure(state=tk.NORMAL)
            consumptionbx.configure(state=tk.NORMAL)
            totalbx.configure(state=tk.NORMAL)

            icbx.delete(0, 'end')
            emailbx.delete(0, 'end')
            addressbx.delete(0, 'end')
            consumptionbx.delete(0, 'end')
            totalbx.delete(0, 'end')

            df=pd.read_csv("combine_record.csv")
            row_count = df.shape[0]

            with open("combine_record.csv") as file:
                csv_read = csv.reader(file)
                df= pd.DataFrame([csv_read],index = None)
                n=1
                while n<=row_count:
                    for val in list(df[n]):
                        if str(val[0]) == str(search_name) and str(val[4]) == str(search_month) and str(val[5]) == str(search_year):
                            icbx.insert(0, val[2])
                            emailbx.insert(0, val[1])
                            addressbx.insert(0,val[3])
                            consumptionbx.insert(0, val[6])
                            totalbx.insert(0, val[7])

                            icbx.configure(state=tk.DISABLED)
                            emailbx.configure(state=tk.DISABLED)
                            addressbx.configure(state=tk.DISABLED)
                            consumptionbx.configure(state=tk.DISABLED)
                            totalbx.configure(state=tk.DISABLED)
                        n+=1

    #user information
        Label_011 = Label(window1, text="Name           :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=50)
        Label_012 = Label(window1, text="IC Number      :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=70)
        Label_013 = Label(window1, text="Email          :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=90)
        Label_014 = Label(window1, text="Month,Year     :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=110)

        Label_015 = Label(window1, text="====================================================", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=130)
        Label_016 = Label(window1, text="Summary of Electrical Bills", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold")).place(x=0, y=150)
        Label_017 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=170)

        Label_018 = Label(window1, text="Bill", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=190)
        Label_019 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=210)
        Label_020 = Label(window1, text="Address         :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=230)
        Label_021 = Label(window1, text="Consumption(kWh):", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=250)
        Label_022 = Label(window1, text="Payment         :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=270)
        Label_023 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=290)

        namebx = Entry(window1)
        namebx.place(x=150, y=50)
        icbx = Entry(window1)
        icbx.place(x=150, y=70)
        emailbx = Entry(window1)
        emailbx.place(x=150, y=90)
        monthbx = Entry(window1)
        monthbx.place(x=150, y=110)
        yearbx = Entry(window1)
        yearbx.place(x=250, y=110)
        addressbx = Entry(window1,width=80)
        addressbx.place(x=150, y=230)
        consumptionbx = Entry(window1)
        consumptionbx.place(x=150, y=250)
        totalbx = Entry(window1)
        totalbx.place(x=150, y=270)

    #Button tu Back to back to report bill
        Button_00 = Button(window1, text="Search", fg='black', bg='#7ea7fe', width=30, height=1, font=("Times New Roman", 12),command=sumbit2).pack(side=BOTTOM)
        Button_01 = Button(window1, text="Back", fg='black', bg='#7ea7fe', width=30, height=1, font=("Times New Roman", 12),command=window1.destroy).pack(side=BOTTOM)
    #https://stackoverflow.com/questions/50474425/python-looping-for-label-variables (example looping lable)

#Button to view te result
    Statement=Button(Reportwindow, text="Full Statement", fg='black',bg='#7ea7fe',width=30,height=1,font=("Times New Roman",12), command=getUser_FullStatement).place(x=240,y=300)


#PAYMENT BULAN YG PERLU DIBAYAR TERMASUK DISCOUNT
    def bill(): #ni tinggalkan masukkan bil yg dia kene bayar yng semasa je satu bulan
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
