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
    Button(screen1, text='Change Company', command=change_company, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=308, y=50)
    Button(screen1, text='Group', command=group, fg='black', font=(
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
    Button(screen1, text='Unit', command=unit, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=260)
    Button(screen1, text='Godown', command=godown, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=280)
    Label(screen1, text='Statutory Details',
          font=('Arial', 11), fg="black").place(x=10, y=310)
    Button(screen1, text='GST Details', command=gst_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=340)
    Button(screen1, text='PAN/CIN Details', command=Pan_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=360)
        
def change_company():
    changescrn = Toplevel(root)
    changescrn.title('CREATE')
    changescrn.geometry('380x300')
    Label(changescrn, text='Change Company', bg="blue",
          font='17', fg="white", width=430).pack()
    global comcmb
    comname = Label(changescrn, text='Name:').place(x=20, y=70)
    sql = "SELECT name FROM company"
    mycursor.execute(sql,)
    change_cpny = mycursor.fetchall()
    chng_cmpny = []
    for i in change_cpny:
        chng_cmpny.append(i[0])
    comcmb = ttk.Combobox(changescrn, width=35)
    comcmb.place(x=130, y=70)
    comcmb['values'] = chng_cmpny
    chng_btn = Button(changescrn, text='Submit', width=17, fg="white", font=( "arial", 13),bg='green',activebackground="yellow",command=grp_submit,relief=GROOVE).place(x=140, y=120)

def group():
    grpscrn = Toplevel(root)
    grpscrn.title('CREATE')
    grpscrn.geometry('600x500')
    Label(grpscrn, text='Group Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global grpname, grpcmb, grpcmb1, grpcmb2, grpcmb3,grpcmb4
    gname = Label(grpscrn, text='Name:').place(x=20, y=70)
    grpname = StringVar()
    grpentry1 = Entry(grpscrn, textvariable=grpname,
                   width=38).place(x=250, y=70)
    gunder = Label(grpscrn, text='Under:').place(x=20, y=100)
    grp_under = ['Bank Accounts','Bank OCC A/c','Bank OD A/c','Branch/Divisions','Capital Account','Cash-in-Hand','Current Assets','Current Liabilities','Deposits(Asset)','Direct Expenses','Direct Income','Duties & Taxes','Expenses(Direct)','Expenses(Indirect)','Fixed Assets','Income(Direct)','Income(Indirect)','Indirect Expenses','Indirect Incomes','Investments','Loans & Advances(Asset)','Loans(Liability)','Misc Expenses(ASSET)','Provisions','Purchase Account','Reserves & Surplus','Retained Earnings','Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debitors','Suspense A/c','Unsecured Loans']
    grpcmb = ttk.Combobox(grpscrn, value=grp_under, width=35)
    grpcmb.place(x=250, y=100)
    grpledg = Label(grpscrn, text='Group behaves like a ledger:').place(x=20, y=130)
    grp_ledg = ['Yes','No']
    grpcmb1 = ttk.Combobox(grpscrn, value=grp_ledg, width=35)
    grpcmb1.place(x=250, y=130)
    grpnet = Label(grpscrn, text='Net Debit/Credit Balances for reporting:').place(x=20, y=160)
    grp_nett = ['Yes','No']
    grpcmb2 = ttk.Combobox(grpscrn, value=grp_nett, width=35)
    grpcmb2.place(x=250, y=160)
    grpcalc = Label(grpscrn, text='Used for Calculation:').place(x=20, y=190)
    grp_calcu = ['Yes','No']
    grpcmb3 = ttk.Combobox(grpscrn, value=grp_calcu, width=35)
    grpcmb3.place(x=250, y=190)
    grpmthd = Label(grpscrn, text='Method to allocate when used in purchase \ninvoice:').place(x=20, y=220)
    grp_method = ['Applicable','Not Applicable']
    grpcmb4 = ttk.Combobox(grpscrn, value=grp_method, width=35)
    grpcmb4.place(x=250, y=220)
    grp_btn = Button(grpscrn, text='Submit', width=20, fg="white", font=( "arial", 13),bg='green',activebackground="yellow",command=grp_submit,relief=GROOVE).place(x=160, y=260)
    
def grp_submit():
    grp_name = grpname.get()
    grp_under = grpcmb.get()
    grp_ledger = grpcmb1.get()
    grp_blnce = grpcmb2.get()
    grp_calcn = grpcmb3.get()
    grp_method = grpcmb4.get()
    sql = 'INSERT INTO mastergroup(name,grp_under,grp_ledger,balance_reporting ,calculn_used,method)  VALUES(%s,%s,%s,%s,%s,%s)'
    val = (grp_name,grp_under,grp_ledger,grp_blnce,grp_calcn,grp_method)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Group Successfully')
    
def gstfun(event):
    ledg_cmb3 = cmb3.get()
    if ledg_cmb3 == 'Yes':
        gstscreen = Toplevel()
        gstscreen.title('CREATE')
        gstscreen.geometry('500x450')
        Label(gstscreen, text='GST details for Ledger',
          font='17', fg="black", width=430).pack()
        gstvar = Label(gstscreen, text='',
          font='17', fg="black", width=430)
        gstvar.pack()
        gstvar.config(text=ledg_name.get())
        global gcmb1, gcmb2,intx,ctx
        gstnme  = Label(gstscreen, text='Nature of Transaction:').place(x=20, y=70)
        gcmb1 = ttk.Combobox(gstscreen, width=35)
        gcmb1.place(x=210,y=70)
        gcmb1['values'] = ['Not Applicable','Branch Transfer Inward','Imports Exempt','Imports Nil rated','Imports Taxable','Interstate Purchase Exempt','Interstate Purchase from Unregisterd Dealer-Exempt','Interstate Purchase from Unregisterd Dealer-Nil Rated','Interstate Purchase from Unregisterd Dealer-Services','Interstate Purchase from Unregisterd Dealer-Taxable','Interstate Purchase Nil Rated','Interstate Purchase Taxable','Interstate Purchase Deemed Exports-Exempt','Interstate Purchase Deemed Exports-Nil Rated','Interstate Purchase Deemed Exports-Taxable','Purchase Deemed Exports-Exempt','Purchase Deemed Exports-Nil Rated','Purchase Deemed Exports-Taxable','Purchase Exempt','Purchase from Composition Dealer','Purchase from SEZ-Exempt','Purchase from SEZ-LUT/Bond','Purchase from SEZ-Nil Rated','Purchase from SEZ-Taxable','Purchase from SEZ(Without Bill of Entry)-Exempt','Purchase from SEZ(Without Bill of Entry)-Nil Rated','Purchase from SEZ(Without Bill of Entry)-Taxable','Purchase from Unregisterd Dealer-Exempt','Purchase from Unregisterd Dealer-Nil Rated','Purchase from Unregisterd Dealer-Taxable','Purchase Nil Rated','Purchase Taxable']
        Label(gstscreen, text='Tax Details',).place(x=20, y=100)
        gsttx = Label(gstscreen, text='Taxability:').place(x=20, y=140)
        gcmb2 = ttk.Combobox(gstscreen, width=35)
        gcmb2.place(x=210,y=140)
        gcmb2['values'] = ['Unknown','Exempt','Nil Rated','Taxable']
        Label(gstscreen, text='Tax Type',).place(x=20, y=170)
        Label(gstscreen, text='Rate',).place(x=210, y=170)
        inttax  = Label(gstscreen, text='Integrated Tax:').place(x=20, y=200)
        intx = StringVar()
        entry1 = Entry(gstscreen, textvariable=intx,
                   width=38)
        entry1.place(x=210, y=200)
        entry1.insert(0,'%')
        cess = Label(gstscreen, text='Cess:').place(x=20, y=230)
        ctx = StringVar()
        entry2 = Entry(gstscreen,textvariable=ctx,
                   width=38)
        entry2.place(x=210, y=230)
        entry2.insert(0,'%')
        gstt_btn = Button(gstscreen, text='Submit', width=18, fg="white", font=("arial", 13),bg='green',activebackground="yellow",command=gstt_submit,relief=GROOVE).place(x=160, y=260)
        
def gstt_submit():
    gs1 = gcmb1.get()
    gs2 = gcmb2.get()
    gs3 = intx.get()
    gs4 = ctx.get()
    sql = 'INSERT INTO ledger_gst(transaction_nature,taxability,integrate_tax ,cess)  VALUES(%s,%s,%s,%s)'
    val = (gs1, gs2, gs3, gs4)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Gst Successfully')
        
    
def ledger():
    screen2 = Toplevel(root)
    screen2.title('CREATE')
    screen2.geometry('700x630')
    Label(screen2, text='Ledger Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global ledg_name,cmb,cmb1, cmb2, cmb3,cmb4,ledg_nme,ledg_adrs,ledg_state,ledg_country,ledg_pincod,cmb5,ledg_intax
    lname = Label(screen2, text='Name:').place(x=20, y=70)
    ledg_name = StringVar()
    entry1 = Entry(screen2, textvariable=ledg_name,
                   width=38).place(x=130, y=70)
    under = Label(screen2, text='Under:').place(x=20, y=100)
    ledger_grp = ['Bank Accounts','Bank OCC A/c','Bank OD A/c','Branch/Divisions','Capital Account','Cash-in-Hand','Current Assets','Current Liabilities','Deposits(Asset)','Direct Expenses','Direct Income','Duties & Taxes','Expenses(Direct)','Expenses(Indirect)','Fixed Assets','Income(Direct)','Income(Indirect)','Indirect Expenses','Indirect Incomes','Investments','Loans & Advances(Asset)','Loans(Liability)','Misc Expenses(ASSET)','Provisions','Purchase Account','Reserves & Surplus','Retained Earnings','Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debitors','Suspense A/c','Unsecured Loans']
    cmb = ttk.Combobox(screen2, value=ledger_grp, width=35)
    cmb.place(x=130, y=100)
    type = Label(screen2, text='Type Of Ledger:').place(x=20, y=130)
    ledger_typ = ['Not Applicable','Discount','Invoice Rounding']
    cmb1 = ttk.Combobox(screen2, value=ledger_typ, width=35)
    cmb1.place(x=130, y=130)
    st_details = Label(screen2, text='Statutory Details',font=('arial',11)).place(x=20, y=180)
    gst_applcbl = Label(screen2, text='Is GST Applicable:',).place(x=20, y=210)
    gst_combo = ['Applicable', 'Not Applicable', 'Undefined']
    cmb2 = ttk.Combobox(screen2, value=gst_combo, width=35)
    cmb2.place(x=135, y=210)
    set = Label(screen2, text='Set/Alter GST Details:').place(x=20, y=240)
    set_combo = ['Yes', 'No']
    cmb3 = ttk.Combobox(screen2, value=set_combo, width=35)
    cmb3.place(x=135, y=240)
    cmb3.bind("<<ComboboxSelected>>",gstfun)
    supply_typ = Label(screen2, text='Type Of Supply:').place(x=20, y=270)
    supply_combo = ['Goods', 'Services']
    cmb4 = ttk.Combobox(screen2, value=supply_combo, width=35)
    cmb4.place(x=135, y=270)
    Label(screen2, text='Mailing Details',
          font='14', fg="black").place(x=20,y=300)
    led_name = Label(screen2, text='Name:').place(x=20, y=330)
    ledg_nme = StringVar()
    entry2 = Entry(screen2, textvariable=ledg_nme,
                   width=38).place(x=130, y=330)
    led_addrss = Label(screen2, text='Address:').place(x=20, y=360)
    ledg_adrs = StringVar()
    entry3 = Entry(screen2, textvariable=ledg_adrs,
                   width=38).place(x=130, y=360)
    led_state = Label(screen2, text='State:').place(x=20, y=390)
    ledg_state = StringVar()
    entry4 = Entry(screen2, textvariable=ledg_state,
                   width=38).place(x=130, y=390)
    led_country = Label(screen2, text='Country:').place(x=20, y=420)
    ledg_country = StringVar()
    entry5 = Entry(screen2, textvariable=ledg_country,
                   width=38).place(x=130, y=420)
    led_pincode = Label(screen2, text='Pincode:').place(x=20, y=450)
    ledg_pincod = StringVar()
    entry6 = Entry(screen2, textvariable=ledg_pincod,
                   width=38).place(x=130, y=450)
    Label(screen2, text='Banking Details',
          font='14', fg="black").place(x=20,y=480)
    led_bnk = Label(screen2, text='Provide Bank Details:').place(x=20, y=510)
    ledg_bnkdetail = ['Yes','No']
    cmb5 = ttk.Combobox(screen2, value=ledg_bnkdetail, width=35)
    cmb5.place(x=135, y=510)
    Label(screen2, text='Tax Registration Details:',
          font='14', fg="black").place(x=20,y=540)
    led_tax = Label(screen2, text='PAN/IN no:').place(x=20, y=570)
    ledg_intax = StringVar()
    entry7 = Entry(screen2, textvariable=ledg_intax,
                   width=38).place(x=130, y=570)
    ledger_btn = Button(screen2, text='Submit', width=18, fg="white", font=("arial", 13),bg='green',activebackground="yellow",command=ledger_submit,relief=GROOVE).place(x=160, y=600)

def ledger_submit():
    ledg_nmee = ledg_name.get()
    ledg_cmb = cmb.get()
    ledg_cmb1 = cmb1.get()
    ledg_cmb2 = cmb2.get()
    ledg_cmb3 = cmb3.get()
    ledg_cmb4 = cmb4.get()
    ledg_namee = ledg_nme.get()
    ledg_addrss = ledg_adrs.get()
    ledg_stte = ledg_state.get()
    ledg_cuntry =  ledg_country.get()
    ledg_pncode = ledg_pincod.get()
    ledg_cmb5 = cmb5.get()
    ledg_itax = ledg_intax.get()
    sql = 'INSERT INTO master_ledger(name,under,type,gst_applicable,set_gst,supply_type,mail_name,addrss,state,country,pincode,bank_details,pan_no)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (ledg_nmee,ledg_cmb,ledg_cmb1,ledg_cmb2,ledg_cmb3,ledg_cmb4,ledg_namee,ledg_addrss,ledg_stte,ledg_cuntry,ledg_pncode,ledg_cmb5,ledg_itax)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Ledger Successfully')
        
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
    stock_itemscrn.geometry('500x370')
    Label(stock_itemscrn, text='Stock Item Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global stock_item_name,stock_entry4,stock_entry5,stock_entry6, stock_entry7, stock_entry8
    Stock_itemname = Label(stock_itemscrn, text='Name:').place(x=20, y=70)
    stock_item_name = StringVar()
    stock_entry1 = Entry(stock_itemscrn, textvariable=stock_item_name,
                         width=38).place(x=210, y=70)
    Stock_itemunder = Label(stock_itemscrn, text='Under:').place(x=20, y=100)
    sql = "SELECT name FROM stockGroup"
    mycursor.execute(sql,)
    stck_under= mycursor.fetchall()
    stck_nameunder = []
    for i in stck_under:
        stck_nameunder.append(i[0])
    stock_entry4 = ttk.Combobox(stock_itemscrn,width=35)
    stock_entry4.place(x=210,y=100)
    stock_entry4['values'] = stck_nameunder
    Stock_itemunit = Label(stock_itemscrn, text='Units:').place(x=20, y=130)
    stockk_under = ['Applicable','Not Applicable']
    stock_entry5 = ttk.Combobox(stock_itemscrn, value=stockk_under, width=35)
    stock_entry5.place(x=210, y=130) 
    Label(stock_itemscrn, text='Statutory Details',
          font='17', fg="black").place(x=20,y=160)
    Stock_gst = Label(stock_itemscrn, text='GST Applicable:').place(x=20, y=190)
    stockk_under1 = ['Applicable','Not Applicable']
    stock_entry6 = ttk.Combobox(stock_itemscrn, value=stockk_under1, width=35)
    stock_entry6.place(x=210, y=190)
    Stock_detail = Label(stock_itemscrn, text='Set/Alter GST details:').place(x=20, y=220)
    stockk_under2 = ['Yes','No']
    stock_entry7 = ttk.Combobox(stock_itemscrn, value=stockk_under2, width=35)
    stock_entry7.place(x=210, y=220)
    Stock_typ = Label(stock_itemscrn, text='Type of Supply:').place(x=20, y=250)
    stockk_under3 = ['Goods','Services']
    stock_entry8 = ttk.Combobox(stock_itemscrn, value=stockk_under3, width=35)
    stock_entry8.place(x=210, y=250)
    stock_itembtn = Button(stock_itemscrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=stock_itemsubmit, relief=GROOVE).place(x=160, y=290)
        
def stock_itemsubmit():
    stck_nme = stock_item_name.get()
    stck_under = stock_entry4.get()
    stck_units = stock_entry5.get()
    stck_gst = stock_entry6.get()
    stck_detail = stock_entry7.get()
    stck_supply = stock_entry8.get()
    sql = 'INSERT INTO stock_item(name,stock_under,units,gst_applicable,gst_details,supply_type) VALUES(%s,%s,%s,%s,%s,%s)'
    val = (stck_nme,stck_under,stck_units, stck_gst,stck_detail, stck_supply)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Stock Item Successfully Created')

def unit() :
    unitscrn = Toplevel(root)
    unitscrn.title('CREATE')
    unitscrn.geometry('500x300')
    Label(unitscrn, text='Unit Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global unientry, unit_symp, unit_formal, unit_qntity, unit_plces
    unit_name = Label(unitscrn, text='Type:').place(x=20, y=70)
    unit_item_name = ['Compound','Simple']
    unientry = ttk.Combobox(unitscrn, value=unit_item_name, width=35)
    unientry.place(x=210, y=70)
    unit_sym = Label(unitscrn, text='Symbol:').place(x=20, y=100)
    unit_symp = StringVar()
    unit_entry1 = Entry(unitscrn, textvariable=unit_symp,
                         width=38).place(x=210, y=100)
    unit_foml = Label(unitscrn, text='Formal Name:').place(x=20, y=130)
    unit_formal = StringVar()
    unit_entry2 = Entry(unitscrn, textvariable=unit_formal,
                         width=38).place(x=210, y=130)
    unit_qnty = Label(unitscrn, text='Unit Quantity Code:').place(x=20, y=160)
    unit_qntity = StringVar()
    unit_entry2 = Entry(unitscrn, textvariable=unit_qntity,
                         width=38).place(x=210, y=160)
    unit_plcs = Label(unitscrn, text='No of decimal places:').place(x=20, y=190)
    unit_plces = IntVar()
    unit_entry3 = Entry(unitscrn, textvariable=unit_plces,
                         width=38).place(x=210, y=190)
    
    unit_itembtn = Button(unitscrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=unit_submit, relief=GROOVE).place(x=220, y=230)

def unit_submit():
    unit_typ = unientry.get()
    unit_symbol = unit_symp.get()
    unit_formall = unit_formal.get()
    unit_quntity = unit_qntity.get()
    unit_deci = unit_plces.get()
    sql = 'INSERT INTO unit(type,symbol,formal_name,quantity_code,no_of_decimal_places) VALUES(%s,%s,%s,%s,%s)'
    val = (unit_typ, unit_symbol, unit_formall, unit_quntity, unit_deci)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Unit Successfully Created')

def godown():
    godownscrn = Toplevel(root)
    godownscrn.title('CREATE')
    godownscrn.geometry('500x300')
    Label(godownscrn, text='Godown Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global gdwn_nme,gdwn_under
    gdown_name = Label(godownscrn, text='Name:').place(x=20, y=70)
    gdwn_nme = StringVar()
    gdwn_entry1 = Entry(godownscrn, textvariable=gdwn_nme,
                         width=38).place(x=190, y=70)
    gdown_under = Label(godownscrn, text='Under:').place(x=20, y=100)
    gdwn_under = StringVar()
    gdwn_entry2 = Entry(godownscrn, textvariable=gdwn_under,
                         width=38).place(x=190, y=100)                
    gd_btn = Button(godownscrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=gdwn_submit, relief=GROOVE).place(x=220, y=150)

def gdwn_submit():
    gd_name = gdwn_nme.get()
    gd_under = gdwn_under.get()
    sql = 'INSERT INTO godown(name,under) VALUES(%s,%s)'
    val = (gd_name, gd_under)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Godown Successfully Created')
    
def gst_details():
    gstscrn = Toplevel(root)
    gstscrn.title('CREATE')
    gstscrn.geometry('850x650')
    gstscrn.resizable(False, False)
    Label(gstscrn, text='Gst Details', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(gstscrn, text='Gst Registration Details',
          font='14', fg="black").place(x=20,y=70)
    Label(gstscrn, text='Invoice Features',
          font='14', fg="black").place(x=440,y=70)
    global gst_nme, gst_entry2, gst_entry3, gst_entry4, gst_entry5, gst_entry6, gst_entry7,gst_thlmt,gst_entry9,gst_entry10,gst_lmt,gst_entry12,gst_entry13,gst_entry14,gst_entry15,gst_entry16,gst_entry17,gst_entry18,gst_entry19
    gst_name = Label(gstscrn, text='State:').place(x=20, y=110)
    gst_nme = StringVar()
    gst_entry1 = Entry(gstscrn, textvariable=gst_nme,
                        width=40).place(x=150, y=110)
    gst_bill = Label(gstscrn, text='e-way Bill applicable:').place(x=440, y=110)
    gst_applcble = ['Yes', 'No']
    gst_entry2 = ttk.Combobox(gstscrn, value=gst_applcble, width=33)
    gst_entry2.place(x=580, y=110)
    gst_typ = Label(gstscrn, text='Registration type:').place(x=20, y=140)
    gst_type = ['Composition', 'Regular']
    gst_entry3 = ttk.Combobox(gstscrn, value=gst_type, width=37)
    gst_entry3.place(x=150, y=140)
    gst_applcble = Label(gstscrn, text='applicable from:').place(x=440, y=140)
    gst_entry4 = DateEntry(gstscrn, width=33)
    gst_entry4.place(x=580, y=140)
    gst_other = Label(gstscrn, text='Assessee of other\ntemptory:').place(x=20, y=170)
    gst_othertem = ['Yes', 'No']
    gst_entry5 = ttk.Combobox(gstscrn, value=gst_othertem, width=37)
    gst_entry5.place(x=150, y=170)
    gst_thrshold = Label(gstscrn, text='Threshold limit includes:').place(x=440, y=170)
    gst_limit = ['Invoice value', 'Taxable and exempt good value','Taxable good value']
    gst_entry6 = ttk.Combobox(gstscrn, value=gst_limit, width=33)
    gst_entry6.place(x=580, y=170)
    gst_appfrom = Label(gstscrn, text='GST applicable from:').place(x=20, y=205)
    gst_entry7 = DateEntry(gstscrn, width=37)
    gst_entry7.place(x=150, y=205)
    gst_thrslmt = Label(gstscrn, text='Threshold limit:').place(x=440, y=205)
    gst_thlmt = IntVar()
    gst_entry8 = Entry(gstscrn, textvariable=gst_thlmt,
                        width=36).place(x=580, y=205)
    Label(gstscrn, text='GSTN/UIN:').place(x=20, y=225)
    gst_un = Label(gstscrn, text='Periodicity of GSTR1:').place(x=20, y=250)
    gst_untem = ['Monthly', 'Quartly']
    gst_entry9 = ttk.Combobox(gstscrn, value=gst_untem, width=37)
    gst_entry9.place(x=150, y=250)
    gst_intra = Label(gstscrn, text='Applicable for intrastate:').place(x=440, y=250)
    gst_state = ['Yes', 'No']
    gst_entry10 = ttk.Combobox(gstscrn, value=gst_state, width=33)
    gst_entry10.place(x=580, y=250)
    Label(gstscrn, text='Additional Features').place(x=20, y=280)
    gst_print = Label(gstscrn, text='Threshold limit:').place(x=440, y=280)
    gst_lmt = IntVar()
    gst_entry11 = Entry(gstscrn, textvariable=gst_lmt,
                        width=36).place(x=580, y=280)
    gst_cess = Label(gstscrn, text='Kerala Flood Cess \napplicable:').place(x=20, y=310)
    gst_cessap = ['Yes', 'No']
    gst_entry12 = ttk.Combobox(gstscrn, value=gst_cessap, width=37)
    gst_entry12.place(x=150, y=310)
    gst_prnt = Label(gstscrn, text='Print e-way bill with \ninvoice:').place(x=440, y=310)
    gst_pt = ['Yes', 'No']
    gst_entry13 = ttk.Combobox(gstscrn, value=gst_pt, width=33)
    gst_entry13.place(x=580, y=310)
    gst_set = Label(gstscrn, text='Set/alter gst rate details:').place(x=20, y=360)
    gst_cessap = ['Yes', 'No']
    gst_entry14 = ttk.Combobox(gstscrn, value=gst_cessap, width=37)
    gst_entry14.place(x=150, y=360)
    gst_invce = Label(gstscrn, text='e-invoicing applicable:').place(x=440, y=360)
    gst_invoice = ['Yes', 'No']
    gst_entry15 = ttk.Combobox(gstscrn, value=gst_invoice, width=33)
    gst_entry15.place(x=580, y=360)
    gst_tax = Label(
        gstscrn, text='Enable tax liability on \nadvance receipts:').place(x=20, y=390)
    gst_taxneed = ['Yes', 'No']
    gst_entry16 = ttk.Combobox(gstscrn, value=gst_taxneed, width=37)
    gst_entry16.place(x=150, y=390)
    gst_tax = Label(
        gstscrn, text='Enable tax liability on \nreverse charge:').place(x=20, y=430)
    gst_retaxneed = ['Yes', 'No']
    gst_entry17 = ttk.Combobox(gstscrn, value=gst_retaxneed, width=37)
    gst_entry17.place(x=150, y=430)
    gst_taxclas = Label(
        gstscrn, text='Enable gst \nclassifications:').place(x=20, y=470)
    gst_cls = ['Yes', 'No']
    gst_entry18 = ttk.Combobox(gstscrn, value=gst_cls, width=37)
    gst_entry18.place(x=150, y=470)
    gst_detls = Label(
        gstscrn, text='Provide LUT/Bond \ndetails:').place(x=20, y=510)
    gst_details = ['Yes', 'No']
    gst_entry19 = ttk.Combobox(gstscrn, value=gst_details, width=37)
    gst_entry19.place(x=150, y=510)
    gst_btn = Button(gstscrn, text='Submit', width=16, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=gst_submit, relief=GROOVE).place(x=380, y=560)

def gst_submit():
    gstt_state = gst_nme.get()
    gstt_applcble = gst_entry2.get()
    gstt_type = gst_entry3.get()
    gstt_appfrom = gst_entry4.get_date()
    gstt_assesee = gst_entry5.get()
    gstt_threshold = gst_entry6.get()
    gstt_applfrom = gst_entry7.get_date()
    gstt_threshold1 = gst_thlmt.get()
    gstt_periodcity = gst_entry9.get()
    gstt_intrastate = gst_entry10.get()
    gstt_threshold2 = gst_lmt.get()
    gstt_cess = gst_entry12.get()
    gstt_print = gst_entry13.get()
    gstt_detls = gst_entry14.get()
    gstt_invoice = gst_entry15.get()
    gstt_advnce = gst_entry16.get()
    gstt_revrse = gst_entry17.get()
    gstt_cls = gst_entry18.get()
    gstt_bond = gst_entry19.get()
    sql = 'INSERT INTO gst(state,bill_applicable,reg_type,applicable_from,assessee,threshold_limit_includes,gst_applicable,threshold_limit,periodicity,applcble_intrastate,cess_applicable,threshold_limit1,gst_details,print_bill,advance_receipts,invoice_applicable,reverse_charge,gst_class,bond_details) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (gstt_state,gstt_applcble,gstt_type,
           gstt_appfrom,gstt_assesee,gstt_threshold,gstt_applfrom,gstt_threshold1,gstt_periodcity,gstt_intrastate,gstt_cess,gstt_threshold2,gstt_detls, gstt_print, gstt_advnce,gstt_invoice,gstt_revrse,gstt_cls,gstt_bond)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('gst Successfully Created')
    
def Pan_details():
    PANscrn = Toplevel(root)
    PANscrn.title('CREATE')
    PANscrn.geometry('390x270')
    PANscrn.resizable(False, False)
    Label(PANscrn, text='PAN/CIN Details', bg="blue",
          font='17', fg="white", width=430).pack()
    global pan_nme
    pan_name = Label(PANscrn, text='PAN/Income Tax No:').place(x=20, y=70)
    pan_nme = StringVar()
    pan_entry1 = Entry(PANscrn, textvariable=pan_nme,
                        width=33).place(x=150, y=70)
    pan_btn = Button(PANscrn, text='Submit', width=13, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=PAN_submit, relief=GROOVE).place(x=150, y=140)
        
def PAN_submit():
    pan_no = pan_nme.get()
    sql = 'INSERT INTO PAN(PAN_NUMBER) VALUES(%s)'
    val = (pan_no,)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('PAN Details Successfully Created')

b1 = Button(root, text="Create", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=create_master).place(x=830, y=180)

def master_alter():
    altscrn = Toplevel(root)
    altscrn.title('ALTER')
    altscrn.geometry('500x500')
    Label(altscrn, text='List Of Masters', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(altscrn, text='Accounting Masters',
          font=('Arial', 11), fg="black").place(x=10, y=50)
    Button(altscrn, text='Change Company', command=change_company, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=308, y=50)
    Button(altscrn, text='Group', command=group, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=70)
    Button(altscrn, text='Ledger', command=ledger, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=90)
    Button(altscrn, text='Currency', command=currency_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=110)
    Button(altscrn, text='Rate Of Exchange', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=130)
    Button(altscrn, text='Voucher Type', command=voucher_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=150)
    Label(altscrn, text='Inventory Masters',
          font=('Arial', 11), fg="black").place(x=10, y=180)
    Button( altscrn, text='Stock Group', command=stock_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=200)
    Button(altscrn, text='Stock Catagory', command=stock_catagory, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=220)
    Button(altscrn, text='Stock Item', command=stock_item, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=240)
    Button(altscrn, text='Unit', command=unit, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=260)
    Button(altscrn, text='Godown', command=godown, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=280)
    Label(altscrn, text='Statutory Details',
          font=('Arial', 11), fg="black").place(x=10, y=310)
    Button(altscrn, text='GST Details', command=gst_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=340)
    Button(altscrn, text='PAN/CIN Details', command=Pan_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=360)
        
b2 = Button(root, text="Alter", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=master_alter).place(x=830, y=210)
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
