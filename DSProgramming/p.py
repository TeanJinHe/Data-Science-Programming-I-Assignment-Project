import tkinter
import time
from tkinter import *
from PIL import Image,ImageTk

def User_window():
    User_window = Toplevel()
    User_window.geometry("550x500")
    User_window.configure(background='#7ea7fe')
    User_window.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")

    Label_01 = Label(User_window, text="ENTER USER DETAILS\n", fg="yellow", bg="#7ea7fe",font=("Times New Roman", 17, "bold"))
    Label_01.pack()

    # image1 = Image.open('C:\\Users\\kavvi\\Desktop\\png-transparent-computer-icons-user-profile-circle-abstract-miscellaneous-rim-account.png')
    # resize_image = image1.resize((150,150))
    # img = ImageTk.PhotoImage(resize_image)
    # Label1 = tkinter.Label(image=img)
    # Label1.image = img
    # Label1.place(x=200,y=35)

    Label_011 = Label(User_window, text="Name:", fg='black', bg='#7ea7fe', font=("Times New Roman", 12,))
    Label_011.place(x=90,y=200)
    Label_012 = Label(User_window, text="Email:", fg='black', bg='#7ea7fe', font=("Times New Roman", 12,))
    Label_012.place(x=90,y=240)
    Label_013 = Label(User_window, text="IC Number:", fg='black', bg='#7ea7fe', font=("Times New Roman", 12,))
    Label_013.place(x=90,y=280)
    Label_014 = Label(User_window, text="Address:", fg='black', bg='#7ea7fe', font=("Times New Roman", 12,))
    Label_014.place(x=90,y=320)

    Button_01 = Button(User_window, text="Submit", activebackground="pink", activeforeground="red")
    Button_01.place(x=230, y=390)

    Entry_01 = Entry(User_window)
    Entry_01.place(x=200, y=200, width=200, height=20)
    Entry_02 = Entry(User_window)
    Entry_02.place(x=200, y=240, width=200, height=20)
    Entry_03 = Entry(User_window)
    Entry_03.place(x=200, y=280, width=200, height=20)
    Entry_04 = Entry(User_window)
    Entry_04.place(x=200, y=320, width=200, height=50)

    backtomain_window1 = Button(User_window, text="BACK TO MAIN MENU", fg='black', bg='#7ea7fe', width=500, height=1,font=("Times New Roman", 12), command=User_window.destroy)
    backtomain_window1.pack(side=BOTTOM)

