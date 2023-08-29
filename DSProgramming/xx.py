import tkinter as tk
import pandas as pd
import time
import datetime
from tkinter import *

window=tk.Tk()
window.title("ELECTRIC BILL MANAGEMENT SYSTEM")
window.geometry("1080x720")
window.configure(background='#7ea7fe')

Title = Label(window,text="ELECTRIC BILL",fg='blue',bd=10,bg='#7ea7fe',font=("Times New Roman",20,"bold")).grid(row=0)

# ==============================Time======================================#
localtime = time.asctime(time.localtime(time.time()))
timeInfo = Label(window, font=('arial', 20, 'bold'), text=localtime, fg="blue",bg='#7ea7fe', bd=10, anchor='w')
timeInfo.grid(row=1, column=0)

Label01=Label(window, text="----------------------Details---------------------------",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=2)
Label02=Label(window, text="--------------------------------------------------------",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=3)
Label03=Label(window, text="      Consumption block                   Rate(RM/kWh)",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=4)
Label04=Label(window, text="--------------------------------------------------------",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=5)
Label05=Label(window, text="     First 200 kWh (1-200 kWh)              0.218",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=6)
Label06=Label(window, text="     Next 100 kWh (201-300 kWh)             0.334",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=7)
Label07=Label(window, text="     Next 300 kWh (301-600 kWh)             0.516",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=8)
Label08=Label(window, text="     Next 300 kWh (601-900 kWh)             0.546",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=9)
Label09=Label(window, text="     Next 901 kWh onwards                   0.571",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=10)
Label10=Label(window, text="--------------------------------------------------------",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=11)
Label11=Label(window, text="More than 600 kWh need include service tax 6 percent",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=12)
Label12=Label(window, text="ICPT help to assist the low income and vulnerable customers under this consumption band which is RM0.02per(kWh)",fg='blue',bg='#7ea7fe',font=("Times New Roman",12)).grid(row=13)

rate = StringVar()
ICPT = StringVar()
electricprice = StringVar()
totalprice = StringVar()
billdate = StringVar()
servicetax = StringVar()
electric =StringVar()

def calculation():
    if (electric.get() == ""):
        electricprice = 0
    else:
        electricprice = float(electric.get())
        if(electricprice<=200):
            electric_rate = electricprice * 0.218
            electric_ICPT = electricprice * 0.02
            electric_price = (electric_rate - electric_ICPT)
            totalprice.set(electric_price)
        elif(electricprice<=300):
            electric_rate = (200*0.218)+((electricprice-200)*0.334)
            electric_ICPT = electricprice * 0.02
            electric_price = "RM", str('%.2f' % electric_rate)
            totalprice.set(electric_price)
        elif(electricprice<=600):
            electric_rate=(200*0.218)+(100*0.334)+((electricprice-300)*0.516)
            electric_ICPT=electricprice*0.02
            electric_price = "RM", str('%.2f' % (electric_rate-electric_ICPT))
            totalprice.set(electric_price)
        elif(electricprice<=900):
            electric_rate = (200*0.218)+(100*0.334)+(300*0.516)+((electricprice-600)*0.546)
            electric_ICPT = electricprice*0.02
            electric_servicetax = (((electricprice-600)*0.546)- ((electricprice-600)*0.02))*0.06
            electric_price = "RM", str('%.2f' % (electric_rate-electric_ICPT+electric_servicetax))
            totalprice.set(electric_price)
        else:
            electric_rate=(200*0.218)+(100*0.334)+(300*0.516)+(300*0.546)+((electricprice-900)*0.571)
            electric_ICPT=electricprice*0.02
            electric_servicetax=((300*0.546)+((electricprice-900)*0.571)- ((electricprice-600)*0.02))*0.06
            electric_price = "RM", str('%.2f' % (electric_rate-electric_ICPT+electric_servicetax))
            totalprice.set(electric_price)

Label(window, text="ENTER YOUR BILL DATE",fg='blue',bg='#7ea7fe',width=20, height=6, font=('Times New Romen', 12)).grid(row=14)
billdate = Entry(window)
billdate.grid(row= 14, column=1, sticky=W)

Label(window, text="ENTER YOUR TOTAL CONSUMPTION (kWh):", fg='blue', bg='#7ea7fe', width=50,font=('Times New Romen', 12)).grid(row=15)
electricbx = Entry(window, textvariable=electric)
electricbx.grid(row= 15, column=1, sticky=W)

Label(window, text= "Total Payment :", fg='blue', bg='#7ea7fe', width=20,font=('Times New Romen', 12)).grid(row=16)
totalpricebx = Entry(window, textvariable = totalprice)
totalpricebx.grid(row= 16,column=1, sticky=W)

