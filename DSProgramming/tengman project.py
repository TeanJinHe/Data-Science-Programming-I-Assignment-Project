import sqlite3 as sql
from datetime import date

DBName = 'Library Database.db'


def LibraryDBInit():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE USER(
            IC      TEXT NOT NULL PRIMARY KEY,
            Name    TEXT NOT NULL,
            Email   TEXT,
            Privilege TEXT NOT NULL DEFAULT "Normal"
        )""")
    cursor.execute("""
        INSERT INTO USER(IC, Name, Privilege) VALUES ("LIBRARY_IC","LIBRARY", "HIGHEST")
    """)
    cursor.execute("""
        CREATE TABLE BOOK(
            ISBN            TEXT NOT NULL PRIMARY KEY,
            BookName       TEXT,
            BorrowingDate   TEXT,
            IC      TEXT DEFAULT  "LIBRARY_IC",
            Status  TEXT DEFAULT "Normal",
            CONSTRAINT FK_IC FOREIGN KEY(IC) REFERENCES USER(IC)
        )
    """)
    con.commit()
    con.close()


def LibraryAppInit():
    import os
    os.remove('Library Database.db')
    LibraryDBInit()
    AddUser('001103140327', 'Leong Teng Man', 'leongahman@gmail.com')
    AddUser('010815990001', 'Hakurei Reimu', None)
    AddUser('004214111999', 'Ahmad haikal bin syuib', 'Kall34@gmail.com')
    AddUser('010321218999', 'Muhammad Syakur Bin Ali', 'Syah56@gmail.com')
    AddUser('010711454415', 'Yep Lean Wan', 'siozo89@gmail.com')
    AddUser('010321308615', 'M. Umasundari', 'linda.wah@gmail.com')
    AddUser('010607639037', 'Hao Kai Leang ', 'fgee@gmail.com')
    AddUser('002109286007', 'Nurul Izzah Binti Arif', 'izhere67@gmail.com')
    AddUser('002918114919', 'Husna Binti Abdullah', 'Hush2235@gmail.com')
    AddUser('010814062399', 'Aizat Amirul Bin Zakir', 'Aizatte34@gmail.com')
    AddUser('099319044380', 'Aezul Bin Mat Zin', 'Aus695@gmail.com')
    AddUser('010709637876', 'Aiman Nabilah Binti Said', 'Aizatte34@gmail.com')
    AddBook('9781603090254', 'Alec: The Years Have Pants', 'Available')
    AddBook('9781603094955', 'Better Place', 'Available')
    AddBook('1735322342', 'Dont Close Your Eyes', 'Available')
    AddBook('0346148936', 'Complicated Moonlight', 'Available')
    AddBook('1400096898', 'Memoirs of a Geisha', 'Available')
    AddBook('0399155341', 'The Help', 'Available')
    AddBook('0316166685', 'The Lovely Bones', 'Available')
    AddBook('1594633665', 'The Girl on the Train', 'Available')
    AddBook('0063093575', 'The Girl with the Dragon Tattoo', 'Restricted')
    AddBook('0385547129', 'Murder Under Her Skin', 'Available')
    AddBook('1496736249', 'The Spanish Daughter', 'Restricted')
    AddBook('666666666666', 'Tales of The Strongest Cirno', 'Restricted')


def ShowAllTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT 
            name
        FROM 
            sqlite_schema
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%';
        """)
    for i in cursor:
        print(i)
    con.close()


def TestDB():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT 
            sql
        FROM 
            sqlite_schema
        WHERE 
            name LIKE "BOOK";
    """)
    for i in cursor:
        print(i)
    con.close()


def CursorToDict(cursor):
    res = []
    for i in cursor:
        resDict = {}
        FieldName = [elem[0] for elem in cursor.description]
        idx = 0
        for j in i:
            resDict[FieldName[idx]] = j
            idx = idx + 1
        res.append(resDict)
    if len(res) == 0:
        return None
    elif len(res) == 1:
        return res[0]
    else:
        return res


def PrintUserTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT * FROM USER;
    """)
    for i in cursor:
        print(i)
    con.close()


