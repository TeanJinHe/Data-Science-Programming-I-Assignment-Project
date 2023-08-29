from tkinter import *
from PIL import ImageTk, Image
import random
import time
import datetime
import tkinter.messagebox as tm


# ==============================Login======================================#
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, font=('arial', 10, 'bold'), text="Username")
        self.label_password = Label(self, font=('arial', 10, 'bold'), text="Password")

        self.entry_username = Entry(self, font=('arial', 8, 'bold'), bd=4, insertwidth=2, justify='right')
        self.entry_password = Entry(self, show="*", font=('arial', 8, 'bold'), bd=4, insertwidth=2, justify='right')

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, font=('arial', 10, 'bold'), text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, padx=1, pady=1, bd=1, fg="black", font=('arial', 16, 'bold'), width=0, text="Login",
                             bg="powder blue", command=self._login_btn_clicked)

        self.logbtn.grid(columnspan=16)

        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "user" and password == "user":
            tm.showinfo("Login info", "Welcome User")

        else:
            tm.showerror("Login error", "Incorrect username")


root= tk()
lf = LoginFrame(root)

root.geometry("1600x8000")
root.resizable(width=True, height=True)
root.title("HP Restaurant")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# ==============================Time======================================#
localtime = time.asctime(time.localtime(time.time()))

titleInfo = Label(Tops, font=('helvetica', 30, 'bold'), text="Harry Potter Restaurant", fg="#FF6F00", bd=10, anchor='w')
titleInfo.grid(row=0, column=0)

timeInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
timeInfo.grid(row=1, column=0)

# ===================================dropdown==============================================#
variable = StringVar(root)
variable.set("Menu")  # default value

w = OptionMenu(root, variable, "Menu", "Price List")
w.pack()

# ===================================declarations==============================================#
rand = StringVar()
pasta = StringVar()
noodles = StringVar()
soup = StringVar()
drinks = StringVar()
burger = StringVar()
subTotal = StringVar()
total = StringVar()
vat = StringVar()
cost = StringVar()


# ===================================functionalities==============================================#
def count():
    x = random.randint(10, 50)
    randomRef = str(x)
    rand.set(randomRef)

    if (pasta.get() == ""):
        pastaCost = 0
    else:
        pastaCost = float(pasta.get())

    if (noodles.get() == ""):
        noodlesCost = 0
    else:
        noodlesCost = float(noodles.get())

    if (soup.get() == ""):
        soupCost = 0
    else:
        soupCost = float(soup.get())

    if (burger.get() == ""):
        burgerCost = 0
    else:
        burgerCost = float(burger.get())

    if (drinks.get() == ""):
        drinksCost = 0
    else:
        drinksCost = float(drinks.get())

    costOfPasta = pastaCost * 350
    costOfDrinks = drinksCost * 25
    costOfNoodles = noodlesCost * 250
    costOfSoup = soupCost * 90
    costOfBurger = burgerCost * 120

    costOfMeal = "Rs", str('%.2f' % (costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger))

    payVat = ((costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger) * 0.15)

    totalCost = (costOfPasta + costOfDrinks + costOfNoodles + costOfSoup + costOfBurger)

    overAllCost = "Rs", str('%.2f' % (payVat + totalCost))

    paidVat = "Rs", str('%.2f' % payVat)

    cost.set(costOfMeal)
    vat.set(paidVat)
    subTotal.set(costOfMeal)
    total.set(overAllCost)

    # bxVat = Entry(f1, font=('arial',16,'bold'),textvariable=cost,bd=10,insertwidth=2,bg="#B9F6CA",justify='right')
    # bxVat.grid(row=2,column=0)

    def show():
        roo = Tk()
        roo.geometry("200x120")
        roo.title("")
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Check Your Bill", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)
        bxVat = Label(roo, font=('aria', 15, 'bold'), textvariable=cost.get(costOfMeal), fg="black", bd=5)
        bxVat.grid(row=2, column=0)
        roo.mainloop()

    show()


def qExit():
    root.destroy()