calcbtn = Button(window, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",bg="#F44336", command=calculation).grid(row=17)
window.mainloop()
# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
#
# #this is the name of my window
# Reportwindow=Tk()
# Reportwindow.geometry("500x400")
# Reportwindow.configure(background='#7ea7fe')
# Reportwindow.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
# greeting=Label(Reportwindow,text="BILL REPORT",fg='blue',bg='#7ea7fe',font=("Times New Roman",20,"bold")).pack()
#
# #UNTUK IMAGE #yg ini kene downlod gambar simpankat mana2file.. pastu tengok ropetic gambar tu coppy locationletakkan kat sini last sekali kene letak nama gamber tu and ,(nama file gambo like .jpeg )
# #image=Image.open('C:\\Users\\Dell\\Desktop\\STUDENT\\DATA SCIENCE PROGRAMMING I\\GROUP ASSIGMENT\\bill5.jpeg')
# # resize_image=image.resize((250,250))
# # img=ImageTk.PhotoImage(resize_image)
# # Label1=tkinter.Label(image=img)
# # Label1.image=img
# # Label1.place(x=120,y=40)
#
# #UNTUK USER PUNYA DATA KESELURUHAN TERMASUK TOTAL PAYMENT
# def getUser_FullStatement(): #full information of user bill
#     window1 = Tk()
#     window1.geometry("500x400")
#     window1.configure(background='#7ea7fe')
#     window1.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
#     Label_01 = Label(window1, text="FULL REPORT", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold")).pack()
#
#     #user information
#     Label_011 = Label(window1, text="Name           :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=50)
#     Label_012 = Label(window1, text="IC Number      :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=70)
#     Label_013 = Label(window1, text="Phone Number   :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=90)
#     Label_014 = Label(window1, text="Date           :", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=110)
#
#     Label_015 = Label(window1, text="====================================================", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=130)
#     Label_016 = Label(window1, text="Summary of Electrical Bills", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold")).place(x=0, y=150)
#     Label_017 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=170)
#
#     Label_018 = Label(window1, text="Bill", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=190)
#     Label_019 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=210)
#     Label_020 = Label(window1, text="Address        :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=230)
#     Label_021 = Label(window1, text="Payment        :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12)).place(x=0, y=250)
#     Label_022 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12)).place(x=0, y=270)
#
#     #Sum all payment
#     Label_023 = Label(window1, text="Total Price    :RM", fg='white', bg='#6495ed', font=("Times New Roman", 12,"bold")).place(x=0, y=290)
#
#     #Button tu Back to back to report bill
#     Button_01 = Button(window1, text="Back", fg='black', bg='#7ea7fe', width=30, height=1, font=("Times New Roman", 12),command=window1.destroy).pack(side=BOTTOM)
#     #https://stackoverflow.com/questions/50474425/python-looping-for-label-variables (example looping lable)
#
# #Button to view te result
# Statement=Button(Reportwindow, text="Full Statement", fg='black',bg='#7ea7fe',width=30,height=1,font=("Times New Roman",12), command=getUser_FullStatement).place(x=240,y=300)
#
#
# #PAYMENT BULAN YG PERLU DIBAYAR TERMASUK DISCOUNT
# def Current_payment(): #ni tinggalkan masukkan bil yg dia kene bayar yng semasa je satu bulan
#     window2=Tk()
#     window2.geometry("350x250")
#     window2.configure(background='#7ea7fe')
#     window2.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
#
#     Label_02=Label(window2,text="Payment You Sould have Done This Month", fg='black', bg='#7ea7fe', font=("Times New Roman", 12, "bold")).pack()
#
#     #this label will show the current payment that user should pay
#     Label_021=Label(window2,text="RM",fg='white', bg='#6495ed', font=("Times New Roman", 20, "bold")).place(x=100, y=100)
#     #print(f'DowndPayment : RM{downpayment}')# label16 = Label(window,text="Your Total Bill is - "+str(total),font="times 18")=example tu popout the current payment
#
#     # Button tu Back to back to report bill
#     Button_02=Button(window2, text="Back", fg='black',bg='#7ea7fe',width=30,height=1,font=("Times New Roman",12), command=window2.destroy).pack(side=BOTTOM)
#
# CurrentP=Button(Reportwindow, text="Current Payment", fg='black',bg='#7ea7fe',width=30,height=1,font=("Times New Roman",12), command=Current_payment).place(x=-15, y=300)
#
# #UNTUK TAMATKAN PENGUNAAN WINDOW
# Statement1 = Button(Reportwindow, text="End Calculated", fg='black',bg='#7ea7fe',width=500, height=1,font=("Times New Roman",12), command=Reportwindow.quit).pack(side=BOTTOM)
#
# #UNTUKKEMBALI KE MAIN WINDOW
# def Back_MainWindow(): #part ni kembali ke main window so command dia kene letak yg farahwahida punya sebab nk back ke sana
#     result = text.get(1.0, END)
#     print(result)
# backtomain_window=Button(Reportwindow, text="Add New Payment", fg='black',bg='#7ea7fe',width=500,height=1,font=("Times New Roman",12), command=Back_MainWindow).pack(side=BOTTOM)
#
# Reportwindow.mainloop()

# from tkinter import *
# from PIL import Image,ImageTk
# from tkinter import ttk
#
# window=Tk()
#
# window.title('ELECTRIC BILL CALCULATOR')
# window.geometry("550x550")
# window.configure(background="#7ea7fe")
# label=Label(
#     text="ENTER USER DETAILS\n", fg="yellow", bg="#7ea7fe",
#             font=("Times New Roman",17,"bold"))
#
# label.pack()
#
# image=Image.open('C:\\Users\\kavvi\\Desktop\\png-transparent-computer-icons-user-profile-circle-abstract-miscellaneous-rim-account.png')
# resize_image=image.resize((150,150))
# img=ImageTk.PhotoImage(resize_image)
# Label1=ttk.Label(image=img)
# Label1.image=img
# Label1.place(x=200,y=35)
#
# name = Label(window, text="Name:", fg="white", bg="black",
#                          font=("Times New Roman",15,)).place(x=90, y=200)
#
# email = Label(window, text="Email:", fg="white", bg="black",
#                          font=("Times New Roman",15,)).place(x=90, y=240)
#
# icnumber = Label(window, text="IC Number:",fg="white", bg="black",
#                          font=("Times New Roman",15,)).place(x=90, y=280)
#
# address = Label(window, text="Address:",fg="white", bg="black",
#                          font=("Times New Roman",15,)).place(x=90, y=320)
#
# sbmitbtn = Button(window, text="Submit", activebackground="pink", activeforeground="red").place(x=230, y=390)
#
# e1 = Entry(window).place(x=200, y=200,width=200,height=20)
#
# e2 = Entry(window).place(x=200, y=240,width=200,height=20)
#
# e3 = Entry(window).place(x=200, y=280,width=200,height=20)
#
# e4 = Entry(window).place(x=200, y=320,width=200,height=50)
#
# def Back_MainWindow():
#     result=text.get(1.0,END)
#     print(result)
#
# def clear_text():
#    text.delete(1.0, END)
#
# text=Text(height=5)
# backtomain_window=Button(window, text="BACK TO MAIN MENU", fg='black',bg='green',width=500,height=1,font=("Times New Roman",12), command=Back_MainWindow).pack(side=BOTTOM)
# btnReset=Button(window,text="CLEAR",fg='black',bg='green',width=500,height=1,font=("Times New Roman",12), command=clear_text).pack(side=BOTTOM)
#
# window.mainloop()

# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk
# mainwindow= Tk()
# mainwindow.title("Electric Bill Calculator")
# mainwindow.geometry("750x250")
# mainwindow.configure(background="#7ea7fe")
# label=Label(
#     text="Welcome to the Electric Calculator Bill!\n"
#          "\nMain Menu\n"
#          "\nPlease click one of the button below:", fg="blue", bg="#7ea7fe",
#             font=("Times New Roman",15,"bold"))
# label.pack()
#
# image=Image.open('C:\\Users\\User\\Desktop\\sem 1 20222023\\data science programming 1\\bill1.png')
# resize_image=image.resize((150,150))
# img=ImageTk.PhotoImage(resize_image)
# Label1=ttk.Label(image=img)
# Label1.image=img
# Label1.place(x=10,y=15)
#
# def open_window1():
#     new1= Toplevel(mainwindow)
#     new1.geometry("750x250")
#     new1.title("Window 1")
#     new1.configure(background="#7ea7fe")
#     Label(new1, text="User Details",)
#
# ttk.Button(mainwindow, text="User Details", command=open_window1,).pack()
#
# def open_window2():
#    new2= Toplevel(mainwindow)
#    new2.geometry("750x250")
#    new2.title("Window 2")
#    new2.configure(background="#7ea7fe")
#    Label(new2, text="Bill",)
#
# ttk.Button(mainwindow, text="Bill", command=open_window2).pack()
#
# def open_window3():
#    new3= Toplevel(mainwindow)
#    new3.geometry("750x250")
#    new3.title("Window 3")
#    new3.configure(background="#7ea7fe")
#    Label(new3, text="Bill Report",)
#
# ttk.Button(mainwindow, text="Bill Report", command=open_window3).pack()
#
# mainwindow.mainloop()