def PrintBookTable():
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        SELECT * FROM BOOK;
    """)
    for i in cursor:
        print(i)
    con.close()


def AddUser(IC, Name, Email, Privilege="Normal"):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO USER(IC, Name, Email, Privilege) VALUES
        (?, ?, ?, ?);
    """, (IC, Name, Email, Privilege))
    con.commit()
    con.close()


def AddBook(ISBN, Name, Status=None):
    con = sql.connect(DBName)
    cursor = con.cursor()
    try:
        if Status is not None:
            cursor.execute("""
                            INSERT INTO BOOK(ISBN, BookName, Status) VALUES
                            (?, ?, ?);
            """, (ISBN, Name, Status))
        else:
            cursor.execute("""
                INSERT INTO BOOK(ISBN, BookName) VALUES
                (?, ?);
            """, (ISBN, Name))
    except:
        return False
    con.commit()
    con.close()


def SearchUser(Name=None, IC=None):
    con = sql.connect(DBName)
    cursor = con.cursor()
    if Name != None:
        cursor.execute(f"""
                    SELECT * FROM USER
                    WHERE Name LIKE \"{Name}\"
                """)
    elif IC != None:
        cursor.execute(f"""
                    SELECT * FROM USER
                    WHERE IC LIKE \"{IC}\"
                """)
    res = CursorToDict(cursor)
    con.close()
    return res