def Bill_window():
    Bill_window = Toplevel()
    Bill_window.geometry("850x650")
    Bill_window.configure(background='#7ea7fe')
    Bill_window.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
    Label_02 = Label(Bill_window, text="ELECTRIC BILL", fg='blue', bd=10, bg='#7ea7fe',font=("Times New Roman", 20, "bold"))
    Label_02.pack()

    # ==============================Time======================================#
    localtime = time.asctime(time.localtime(time.time()))
    Label_021 = Label(Bill_window, font=('arial', 15, 'bold'), text=localtime, fg="blue", bg='#7ea7fe', bd=10,anchor='w')
    Label_021.place(x=200, y=50)
    Label_022 = Label(Bill_window, text="----------------------Details---------------------------", fg='blue',bg='#7ea7fe', font=("Times New Roman", 12))
    Label_022.place(x=150, y=100)
    Label_023 = Label(Bill_window, text="--------------------------------------------------------", fg='blue',bg='#7ea7fe', font=("Times New Roman", 12))
    Label_023.place(x=150, y=120)
    Label_024 = Label(Bill_window, text="      Consumption block                   Rate(RM/kWh)", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_024.place(x=150, y=140)
    Label_025 = Label(Bill_window, text="--------------------------------------------------------", fg='blue',bg='#7ea7fe', font=("Times New Roman", 12))
    Label_025.place(x=150, y=160)
    Label_026 = Label(Bill_window, text="     First 200 kWh (1-200 kWh)              0.218", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_026.place(x=150, y=180)
    Label_027 = Label(Bill_window, text="     Next 100 kWh (201-300 kWh)             0.334", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_027.place(x=150, y=200)
    Label_028 = Label(Bill_window, text="     Next 300 kWh (301-600 kWh)             0.516", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_028.place(x=150, y=220)
    Label_029 = Label(Bill_window, text="     Next 300 kWh (601-900 kWh)             0.546", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_029.place(x=150, y=240)
    Label_0201= Label(Bill_window, text="     Next 901 kWh onwards                      0.571", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_0201.place(x=150, y=260)
    Label_0202= Label(Bill_window, text="--------------------------------------------------------", fg='blue',bg='#7ea7fe', font=("Times New Roman", 12))
    Label_0202.place(x=150, y=280)
    Label_0203= Label(Bill_window, text="More than 600 kWh need include service tax 6 percent", fg='blue', bg='#7ea7fe',font=("Times New Roman", 12))
    Label_0203.place(x=100, y=300)
    Label_0204= Label(Bill_window,text="ICPT help to assist the low income and vulnerable customers under this consumption band which is RM0.02per(kWh)",fg='blue', bg='#7ea7fe', font=("Times New Roman", 12))
    Label_0204.place(x=100, y=320)

    rate = StringVar()
    ICPT = StringVar()
    electricprice = StringVar()
    totalprice = StringVar()
    billdate = StringVar()
    servicetax = StringVar()
    electric = StringVar()

    def calculation():
        if (electric.get() == ""):
            electricprice = 0
        else:
            electricprice = float(electric.get())
            if (electricprice <= 200):
                electric_rate = electricprice * 0.218
                electric_ICPT = electricprice * 0.02
                electric_price = (electric_rate - electric_ICPT)
                totalprice.set(electric_price)
            elif (electricprice <= 300):
                electric_rate = (200 * 0.218) + ((electricprice - 200) * 0.334)
                electric_ICPT = electricprice * 0.02
                electric_price = "RM", str('%.2f' % electric_rate)
                totalprice.set(electric_price)
            elif (electricprice <= 600):
                electric_rate = (200 * 0.218) + (100 * 0.334) + ((electricprice - 300) * 0.516)
                electric_ICPT = electricprice * 0.02
                electric_price = "RM", str('%.2f' % (electric_rate - electric_ICPT))
                totalprice.set(electric_price)
            elif (electricprice <= 900):
                electric_rate = (200 * 0.218) + (100 * 0.334) + (300 * 0.516) + ((electricprice - 600) * 0.546)
                electric_ICPT = electricprice * 0.02
                electric_servicetax = (((electricprice - 600) * 0.546) - ((electricprice - 600) * 0.02)) * 0.06
                electric_price = "RM", str('%.2f' % (electric_rate - electric_ICPT + electric_servicetax))
                totalprice.set(electric_price)
            else:
                electric_rate = (200 * 0.218) + (100 * 0.334) + (300 * 0.516) + (300 * 0.546) + (
                            (electricprice - 900) * 0.571)
                electric_ICPT = electricprice * 0.02
                electric_servicetax = ((300 * 0.546) + ((electricprice - 900) * 0.571) - (
                            (electricprice - 600) * 0.02)) * 0.06
                electric_price = "RM", str('%.2f' % (electric_rate - electric_ICPT + electric_servicetax))
                totalprice.set(electric_price)

    Label(Bill_window, text="ENTER YOUR BILL DATE", fg='black', bg='#7ea7fe',font=('Times New Romen', 12, "bold")).place(x=100, y=380)
    billdate = Entry(Bill_window)
    billdate.place(x=480, y=380, width=200, height=20)

    Label(Bill_window, text="ENTER YOUR TOTAL CONSUMPTION (kWh):", fg='black', bg='#7ea7fe',font=('Times New Romen', 12, "bold")).place(x=100, y=420)
    electricbx = Entry(Bill_window, textvariable=electric)
    electricbx.place(x=480, y=420, width=200, height=20)

    Label(Bill_window, text="Total Payment :", fg='black', bg='#7ea7fe', font=('Times New Romen', 12, "bold")).place(x=100, y=460)
    totalpricebx = Entry(Bill_window, textvariable=totalprice)
    totalpricebx.place(x=480, y=460, width=200, height=20)

    calcbtn = Button(Bill_window, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total", bg="#F44336",command=calculation)
    calcbtn.place(x=330, y=500)

    backtomain_window2 = Button(Bill_window, text="BACK TO MAIN MENU", fg='black', bg='#7ea7fe', width=500, height=1,font=("Times New Roman", 12), command=Bill_window.destroy)
    backtomain_window2.pack(side=BOTTOM)

def Reportwindow():
    Reportwindow = Toplevel()
    Reportwindow.geometry("500x400")
    Reportwindow.configure(background='#7ea7fe')
    Reportwindow.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
    greeting = Label(Reportwindow, text="BILL REPORT", fg='blue', bg='#7ea7fe',font=("Times New Roman", 20, "bold"))
    greeting.pack()

    # image2 = Image.open('C:\\Users\\Dell\\Desktop\\STUDENT\\DATA SCIENCE PROGRAMMING I\\GROUP ASSIGMENT\\bill5.jpeg')
    # resize_image = image2.resize((250, 250))
    # img = ImageTk.PhotoImage(resize_image)
    # Label2 = tkinter.Label(image=img)
    # Label2.image = img
    # Label2.place(x=120, y=40)

    def getUser_FullStatement():
        window1 = Tk()
        window1.geometry("500x400")
        window1.configure(background='#7ea7fe')
        window1.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
        Label_03 = Label(window1, text="FULL REPORT", fg='black', bg='#7ea7fe', font=("Times New Roman", 12, "bold"))
        Label_03.pack()

        Label_031 = Label(window1, text="Name           :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_031.place(x=0, y=50)
        Label_032 = Label(window1, text="IC Number      :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_032.place(x=0, y=70)
        Label_033 = Label(window1, text="Phone Number   :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_033.place(x=0, y=90)
        Label_034 = Label(window1, text="Date           :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_034.place(x=0, y=110)

        Label_035 = Label(window1, text="====================================================", fg='black', bg='#7ea7fe',font=("Times New Roman", 12))
        Label_035.place(x=0, y=130)
        Label_036 = Label(window1, text="Summary of Electrical Bills", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold"))
        Label_036.place(x=0, y=150)
        Label_037 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12))
        Label_037.place(x=0, y=170)

        Label_038 = Label(window1, text="Bill", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_038.place(x=0, y=190)
        Label_039 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12))
        Label_039.place(x=0, y=210)
        Label_0301 = Label(window1, text="Address        :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_0301.place(x=0, y=230)
        Label_0302 = Label(window1, text="Payment        :", fg='black', bg='#7ea7fe', font=("Times New Roman", 12))
        Label_0302.place(x=0, y=250)
        Label_0303 = Label(window1, text="----------------------------------------------------", fg='black', bg='#7ea7fe',font=("Times New Roman", 12))
        Label_0303.place(x=0, y=270)

        Label_0304 = Label(window1, text="Total Price    :RM", fg='white', bg='#6495ed',font=("Times New Roman", 12, "bold"))
        Label_0304.place(x=0, y=290)

        Button_03 = Button(window1, text="Back", fg='black', bg='#7ea7fe', width=30, height=1, font=("Times New Roman", 12),command=window1.destroy)
        Button_03 .pack(side=BOTTOM)

    Statement = Button(Reportwindow, text="Full Statement", fg='black', bg='#7ea7fe', width=30, height=1,font=("Times New Roman", 12), command=getUser_FullStatement)
    Statement.place(x=240, y=300)

    def Current_payment():
        window2 = Tk()
        window2.geometry("350x250")
        window2.configure(background='#7ea7fe')
        window2.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
        Label_04 = Label(window2, text="Payment You Sould have Done This Month", fg='black', bg='#7ea7fe',font=("Times New Roman", 12, "bold"))
        Label_04.pack()

        Label_041 = Label(window2, text="RM", fg='white', bg='#6495ed', font=("Times New Roman", 20, "bold"))
        Label_041.place(x=100,y=100)

        Button_04 = Button(window2, text="Back", fg='black', bg='#7ea7fe', width=30, height=1, font=("Times New Roman", 12),command=window2.destroy)
        Button_04.pack(side=BOTTOM)

    CurrentP = Button(Reportwindow, text="Current Payment", fg='black', bg='#7ea7fe', width=30, height=1,font=("Times New Roman", 12), command=Current_payment)
    CurrentP.place(x=-15, y=300)

    Statement1 = Button(Reportwindow,text="End Calculated", fg='black', bg='#7ea7fe', width=500, height=1,font=("Times New Roman", 12), command=Reportwindow.destroy)
    Statement1.pack(side=BOTTOM)

    backtomain_window3 = Button(Reportwindow, text="BACK TO MAIN MENU", fg='black', bg='#7ea7fe', width=500, height=1,font=("Times New Roman", 12), command=Reportwindow.destroy)
    backtomain_window3.pack(side=BOTTOM)


Main_window = Tk()
Main_window.geometry("500x400")
Main_window.configure(background='#7ea7fe')
Main_window.title("ELECTRICAL CALCULATOR TO COMFIRM YOUR BILLS")
greeting1=Label(Main_window,text="Welcome to the Electric Calculator Bill!\n""\nMain Menu\n"
                                 "\nPlease click one of the button below:"
                ,fg="black", bg="#7ea7fe",font=("Times New Roman", 14, "bold"))
greeting1.pack()

# image = Image.open('C:\\Users\\User\\Desktop\\sem 1 20222023\\data science programming 1\\bill1.png')
# resize_image = image.resize((150,150))
# img = ImageTk.PhotoImage(resize_image)
# Label3 = Label(image=img)
# Label3.image = img
# Label3.place(x=10, y=15)

window4 = Button(Main_window, text="Cancel", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command=Main_window.destroy)
window4.pack(side=BOTTOM)
window3 = Button(Main_window, text="Bill Report", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"),command=Reportwindow)
window3.pack(side=BOTTOM)
window2 = Button(Main_window, text="Bill", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command=Bill_window)
window2.pack(side=BOTTOM)
window1 = Button(Main_window, text="User Details", fg='black', bg='#7ea7fe',width=500, height=1,font=("Times New Roman", 12, "bold"), command=User_window)
window1.pack(side=BOTTOM)

Main_window.mainloop()