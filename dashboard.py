from glob import glob
import imghdr
from msilib.schema import Font, Icon
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
from PIL import ImageTk, Image


def create_master():
    screen1 = Toplevel(root)
    screen1.title('CREATE')
    screen1.geometry('500x500')
    Label(screen1, text='List Of Masters', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(screen1, text='Accounting Masters',
          font=('Arial', 11), fg="black").place(x=10, y=50)
    Button(screen1, text='Group', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=70)
    Button(screen1, text='Ledger', command=ledger, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=90)
    Button(screen1, text='Currency', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=110)
    Button(screen1, text='Rate Of Exchange', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=130)
    Button(screen1, text='Voucher Type', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=150)
    Label(screen1, text='Inventory Masters',
          font=('Arial', 11), fg="black").place(x=10, y=180)
    Button(screen1, text='Stock Group', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=200)
    Button(screen1, text='Stock Catagory', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=220)
    Button(screen1, text='Stock Item', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=240)
    Button(screen1, text='Unit', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=260)
    Button(screen1, text='Godown', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=280)
    Label(screen1, text='Statutory Details',
          font=('Arial', 11), fg="black").place(x=10, y=310)
    Button(screen1, text='GST Details', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=360)
    Button(screen1, text='PAN/CIN Details', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=340)
    
def ledger():
    screen2 = Toplevel(root)
    screen2.title('CREATE')
    screen2.geometry('700x500')
    Label(screen2, text='Ledger Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    lname = Label(screen2, text='Name:').place(x=20, y=70)
    ledg_name = StringVar()
    entry1 = Entry(screen2, textvariable='',width=38).place(x=130, y=70)
    under = Label(screen2, text='Under:').place(x=20, y=100)
    ledger_grp = ['Bank Accounts','Bank OCC A/c','Bank OD A/c','Branch/Divisions','Capital Account','Cash-in-Hand','Current Assets','Current Liabilities','Deposits(Asset)','Direct Expenses','Direct Income','Duties & Taxes','Expenses(Direct)','Expenses(Indirect)','Fixed Assets','Income(Direct)','Income(Indirect)','Indirect Expenses','Indirect Incomes','Investments','Loans & Advances(Asset)','Loans(Liability)','Misc Expenses(ASSET)','Provisions','Purchase Account','Reserves & Surplus','Retained Earnings','Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debitors','Suspense A/c','Unsecured Loans']
    cmb = ttk.Combobox(screen2, value=ledger_grp, width=35).place(x=130, y=100)
    type = Label(screen2, text='Type Of Ledger:').place(x=20, y=130)
    ledger_typ = ['Not Applicable','Discount','Invoice Rounding']
    cmb1 = ttk.Combobox(screen2, value=ledger_typ, width=35).place(x=130, y=130)
    st_details = Label(screen2, text='Statutory Details',font=('arial',11)).place(x=20, y=180)
    gst_applcbl = Label(screen2, text='Is GST Applicable:',).place(x=20, y=210)
    gst_combo = ['Applicable', 'Not Applicable', 'Undefined']
    cmb2 = ttk.Combobox(screen2, value=gst_combo, width=35).place(x=135, y=210)
    set = Label(screen2, text='Set/Alter GST Details:').place(x=20, y=240)
    set_combo = ['Yes', 'No']
    cmb3 = ttk.Combobox(screen2, value=set_combo, width=35).place(x=135, y=240)
    
    lname = Label(screen2, text='Name:').place(x=20, y=70)
    supply_typ = Label(screen2, text='Type Of Supply:').place(x=20, y=270)
    supply_combo = ['Goods', 'Services']
    cmb4 = ttk.Combobox(screen2, value=supply_combo, width=35).place(x=135, y=270)
    
    ledger_btn = Button(screen2, text='Submit', width=20, fg="white", font=( "arial", 13),bg='green',activebackground="yellow",command=ledger_submit,relief=GROOVE).place(x=160, y=310)

def ledger_submit():
    pass
root = Tk()
root.geometry("1360x730")
root.resizable(True, True)
root.title("TALLY PRIME")
curnt_period = Label(root, text="CURRENT PERIOD", fg="blue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE", fg="blue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-23", fg="black").place(x=40, y=60)
date = Label(root, text="Friday, 1-Apr-2022", fg="black").place(x=340, y=60)
cmpny = Label(root, text="Name Of Company",
              borderwidth=3, fg="blue").place(x=40, y=100)
lst_entry = Label(root, text="Date Of Last Entry",
                  fg="blue").place(x=340, y=100)
cpny = Label(root, text="ABC Pvt ltd", fg="black").place(x=40, y=140)
date_entry = Label(root, text="1-Apr-22", fg="black").place(x=340, y=140)
separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
frame = Label(root, text="Gateway of Tally", bg="blue", fg="white",
              width=40, padx=20, pady=10).place(x=740, y=65)
frame1 = Frame(root, bg="black", width=305, height=570)
frame1.place(x=740, y=100)
frame2 = Frame(frame1, bg="skyblue", width=305, height=570)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="MASTERS", bg="skyblue",
              fg="black", font="17").place(x=850, y=150)




b1 = Button(root, text="Create", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=create_master).place(x=830, y=180)

b2 = Button(root, text="Alter", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=create_master).place(x=830, y=210)
b3 = Button(root, text="Chart Of Accounts", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=240)
mstrs2 = Label(root, text="Transactions", bg="skyblue",
               fg="black", font="17").place(x=850, y=290)
b5 = Button(root, text="Vouchers", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=320)
b6 = Button(root, text="Day Book", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=350)
mstrs3 = Label(root, text="UTILITIES", bg="skyblue",
               fg="black", font="17").place(x=850, y=390)
b7 = Button(root, text="Banking", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=420)
mstrs4 = Label(root, text="REPORTS", bg="skyblue",
               fg="black", font="17").place(x=850, y=460)
b71 = Button(root, text="BalanceSheet", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1).place(x=830, y=490)
b8 = Button(root, text="Profit & Loss A/c", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=520)
b9 = Button(root, text="Stock Summary", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=550)
b10 = Button(root, text="Ratio Analysis", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1).place(x=830, y=580)

b11 = Button(root, text="Display More Reports", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1).place(x=830, y=620)

frame3 = Frame(root, bg="skyblue", width=130, height=750)
frame3.place(x=1200, y=0)
date = Button(frame3, text="Date", width=20, fg="black", font=(
    "impact", 8), activebackground="yellow", activeforeground="red")
date.place(x=13, y=20)

company = Button(frame3, text="Company", width=20, fg="black", font=(
    "impact", 8),activebackground="yellow", activeforeground="red").place(x=13, y=50)

root.mainloop()