def SearchBook(BookName=None, ISBN=None, ExactMatch=False, LIMIT=5):
    con = sql.connect(DBName)
    cursor = con.cursor()
    if ExactMatch == False:
        if BookName != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE BookName LIKE '%{BookName}%'
                        LIMIT {LIMIT}
                    """)
        elif ISBN != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE ISBN LIKE '%{ISBN}%'
                        LIMIT {LIMIT}
                    """)
    else:
        if BookName != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE BookName LIKE '{BookName}'
                        LIMIT {LIMIT}
                    """)
        elif ISBN != None:
            cursor.execute(f"""
                        SELECT * FROM BOOK
                        WHERE ISBN LIKE '{ISBN}'
                        LIMIT {LIMIT}
                    """)
    res = CursorToDict(cursor)
    con.close()
    return res


def GetBookCurrBorrower(BookName=None, ISBN=None):
    book = SearchBook(BookName, ISBN, ExactMatch=True)
    if book is not None:
        user = SearchUser(IC=book['IC'])
    if user is not None:
        return user['Name']
    return None


def IsBookAvailable(BookName=None, ISBN=None):
    temp = SearchBook(BookName, ISBN, ExactMatch=True)
    if temp is None:
        return False
    return temp['IC'] == "LIBRARY_IC" and temp['Status'] != 'Restricted'


def GetBookStatus(BookName=None, ISBN=None):
    temp = SearchBook(BookName, ISBN, ExactMatch=True)
    if temp is None:
        return "No record"
    elif temp['Status'] == 'Restricted':
        return "Only Internal Reading"
    elif temp['IC'] == "LIBRARY_IC":
        return "Available for borrowing"
    else:
        return "No Available"


def GetUserBorrowedBook(Name=None, IC=None):
    user = SearchUser(Name, IC)
    if not (user == None):
        con = sql.connect(DBName)
        cursor = con.cursor()
        cursor.execute(f"""
            SELECT ISBN, BookName, BorrowingDate FROM BOOK
            WHERE IC like \"{user['IC']}\"
        """)
        res = CursorToDict(cursor)
        con.close()
        return res
    return None


def UpdateData(Table, CurrPK, PKName, NewInstance):
    con = sql.connect(DBName)
    cursor = con.cursor()
    query = f"UPDATE {Table} SET "
    for i in NewInstance:
        query += f"{i} = "
        if isinstance(NewInstance[i], str) == True:
            query += f"\"{NewInstance[i]}\""
        else:
            query += f"{NewInstance[i]}"
        query += ", "
    query = query[:-2:]
    query += f"WHERE {PKName} ="
    if isinstance(NewInstance[PKName], str) == True:
        query += f"\"{CurrPK}\""
    else:
        query += f"{CurrPK}"
    cursor.execute(query)
    con.commit()
    con.close()


def UpdateBook(CurrISBN, NewInstance):
    UpdateData("BOOK", CurrISBN, "ISBN", NewInstance)


def UpdateUser(CurrIC, NewInstance):
    UpdateData("USER", CurrIC, "IC", NewInstance)


def DeleteUser(IC):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute(f"""
            DELETE FROM USER
            WHERE IC=\"{IC}\"
        """)
    con.commit()
    con.close()


def DeleteBook(ISBN):
    con = sql.connect(DBName)
    cursor = con.cursor()
    cursor.execute(f"""
            DELETE FROM BOOK
            WHERE ISBN=\"{ISBN}\"
        """)
    con.commit()
    con.close()


def BorrowBook(ISBN, IC, Date=date.today()):
    con = sql.connect(DBName)
    con.execute("PRAGMA foreign_keys = 1")
    cursor = con.cursor()
    try:
        cursor.execute(f"""
            UPDATE BOOK 
            SET IC = \"{IC}\",
                BorrowingDate = \"{Date}\"
            WHERE ISBN = \"{ISBN}\"
        """)
        con.commit()
        con.close()
        return True
    except sql.IntegrityError:
        return "IC Error"
    except:
        return False


def ReturnBook(ISBN, Date=None):
    return BorrowBook(ISBN, "LIBRARY_IC")

import datetime as datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # to use the combobox

from tkcalendar import Calendar

from Library_App_Engine import *

window = Tk()
window.title("Library Catalogue")
window.geometry(f"{720}x{480}")
window.resizable(1, 1)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
bgPhoto = PhotoImage(file="library.png")
my_label = Label(window, image=bgPhoto)
my_label.place(x=0, y=0)


def ShowFrame(CurrPage, NewPage):
    if CurrPage is not None:
        CurrPage.destroy()
    if callable(NewPage):
        NewPage()


def AutoResizeConfig(frame):
    for col in range(0, frame.grid_size()[0]):
        frame.columnconfigure(col, weight=1)
    for row in range(0, frame.grid_size()[1]):
        frame.columnconfigure(row, weight=1)
    return frame


def MainPage(Criteria='BookName'):
    print("---Book List---")
    PrintBookTable()
    print("---END of Book List---")
    print("---User List---")
    PrintUserTable()
    print("---End of User List---")
    frame = LabelFrame(window, text='WELCOME TO LIBRARY CATALOGUE\n')
    BookChoiceVar = StringVar(value=[])

    def SearchBtCmd(ISBN=None, BookName=None):
        BookRes = SearchBook(ISBN=ISBN, BookName=BookName)
        temp = []
        if type(BookRes) is list:
            for i in BookRes:
                temp.append(i['BookName'])
        elif type(BookRes) is dict:
            temp.append(BookRes['BookName'])
        BookChoiceVar.set(temp)

    SearchBt = Button(frame, text='Search')
    SearchEntry = Entry(frame)
    # Book Info frame
    ISBNVar = StringVar(value="None")
    BookNameVar = StringVar(value="None")
    StatusVar = StringVar(value="None")
    BookInfoFrame = GetBookInfoFrame(frame, ISBNVar, BookNameVar, StatusVar)
    BookLiBox = Listbox(frame, height=5, listvariable=BookChoiceVar)

    def BookLiBoxSel(*args):
        idxs = BookLiBox.curselection()
        if len(idxs) < 1:
            return
        idxs = idxs[0]
        instance = SearchBook(BookName=BookLiBox.get(idxs), ExactMatch=True)
        ISBNVar.set(instance['ISBN'])
        BookNameVar.set(instance['BookName'])
        StatusVar.set(GetBookStatus(ISBN=instance['ISBN']))

    BookLiBox.bind('<<ListboxSelect>>', BookLiBoxSel)
    SearchLbl = Label(frame)
    ChgSearchBt = Button(frame, text='Change Search Criteria')

    if Criteria == 'BookName':
        SearchLbl['text'] = "Enter the Book Name: "
        SearchBt['command'] = lambda *args: SearchBtCmd(BookName=SearchEntry.get())
        ChgSearchBt['command'] = lambda: ShowFrame(frame.destroy(), MainPage('ISBN'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(BookName=SearchEntry.get()))
    else:
        SearchLbl['text'] = "Enter the ISBN: "
        SearchBt['command'] = lambda *args: SearchBtCmd(ISBN=SearchEntry.get())
        ChgSearchBt['command'] = lambda: ShowFrame(frame.destroy(), MainPage('BookName'))
        SearchEntry.bind('<KeyPress>', lambda *args: SearchBtCmd(ISBN=SearchEntry.get()))

    # button frame
    def InstanceCtor():
        return SearchBook(ISBN=ISBNVar.get(), ExactMatch=True)

    EditBtn = Button(frame, text='Edit', command=lambda: ShowFrame(frame.destroy(), EditBookPage(InstanceCtor())))
    ReturnBtn = Button(frame, text='Return', command=lambda: ShowFrame(frame.destroy(), ReturnBookPage(InstanceCtor())))
    BorrowBtn = Button(frame, text='Borrow',
                       command=lambda: ShowFrame(frame.destroy(), BorrowBookPage(ISBNVar.get(), BookNameVar.get())))
    RegisterBtn = Button(frame, text='Register New User', command=lambda: ShowFrame(frame, RegisterUserPage))
    AddBookBtn = Button(frame, text='Add New Book', command=lambda: ShowFrame(frame, AddNewBook))

    # styling
    FontStyle = ("Lato", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    bgColor = "#FFB067"
    frame.config(height=1000, width=1000, bd=10, relief='groove', bg=bgColor, fg="black", font=FontStyle1)
    SearchEntry.config(font=("Lato", 21, "bold"))
    SearchLbl.config(font=FontStyle, bg=bgColor)
    BookLiBox.config(relief='sunken', width=55, font=("Lato", 12))

    # button styling
    BtnBgColor = "#FF8300"
    BtnFontStyle = ("Lato", 16)
    AddBookBtn.config(bg=BtnBgColor, width=20, font=BtnFontStyle)
    RegisterBtn.config(bg=BtnBgColor, width=20, font=BtnFontStyle)
    ChgSearchBt.config(bg=BtnBgColor, width=20, font=BtnFontStyle)
    BorrowBtn.config(bg=BtnBgColor, width=10, font=BtnFontStyle)
    ReturnBtn.config(bg=BtnBgColor, width=10, font=BtnFontStyle)
    EditBtn.config(bg=BtnBgColor, width=10, font=BtnFontStyle)
    SearchBt.config(bg=BtnBgColor, width=10, font=BtnFontStyle)
    BookInfoFrame = AutoResizeConfig(BookInfoFrame)
    for child in BookInfoFrame.winfo_children():
        child.config(font=BtnFontStyle)

    # positioning
    frame.grid()
    SearchLbl.grid(row=0)
    SearchEntry.grid(row=0, column=1, padx=5)
    BookLiBox.grid(row=1)
    BookInfoFrame.grid(row=1, column=1)
    SearchBt.grid(column=1)
    BorrowBtn.grid(column=1)
    EditBtn.grid(column=1)
    ReturnBtn.grid(column=1)
    ReturnBtn.grid(column=1)
    ChgSearchBt.grid(column=0, row=2)
    RegisterBtn.grid(column=0, row=3)
    AddBookBtn.grid(column=0, row=4)
    frame = AutoResizeConfig(frame)


def BorrowBookPage(ISBN=None, BookName=None):
    frame = LabelFrame(window, text='BORROW\n')
    frame.grid()
    BookLabel = Label(frame, text='Book ID: ')
    ISBNLbl = Label(frame, text='Book Name: ')
    BackBtn = Button(frame, text='Back', command=lambda: ShowFrame(frame, MainPage))
    ISBNEntry = Entry(frame)
    BookNameEntry = Entry(frame)
    BorrowerICEntry = Entry(frame)
    BorrowerICEntry.bind('<Return>', lambda *args: Borrow())

    def Borrow():
        msgbx = messagebox.askyesno(message="Confirm?")
        if msgbx == False:
            ShowFrame(frame, MainPage)
        else:
            if (BorrowBook(ISBN=ISBNEntry.get(), IC=BorrowerICEntry.get()) == 'IC Error'):
                msgbx = messagebox.askyesnocancel(
                    message="The IC is not recorded in the system. Enter yes proceed to register or cancel to correct")
                if msgbx is False:
                    ShowFrame(frame, MainPage)
                elif msgbx is True:
                    ShowFrame(frame, RegisterUserPage)
            else:
                ShowFrame(frame, MainPage)

    BorrowBtn = Button(frame, text='Borrow', command=lambda: Borrow())

    if ISBN != None:
        ISBNEntry.insert(0, ISBN)
    if BookName != None:
        BookNameEntry.insert(0, BookName)
    ISBNEntry['state'] = "readonly"
    BookNameEntry['state'] = "readonly"
    ICLbl = Label(frame, text="IC: ")

    # styling
    FontStyle = ("Lato", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "black"
    bgColor = "#FFB067"
    BtnBgColor = "#FF8300"
    frame.config(height=1000, width=1000, bd=10, relief='groove', bg=bgColor, fg=fgColor, font=FontStyle1)
    ICLbl.config(fg=fgColor, bg=bgColor, font=FontStyle)
    BookLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLbl.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNEntry.config(font=FontStyle)
    BookNameEntry.config(fg=fgColor, font=FontStyle)
    BorrowerICEntry.config(font=FontStyle)
    BorrowBtn.config(bg=BtnBgColor, width=10, font=("Lato", 16))
    BackBtn.config(bg=BtnBgColor, width=10, font=("Lato", 16))

    # postioning
    BookLabel.grid(column=0, row=0)
    ISBNLbl.grid(column=0, row=1)
    ISBNEntry.grid(row=0, column=1, padx=5, pady=5)
    BookNameEntry.grid(row=1, column=1, padx=5, pady=5)
    ICLbl.grid(column=0, row=3)
    BorrowerICEntry.grid(column=1, row=3)
    BackBtn.grid(column=0, row=4)
    BorrowBtn.grid(column=1, row=4)

    if ISBN is None or BookName is None or ISBN == "None" or BookName == "None":
        ShowFrame(frame, MainPage)
    elif IsBookAvailable(BookName, ISBN) == False:
        messagebox.showinfo(message="The Book is not available for borrowing")
        ShowFrame(frame, MainPage)
    frame = AutoResizeConfig(frame)


def GetBookInfoFrame(parent, ISBNVar, BookNameVar, StatusVar):
    frame = LabelFrame(parent)
    Label(frame, text="ISBN :").grid(row=0)
    Label(frame, textvariable=ISBNVar).grid(row=0, column=1)
    Label(frame, text="Book Name :").grid(row=1)
    Label(frame, textvariable=BookNameVar).grid(row=1, column=1)
    Label(frame, text="Status :").grid(row=2)
    Label(frame, textvariable=StatusVar).grid(row=2, column=1)
    return frame


def ReturnBookPage(instance=None):
    FontStyle = ("Lato", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "black"
    bgColor = "#FFB067"

    frame = LabelFrame(window, text='RETURN\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    frame.grid()

    BookNameLbl = Label(frame, text='Book Name:', fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLbl = Label(frame, text='ISBN:', fg=fgColor, bg=bgColor, font=FontStyle)
    DateLbl = Label(frame, text=" Return Date :", bg=bgColor, font=FontStyle)
    ISBNSearchLbl = Label(frame, text='ISBN Search: ', fg=fgColor, bg=bgColor, font=FontStyle)
    calendar = Calendar(frame, selectmode='day',
                        year=datetime.date.today().year, month=datetime.date.today().month,
                        day=datetime.date.today().day)
    ISBNVar = StringVar()
    ISBNSearchEntry = Entry(frame, font=("Arial Narrow", 16))

    def ISBNSearch():
        BookRes = SearchBook(ISBN=ISBNSearchEntry.get(), ExactMatch=False)
        if type(BookRes) is list:
            for i in BookRes:
                BookNameLbl['text'] = f"Book Name:\t{i['BookName']}"
                ISBNLbl['text'] = f"Book Name:\t{i['ISBN']}"
                ISBNVar.set(value=i['ISBN'])
                break
        elif type(BookRes) is dict:
            BookNameLbl['text'] = f"Book Name: {BookRes['BookName']}"
            ISBNLbl['text'] = f"Book Name: {BookRes['ISBN']}"
            ISBNVar.set(value=BookRes['ISBN'])

    def Return():
        ISBN = ISBNVar.get()
        if IsBookAvailable(ISBN=ISBN) is True:
            messagebox.showinfo(message="The Book is in the library")
        else:
            BookRes = SearchBook(ISBN=ISBN, ExactMatch=True)
            BorrowingDate = datetime.datetime.strptime(BookRes['BorrowingDate'], '%Y-%m-%d')
            ReturnDate = datetime.datetime.strptime(calendar.get_date(), '%m/%d/%y')
            datediff = ReturnDate - BorrowingDate
            dayUnit = datetime.timedelta(days=1)
            if datediff > dayUnit * 7:
                messagebox.showinfo(message=f"""Overdue and please immediately pay the fine.
                The fine amount: RM0.20*{int(datediff // dayUnit)}days = RM{datediff // dayUnit * 0.2:.2f}
                """)
            ReturnBook(ISBN)
            messagebox.showinfo(message=f"The book have been successfully returned")
            ShowFrame(frame, MainPage)

    ISBNSearchEntry.bind("<KeyPress>", lambda *args: ISBNSearch())
    if type(instance) is dict:
        ISBNVar.set(value=instance['ISBN'])
        BookNameLbl['text'] = f"Book Name: {instance['BookName']}"
        ISBNLbl['text'] = f"ISBN: {instance['ISBN']}"
        ISBNSearchEntry.insert(0, instance['ISBN'])
    frame = AutoResizeConfig(frame)
    BookNameLbl.grid(column=0, row=0)
    ISBNLbl.grid(column=0, row=1)
    ISBNSearchLbl.grid(column=0, row=2)
    ISBNSearchEntry.grid(row=2, column=1)
    DateLbl.grid(row=3, column=0)
    calendar.grid(row=3, column=1)
    Button(frame, text='Back', bg="#FF8300", width=10, font=("Lato", 16),
           command=lambda: ShowFrame(frame, MainPage)).grid(column=0)
    Button(frame, text='Return', bg="#FF8300", width=10, font=("Lato", 16), command=Return).grid(column=1, row=4)


def RegisterUserPage():
    FontStyle = ("Lato", 24)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "black"
    bgColor = "#FFB067"
    frame = LabelFrame(window, text='REGISTRATION',
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    frame.grid()

    def GetEntryInfo():
        IC = ICEntry.get()
        Name = NameEntry.get()
        Email = EmailEntry.get()
        if IC == '' or Name == '':
            return
        if Email == '':
            Email = None
        AddUser(IC, Name, Email)
        ShowFrame(frame, MainPage)

    RegBtn = Button(frame, text='Register', bg=bgColor, command=GetEntryInfo)
    BackBtn = Button(frame, text='Back', command=lambda: ShowFrame(frame, MainPage))

    RegBtn.config(bg="#FF8300", width=10, font=("Lato", 16))
    NameLabel = Label(frame, text="Name :", fg=fgColor, bg=bgColor, font=FontStyle)
    ICLabel = Label(frame, text="IC No. :", fg=fgColor, bg=bgColor, font=FontStyle)
    EmailLabel = Label(frame, text="Email :", fg=fgColor, bg=bgColor, font=FontStyle)
    NameEntry = Entry(frame, font=FontStyle)
    ICEntry = Entry(frame, font=FontStyle)
    EmailEntry = Entry(frame, font=FontStyle)
    BackBtn.config(bg="#FF8300", width=10, font=("Lato", 16))
    frame = AutoResizeConfig(frame)
    # positioning
    NameLabel.grid(row=0, column=0)
    NameEntry.grid(row=0, column=1, padx=50)
    ICLabel.grid(row=1, column=0)
    ICEntry.grid(row=1, column=1, padx=50)
    EmailLabel.grid(row=2, column=0)
    EmailEntry.grid(row=2, column=1)
    RegBtn.grid(row=3, column=1, padx=50)
    BackBtn.grid(row=3, column=0)


# if instance is None, then it is a adding new book page
def AddNewBook(instance=None):
    FontStyle = ("Lato", 21)
    FontStyle1 = ("halvetica", 21, "bold")
    fgColor = "black"
    bgColor = "#FFB067"
    frame = LabelFrame(window, text='ADD NEW BOOK\n', height=1000, width=1000,
                       bd=10, relief='groove',
                       bg=bgColor, fg=fgColor, font=FontStyle1)
    if instance is not None:
        frame['text'] = 'EDIT BOOK'
    frame.grid()
    # initialise widgets
    BookNameLabel = Label(frame, text="Book Name :", font=FontStyle)
    ISBNLabel = Label(frame, text="ISBN:", font=FontStyle)
    BookNameEntry = Entry(frame)
    ISBNEntry = Entry(frame)
    StatusBox = ttk.Combobox(frame, values=('Normal', 'Restricted'), font=("Lato", 14))
    StatusBox.state(["readonly"])
    BackBtn = Button(frame, text='Back', bg="#FF8300", command=lambda: ShowFrame(frame, MainPage))

    def GetEntryInfo():
        ISBN = ISBNEntry.get()
        BookName = BookNameEntry.get()
        Status = StatusBox.get()
        if len(ISBN) < 1 or len(BookName) < 1 or len(Status) < 1:
            return
        if instance is not None:
            UpdateBook(instance['ISBN'], dict(ISBN=ISBN, BookName=BookName, Status=Status))
        elif AddBook(ISBN=ISBN, Name=BookName, Status=Status) == False:
            messagebox.showinfo(message="The Book is already registered in the library")
        ShowFrame(frame, MainPage)

    AddBtn = Button(frame, text='Add', command=GetEntryInfo)
    if instance is not None:
        StatusBox.set(instance['Status'])
        BookNameEntry.insert(0, instance['BookName'])
        ISBNEntry.insert(0, instance['ISBN'])
        AddBtn['text'] = "Edit"

    # styling the widgets
    AddBtn.config(bg="#FF8300", width=10, font=("Lato", 16))
    BackBtn.config(bg="#FF8300", width=10, font=("Lato", 16))
    BookNameLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    ISBNLabel.config(fg=fgColor, bg=bgColor, font=FontStyle)
    BookNameEntry.config(font=FontStyle)
    ISBNEntry.config(font=FontStyle)
    # putting widgets
    BookNameLabel.grid(row=0, column=0, padx=50)
    BookNameEntry.grid(row=0, column=1, padx=50)
    ISBNLabel.grid(row=1, column=0)
    ISBNEntry.grid(row=1, column=1)
    StatusBox.grid(row=2)
    BackBtn.grid(row=3, column=0)
    AddBtn.grid(row=3, column=1)
    frame = AutoResizeConfig(frame)


def EditBookPage(instance=None):
    if instance is None:
        MainPage()
    else:
        AddNewBook(instance)


if __name__ == '__main__':
    LibraryAppInit()
    MainPage()
    window.mainloop()