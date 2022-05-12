from msilib.schema import Font
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
from turtle import width
import mysql.connector
import io
from models import *
import tkcalendar
from tkcalendar import DateEntry

root=Tk()
root.geometry("1360x730")
root.resizable(False, False)

root.title("TALLY PRIME")


curnt_period = Label(root, text="CURRENT PERIOD",fg="blue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="blue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-23", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",borderwidth=3,fg="blue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry", fg="blue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22",fg="black").place(x=340, y=140)
separator = ttk.Separator(root,orient='vertical')
separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
frame = Label(root, text="Gateway of Tally",bg="blue",fg="white",width=40,padx=20,pady=10).place(x=740, y=110)
frame1 = Frame(root, bg="black", width=305, height=540)
frame1.place(x=740, y=145)
frame2 = Frame(frame1, bg="skyblue", width=305, height=540)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Masters",bg="skyblue",fg="black",font="17").place(x=870,y=190)
def func1():
    screen1 = Toplevel(root)
    screen1.title('Create')
    screen1.geometry('500x500')

b1 = Button(root, text="Create", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=230)

b2 = Button(root, text="Alter", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=260)
b3 = Button(root, text="Chart of Accounts", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=290)

mstrs1 = Label(root, text="Transactions",bg="skyblue",fg="black",font="17").place(x=840,y=320)
b5 = Button(root, text="Vouchers", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=360)
b6 = Button(root, text="Day Book", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=390)
mstrs2 = Label(root, text="Utilities",bg="skyblue",fg="black",font="17").place(x=870,y=420)
b7 = Button(root, text="Banking", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=450)

mstrs3 = Label(root, text="Reports",bg="skyblue",fg="black",font="17").place(x=870,y=490)
b8 = Button(root, text="Balance Sheet", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=530)
b9 = Button(root, text="Profit & Loss", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=560)
b10 = Button(root, text="Stock Summary", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=590)

b10 = Button(root, text="Ratio Analysis", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=func1).place(x=830, y=620)
b11 = Button(root, text="Display More Reports", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1, command=func1).place(x=830, y=660)
             
frame3 = Frame(root, bg="skyblue", width=130, height=750)
frame3.place(x=1200, y=0)
date = Button(frame3, text="Date", width=20, fg="black", font=(
    "impact", 8), command=func1, activebackground="yellow", activeforeground="red")
date.place(x=13, y=20)