def reset():
    rand.set("")
    pasta.set("")
    burger.set("")
    noodles.set("")
    drinks.set("")
    soup.set("")
    subTotal.set("")
    vat.set("")
    cost.set("")
    total.set("")


# ===================================Menu List===================================#

pastaLabel = Label(f1, font=('arial', 16, 'bold'), text="Pasta", bd=16, anchor="w")
pastaLabel.grid(row=1, column=0)
bxPasta = Entry(f1, font=('arial', 16, 'bold'), textvariable=pasta, bd=10, insertwidth=4, bg="#B9F6CA", justify='right')
bxPasta.grid(row=1, column=1)

noodlesLabel = Label(f1, font=('arial', 16, 'bold'), text="Chowmein", bd=16, anchor="w")
noodlesLabel.grid(row=2, column=0)
bxNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=noodles, bd=10, insertwidth=4, bg="#B9F6CA",
                  justify='right')
bxNoodles.grid(row=2, column=1)

soupLabel = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
soupLabel.grid(row=3, column=0)
bxSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=soup, bd=10, insertwidth=4, bg="#B9F6CA", justify='right')
bxSoup.grid(row=3, column=1)

burgerLabel = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
burgerLabel.grid(row=4, column=0)
bxBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=burger, bd=10, insertwidth=4, bg="#B9F6CA",
                 justify='right')
bxBurger.grid(row=4, column=1)

drinksLabel = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
drinksLabel.grid(row=5, column=0)
bxDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=drinks, bd=10, insertwidth=4, bg="#B9F6CA",
                 justify='right')
bxDrinks.grid(row=5, column=1)

# ===================================Total Price===================================#


orderLabel = Label(f1, font=('arial', 16, 'bold'), text="Order No", bd=16, anchor="w")
orderLabel.grid(row=1, column=4)
bxOrder = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="#B9F6CA", justify='right')
bxOrder.grid(row=1, column=5)

costLabel = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
costLabel.grid(row=2, column=4)
bxCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg="#B9F6CA", justify='right')
bxCost.grid(row=2, column=5)

vatLabel = Label(f1, font=('arial', 16, 'bold'), text="15% Vat", bd=16, anchor="w")
vatLabel.grid(row=3, column=4)
bxVat = Entry(f1, font=('arial', 16, 'bold'), textvariable=vat, bd=10, insertwidth=4, bg="#B9F6CA", justify='right')
bxVat.grid(row=3, column=5)

subTotalLabel = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
subTotalLabel.grid(row=4, column=4)
bxSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=subTotal, bd=10, insertwidth=4, bg="#B9F6CA",
                   justify='right')
bxSubTotal.grid(row=4, column=5)

totalCostLabel = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
totalCostLabel.grid(row=5, column=4)
bxTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=total, bd=10, insertwidth=4, bg="#B9F6CA",
                    justify='right')
bxTotalCost.grid(row=5, column=5)

# menu#
'''
lblTest= Label(f1, font=('arial', 16, 'bold'),text="burger",bd=16,anchor="w")
lblTest.grid(row=5, column=4)
'''

# ==========================================Buttons================================#
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="#F44336", command=count).grid(row=7, column=2)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="powder blue", command=reset).grid(row=7, column=3)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="#F44336", command=qExit).grid(row=7, column=4)


# ==========================================Menu Price================================#

def price():
    roo = Tk()
    roo.geometry("600x220")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Food Items", fg="steel blue", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="           ", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Price", fg="#F44336", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Baked Pasta", fg="#F44336", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="350 Tk", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chowmein", fg="#F44336", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250 Tk", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Soup", fg="#F44336", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="90 Tk", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger", fg="#F44336", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="120 Tk", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="#F44336", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25 Tk", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)

    roo.mainloop()


igm = PhotoImage(file="C:/Users/user/OneDrive/Desktop/menu.png")
btnprice = Button(root, image=igm, command=price).pack()

# ==========================================Picture================================#
imgpath = "C:/Users/user/Downloads/aa.png"
img = PhotoImage(file=imgpath)
panel = Label(root, image=img)
panel.place(x=476, y=255)

root.mainloop()