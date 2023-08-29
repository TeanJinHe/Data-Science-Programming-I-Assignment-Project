import tkinter as tk
from csv import DictWriter
import os
import time
import pandas as pd
from tkinter import messagebox
from tkinter import *
import csv

User_window=Tk()
User_window.title('USER DETAILS')
User_window.geometry("550x550")
User_window.configure(background="#7ea7fe")
label=Label(text="ENTER USER DETAILS\n", fg="yellow", bg="#7ea7fe",font=("Times New Roman",17,"bold"))
label.pack()

# image=Image.open('C:\\Users\\user\\Downloads\\user.jpeg')
# resize_image=image.resize((150,150))
# img=ImageTk.PhotoImage(resize_image)
# Label1=ttk.Label(User_window,image=img)
# Label1.image=img
# Label1.place(x=200,y=35)

name = Label(User_window, text="Name:", fg="white", bg="black",font=("Times New Roman",15,))
name.place(x=90, y=200)
email = Label(User_window, text="Email:", fg="white", bg="black",font=("Times New Roman",15,))
email.place(x=90, y=240)
icnumber = Label(User_window, text="IC Number:",fg="white", bg="black",font=("Times New Roman",15,))
icnumber.place(x=90, y=280)
address = Label(User_window, text="Address:",fg="white", bg="black",font=("Times New Roman",15,))
address.place(x=90, y=320)

name1 = Entry(User_window)
name1.place(x=200, y=200,width=200,height=20)
email1 = Entry(User_window)
email1.place(x=200, y=240,width=200,height=20)
icnumber1 = Entry(User_window)
icnumber1.place(x=200, y=280,width=200,height=20)
address1 = Entry(User_window)
address1.place(x=200, y=320,width=200,height=50)

def clear_text():
    text.delete(1.0, END)

def submit1():
    namex = name1.get()
    emailx = email1.get()
    icx = icnumber1.get()
    addressx = address1.get()
    with open("user_records.csv", 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['Name', 'Email', 'IC Number','Address'])

        if os.stat("user_records.csv").st_size == 0:  # checks if file contains the header or not
            DictWriter.writeheader(dict_writer)

        dict_writer.writerow({'Name': namex, 'Email': emailx, 'IC Number': icx,'Address': addressx})

        messagebox.showinfo('Message', 'Record added Sucessfully')  # creating message box

        name = name1.delete(0, tk.END)
        email = email1.delete(0,tk.END)
        ic = icnumber1.delete(0, tk.END)
        address = address1.delete(0, tk.END)

sbmitbtn = Button(User_window, text="Submit", activebackground="pink", activeforeground="red",bd=16, fg="black", font=('arial', 16, 'bold'), width=10,bg="#F44336", command=submit1).place(x=230, y=390)

text=Text(height=5)
backtomain_window=Button(User_window, text="BACK TO MAIN MENU", fg='black',bg='green',width=500,height=1,font=("Times New Roman",12), command=User_window.destroy).pack(side=BOTTOM)
btnReset=Button(User_window,text="CLEAR",fg='black',bg='green',width=500,height=1,font=("Times New Roman",12), command=clear_text).pack(side=BOTTOM)


f1 = pd.read_csv("user_records.csv", index_col=0)
f2 = pd.read_csv("bill_records.csv", index_col=0)
combine_record = pd.merge(f1,f2, left_on="Name", right_on="Name", how="left")
combine_record.to_csv("combine_record.csv")