def func2():
    global screen2
    screen2 = Toplevel(root)
    screen2.resizable(False, False)
    screen2.title('Company')
    screen2.geometry('430x430')
    Label(screen2, text='List Of Companies',bg="blue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(screen2, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=40)
    sbmibtn2 = Button(screen2, text='Alter Company',command=alter,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=70)
    sbmibtn3 = Button(screen2, text='Select Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=create, fg='black',font=('Arial',9),activebackground='yellow', width=30, border=0).place(x=240, y=130)
    my_frame = Frame(screen2)
    my_scrollbar = Scrollbar(my_frame,orient=VERTICAL)
    my_listbox = Listbox(my_frame,yscrollcommand=my_scrollbar.set,width=60)
    my_scrollbar.config(command = my_listbox.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame.place(x=20,y=180)
    my_listbox.pack(pady=10)
    mycursor.execute("select name from company")
    for x in mycursor:
        my_listbox.insert(END,x)

def create():
    global screen3
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('Create Company')
    screen3.geometry('940x670')
    Label(screen3, text='COMPANY CREATION',bg="navyblue",font='17',fg="white",width=640).pack()
    global  Cname,Cmailing,Caddress, mail,statee,countryy,picode,tephone,mophone,faxx,sitee,symboll,formall,e2,e14
    Cname = StringVar()
    Cmailing = StringVar()
    Caddress = StringVar()
    mail = StringVar()
    statee = StringVar()
    countryy = StringVar()
    picode = IntVar()
    tephone = StringVar()
    mophone = StringVar()
    faxx = StringVar()
    sitee = StringVar()
    symboll = StringVar()
    formall = StringVar()
    
    
    cname = Label(screen3, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen3, textvariable=Cname,width=40).place(x=130, y=70)
    y1 = Label(screen3, text='Financial Year begining From:').place(x=450, y=70)
    e2 = DateEntry(screen3,width=25)
    e2.place(x=650, y=70)
    adrs1 = Label(screen3, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen3, textvariable=Cmailing, width=40).place(x=130, y=110)
    y2 = Label(screen3, text='Books Begining From:').place(x=450, y=110)
    e14 = DateEntry(screen3, width=25)
    e14.place(x=650, y=110)
    adrs = Label(screen3, text='Address:').place(x=20, y=150)
    e4 = Entry(screen3,textvariable=Caddress,width=40).place(x=130, y=150)
    state = Label(screen3, text='State:').place(x=20, y=190)
    e5 = Entry(screen3, textvariable=statee, width=40).place(x=130, y=190)
    country = Label(screen3, text='Country:').place(x=20, y=230)
    e6 = Entry(screen3, textvariable= countryy, width=40).place(x=130, y=230)
    pcode = Label(screen3, text='Pincode:').place(x=20, y=270)
    e7 = Entry(screen3, textvariable= picode , width=40).place(x=130, y=270)
    tphone = Label(screen3, text='Telephone:').place(x=20, y=310)
    e8 = Entry(screen3, textvariable=tephone , width=40).place(x=130, y=310)
    mphone = Label(screen3, text='Mobile:').place(x=20, y=350)
    e9 = Entry(screen3, textvariable=mophone, width=40).place(x=130, y=350)
    fax = Label(screen3, text='Fax:').place(x=20, y=390)
    e10 = Entry(screen3, textvariable=faxx, width=40).place(x=130, y=390)
    email = Label(screen3, text='Email:').place(x=20, y=430)
    e10 = Entry(screen3, textvariable=mail, width=40).place(x=130, y=430)
    site = Label(screen3, text='Website:').place(x=20, y=470)
    e11 = Entry(screen3, textvariable=sitee, width=40).place(x=130, y=470)
    symbol = Label(screen3, text='Currency Symbol:').place(x=20, y=510)
    e12 = Entry(screen3, textvariable=symboll, width=40).place(x=130, y=510)
    formal = Label(screen3, text='Formal Name:').place(x=20, y=550)
    e13 = Entry(screen3, textvariable=formall, width=40).place(x=130, y=550)
    btn = Button(screen3, text='Submit', width=20, fg="white", font=( "arial", 13),bg='green',activebackground="yellow",command=submit).place(x=160, y=590)
    

def submit():
    global coname,Fyear,madrs,Byear,adrs,state,country,picode,tno,mno,fax,mail,site,cusymbol,formal
    coname = Cname.get()
    madrs = Cmailing.get()
    adrs = Caddress.get()
    mail = mail.get()
    state = statee.get()
    country = countryy.get()
    picode = picode.get()
    tno = tephone.get()
    mno = mophone.get()
    fax = faxx.get()
    site = sitee.get()
    Fyear = e2.get_date()
    Byear = e14.get_date()
    cusymbol = symboll.get()
    formal = formall.get()
    sql = 'INSERT INTO company(name, mailing_name, address, email, state, country, pincode, telephone, mobile, fax, website, financial_year, year_begin, currencysign, currency) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (coname, madrs, adrs, mail, state, country, picode,
           tno, mno, fax, site, Fyear, Byear, cusymbol, formal)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Company Successfully')

def alter():
    global screen4
    screen3 = Toplevel(root)
    screen3.resizable(False, False)
    screen3.title('Alter Company')
    screen3.geometry('940x670')
    Label(screen3, text='ALTER COMPANY',bg="navyblue",font='17',fg="white",width=640).pack()
    
    
company = Button(frame3, text="Company", width=20, fg="black", font=(
    "impact", 8), command=func2, activebackground="yellow", activeforeground="red").place(x=13, y=50)


root.mainloop()

