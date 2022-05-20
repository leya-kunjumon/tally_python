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
    Button(screen1, text='Currency', command=currency_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=110)
    Button(screen1, text='Rate Of Exchange', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=130)
    Button(screen1, text='Voucher Type', command=voucher_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=150)
    Label(screen1, text='Inventory Masters',
          font=('Arial', 11), fg="black").place(x=10, y=180)
    Button(screen1, text='Stock Group', command=stock_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=200)
    Button(screen1, text='Stock Catagory', command=stock_catagory, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=220)
    Button(screen1, text='Stock Item', command=stock_item, fg='black', font=(
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
    entry1 = Entry(screen2, textvariable=ledg_name,
                   width=38).place(x=130, y=70)
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

def currency_creation():
    currncy_scrn = Toplevel(root)
    currncy_scrn .title('CREATE')
    currncy_scrn.geometry('600x450')
    Label(currncy_scrn, text='Currency Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global curncy_symb, curncy_name, curncy_code, decml_plcs, word,deci_plc, entry5, entry6,entry7
    currncy_symcbol = Label(currncy_scrn, text='Currency Symbol:').place(x=20, y=70)
    curncy_symb = StringVar()
    entry1 = Entry(currncy_scrn,textvariable=curncy_symb, width=38)
    entry1.place(x=250, y=70)
    currncy_name = Label(currncy_scrn, text='Currency Name:').place(x=20, y=100)
    curncy_name = StringVar()
    entry2 = Entry(currncy_scrn, textvariable=curncy_name, width=38).place(x=250, y=100)
    currncy_code = Label(currncy_scrn, text='ISO Currency Code:').place(x=20, y=130)
    curncy_code = StringVar()
    entry3 = Entry(currncy_scrn, textvariable=curncy_code, width=38).place(x=250, y=130)
    deci_plces = Label(
        currncy_scrn, text='No Of Decimal Places:').place(x=20, y=160)
    decml_plcs = IntVar()
    entry4 = Entry(currncy_scrn, textvariable=decml_plcs,
                   width=38).place(x=250, y=160)
    show = Label(
        currncy_scrn, text='Show Amount in Millions:').place(x=20, y=190)
    show_plcs = ['Yes', 'No']
    entry5 = ttk.Combobox(currncy_scrn,value=show_plcs,
                   width=35)
    entry5.place(x=250, y=190)
    suffix = Label(
        currncy_scrn, text='Suffix symbol to amount:').place(x=20, y=220)
    suffix_plcs = ['Yes', 'No']
    entry6 = ttk.Combobox(currncy_scrn, value=suffix_plcs,
                   width=35)
    entry6.place(x=250, y=220)
    space = Label( currncy_scrn, text='Add space between amount and symbol:').place(x=20, y=250)
    space_plcs = ['Yes', 'No']
    entry7 = ttk.Combobox(currncy_scrn, value=space_plcs,
                   width=35)
    entry7.place(x=250, y=250)
    word_after = Label( currncy_scrn, text='Word reprenting amount after decimal:').place(x=20, y=280)
    word = StringVar()
    entry8 = Entry(currncy_scrn, textvariable=word,
                   width=38).place(x=250, y=280)
    deci = Label(
        currncy_scrn, text='No of decimal places for amount in words:').place(x=20, y=310)
    deci_plc = IntVar()
    entry9 = Entry(currncy_scrn, textvariable=deci_plc,
                   width=38)
    entry9.place(x=250, y=310)
    crncy_btn = Button(currncy_scrn, text='Submit', width=20, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=crncy_submit, relief=GROOVE).place(x=160, y=360)
        
def crncy_submit():
    currncy_sym = curncy_symb.get()
    formal_name = curncy_name.get()
    code  = curncy_code.get()
    dec_plc = decml_plcs.get()
    show_plc = entry5.get()
    suffx_plc = entry6.get()
    shw_plc = entry7.get()
    word_repsn = word.get()
    deci_plces = deci_plc.get()
    sql = 'INSERT INTO currency(symbol,formal_name,currency_code,decimal_places,amount_in_millions,suffix_symbol,space,word_repsn,decimal_words)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (currncy_sym,formal_name,code,dec_plc,show_plc,suffx_plc,shw_plc,word_repsn,deci_plces)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Currency Successfully')
    
def voucher_creation():
    voucher_scrn = Toplevel(root)
    voucher_scrn .title('CREATE')
    voucher_scrn.geometry('600x490')
    Label(voucher_scrn, text='Voucher Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global vou_name, vou_entry1, vou_abbrvn, vou_entry2, vou_entry3, vou_entry4, vou_entry5,vou_entry6,vou_entry7,vou_entry8,vou_entry9
    voucher_name = Label(voucher_scrn, text='Name:').place(x=20, y=70)
    vou_name = StringVar()
    entry1 = Entry(voucher_scrn, textvariable=vou_name, width=38).place(x=280, y=70)
    voucher_type= Label(voucher_scrn, text='Select Type Of Voucher:').place(x=20, y=100)
    vou_typ = ['Attendance','Contra','Credit Note','Debit Note','Delivery Note','Job Work in Order','Job Work Out Order','Journal','Material In','Material Out','Memorandum','Payment','Payroll','Physical Stock','Purchase Order','Receipt','Receipt Note','Rejections In','Rejections Out','Reversing Journal','Sales','Sales Order','Stock Journal']
    vou_entry1 = ttk.Combobox(voucher_scrn,value=vou_typ,
                   width=35)
    vou_entry1.place(x=280, y=100)
    voucher_abrvtn = Label(
        voucher_scrn, text='Abbreviation:').place(x=20,y=130)
    vou_abbrvn = StringVar()
    entry2 = Entry(voucher_scrn, textvariable=vou_abbrvn,width=38).place(x=280,y=130)
    voucher_actvn = Label(voucher_scrn, text='Activate this Voucher Type:').place(x=20,y=160)
    vou_acvn = ['Yes','No']
    vou_entry2 = ttk.Combobox(voucher_scrn, value=vou_acvn,
                              width=35)
    vou_entry2.place(x=280, y=160)
    voucher_mthod = Label(
        voucher_scrn, text='Method of Voucher Numbering:').place(x=20, y=190)
    vou_method = ['Automatic','Automatic(Manual Override)','Manual','Multi-User Auto','None']
    vou_entry3 = ttk.Combobox(voucher_scrn, value=vou_method,
                              width=35)
    vou_entry3.place(x=280, y=190)
    voucher_date = Label(
        voucher_scrn, text='Use Effective dates for vouchers:').place(x=20, y=220)
    vou_date = ['Yes', 'No']
    vou_entry4 = ttk.Combobox(voucher_scrn, value=vou_date,
                              width=35)
    vou_entry4.place(x=280, y=220)
    voucher_trnscns = Label(voucher_scrn, text='Allow zero-valued transactions:').place(x=20, y=250)
    vou_trns = ['Yes', 'No']
    vou_entry5 = ttk.Combobox(voucher_scrn, value=vou_trns,
                              width=35)
    vou_entry5.place(x=280, y=250)
    voucher_optnl = Label(
        voucher_scrn, text='Make this voucher type as Optional by default:').place(x=20, y=280)
    vou_opn = ['Yes', 'No']
    vou_entry6 = ttk.Combobox(voucher_scrn, value=vou_opn,
                              width=35)
    vou_entry6.place(x=280, y=280)
    voucher_narratn = Label(
        voucher_scrn, text='Allow narration in voucher:').place(x=20, y=310)
    vou_narrtn = ['Yes', 'No']
    vou_entry7 = ttk.Combobox(voucher_scrn, value=vou_narrtn,
                              width=35)
    vou_entry7.place(x=280, y=310)
    voucher_ledger = Label(
        voucher_scrn, text='Provide narrations for each ledger in narrations:').place(x=20, y=340)
    vou_ledger = ['Yes', 'No']
    vou_entry8 = ttk.Combobox(voucher_scrn, value=vou_ledger,
                              width=35)
    vou_entry8.place(x=280, y=340)
    voucher_saving =  Label(
        voucher_scrn, text='Print voucher after saving:').place(x=20, y=370)
    vou_saving = ['Yes', 'No']
    vou_entry9 = ttk.Combobox(voucher_scrn, value=vou_saving,
                              width=35)
    vou_entry9.place(x=280, y=370)
    voucher_btn = Button(voucher_scrn, text='Submit', width=20, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=voucher_submit, relief=GROOVE).place(x=220, y=420)
        
def voucher_submit():
    vouc_namee = vou_name.get()
    vouc_type = vou_entry1.get()
    vouc_abbrvn = vou_abbrvn.get()
    vouc_actvn = vou_entry2.get()
    vouc_method = vou_entry3.get()
    vouc_date = vou_entry4.get()
    vouc_value = vou_entry5.get()
    vouc_typ_optional = vou_entry6.get()
    vouc_narrtn = vou_entry7.get()
    vouc_ledger = vou_entry8.get()
    vouc_save = vou_entry9.get()
    sql = 'INSERT INTO voucher(name,type,abbreviation,voucher_activate,voucher_method,Use_effective_dates,allow_zero_valued,voucher_type_optional,voucher_narration,ledger_narration,voucher_saving)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (vouc_namee, vouc_type, vouc_abbrvn, vouc_actvn,
           vouc_method, vouc_date, vouc_value, vouc_typ_optional, vouc_narrtn, vouc_ledger, vouc_save)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Voucher Successfully')
    
def stock_creation():
    stock_scrn = Toplevel(root)
    stock_scrn .title('CREATE')
    stock_scrn.geometry('500x270')
    Label(stock_scrn, text='Stock Group Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global stock,stockk_under,stock_entry3, stock_entry4
    Stock_name = Label(stock_scrn, text='Name:').place(x=20, y=70)
    stock = StringVar()
    stock_entry1 = Entry(stock_scrn, textvariable=stock, width=38).place(x=260, y=70)
    stock_under = Label(stock_scrn, text='Under:').place(x=20, y=100)
    stockk_under = StringVar()
    stock_entry2 = Entry(stock_scrn, textvariable=stockk_under, width=38).place(x=260, y=100)
    stock_qnty = Label(stock_scrn, text='Should quantities of items be added:').place(x=20, y=130)
    stockk_qnty = ['Yes','No']
    stock_entry3 = ttk.Combobox(stock_scrn, value=stockk_qnty, width=35)
    stock_entry3.place(x=260, y=130)
    stock_gst =  Label(stock_scrn, text='Set/Alter GST details:').place(x=20, y=160)
    stockk_gst = ['Yes','No']
    stock_entry4 = ttk.Combobox(stock_scrn, value=stockk_gst, width=35)
    stock_entry4.place(x=260, y=160)
    stock_btn = Button(stock_scrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=stock_submit, relief=GROOVE).place(x=200, y=220)
def stock_submit():
    stck_name = stock.get()
    stck_under = stockk_under.get()
    stck_qnty = stock_entry3.get()
    stck_details = stock_entry4.get()
    sql = 'INSERT INTO stockGroup(name,stock_under,stock_quantities,stock_details) VALUES(%s,%s,%s,%s)'
    val = (stck_name, stck_under,stck_qnty,stck_details)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Stock Group Successfully Created')

def stock_catagory():
    stock_catagscrn = Toplevel(root)
    stock_catagscrn.title('CREATE')
    stock_catagscrn.geometry('400x270')
    Label(stock_catagscrn , text='Stock Catagory Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global stock_product
    Stock_catgname = Label(stock_catagscrn, text='Name:').place(x=20, y=70)
    stock_product = StringVar()
    stock_entry1 = Entry(stock_catagscrn, textvariable=stock_product,
                         width=38).place(x=100, y=70)
    stock_catagbtn = Button(stock_catagscrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=stock_catagsubmit, relief=GROOVE).place(x=160, y=130)

def stock_catagsubmit():
    stck_catag = stock_product.get()
    sql = 'INSERT INTO stock_Catagory(name) VALUES(%s)'
    val = (stck_catag,)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Stock Catagory Successfully Created')

def stock_item():
    stock_itemscrn = Toplevel(root)
    stock_itemscrn .title('CREATE')
    stock_itemscrn.geometry('500x270')
    Label(stock_itemscrn, text='Stock Item Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global stock_item_name
    Stock_itemname = Label(stock_itemscrn, text='Name:').place(x=20, y=70)
    stock_item_name = StringVar()
    stock_entry1 = Entry(stock_itemscrn, textvariable=stock_product,
                         width=38).place(x=100, y=70)
    
    
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
