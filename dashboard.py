from glob import glob
import imghdr
from msilib.schema import Font, Icon
from sre_constants import ANY
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
from tkinter import font
from tkinter.font import BOLD
# from tkinter import _Anchor
from turtle import bgcolor, width
import mysql.connector
import io
from models import *
import tkcalendar
from tkcalendar import DateEntry
from PIL import ImageTk,Image
root=Tk()
root.geometry("1360x730")
root.resizable(True, True)
root.title("TALLY PRIME")
curnt_period = Label(root, text="CURRENT PERIOD",fg="blue").place(x=40, y=30)
curnt_date = Label(root, text="CURRENT DATE",fg="blue").place(x=340, y=30)
prd = Label(root, text="1-Apr-22 to 31-March-23", fg="black").place(x=40, y=60)
date = dt.datetime.now()
# Create Label to display the Date
label = Label(root, text=f"{date:%A,  %d-%B-%Y}",fg="black")
label.place(x=340, y=60)

style1 =  ttk.Style()
style1.configure("mystyle1.Treeview",borderwidth=0, font=(
    'Calibri', 11, 'bold'))  # Modify the font of the body
style1.configure("mystyle1.Treeview.Heading", font=('Calibri', 10, 'bold'),
                 foreground="blue")  # Modify the font of the headings

ord_previewtree = ttk.Treeview(
    root, style="mystyle1.Treeview")

treescroll = ttk.Scrollbar(ord_previewtree, orient="vertical",
                           command=ord_previewtree.yview)
treescroll.pack(side='right', fill='y')
ord_previewtree.configure(yscrollcommand=treescroll.set)

ord_previewtree["columns"] = ["1","2"]
ord_previewtree.column("#0", width=1)
ord_previewtree.column("1", width=100)
ord_previewtree.column("2", width=300)

ord_previewtree.heading("#0",text="")
ord_previewtree.heading("1",text="Name Of Company")
ord_previewtree.heading("2", text="Date Of Last Entry")
ord_previewtree.place(x=5, y=130, width=600,height=550)
separator = ttk.Separator(root, orient='vertical')
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
frame = Label(root, text="Gateway of Tally", bg="skyblue", fg="black",
              width=40, padx=20, pady=10).place(x=740, y=65)
frame1 = Frame(root, bg="black", width=305, height=570)
frame1.place(x=740, y=100)
frame2 = Frame(frame1, bg="skyblue", width=305, height=570)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="MASTERS", bg="skyblue",
              fg="black", font="17").place(x=850, y=150)

def create_master() :
    screen1 = Toplevel(root)
    screen1.title('CREATE')
    screen1.geometry('500x650')
    Label(screen1, text='List Of Masters', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(screen1, text='Accounting Masters',
          font=('Arial', 11), fg="black").place(x=10, y=100)
    Button(screen1, text='Change Company', command=change_company, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=308, y=50)
        
    def showMore() :  
        Button(screen1, text='Budget',fg='black', font=(
            'Arial', 10), activebackground='yellow', border=0).place(x=13, y=220) 
        
        Button(screen1, text='Scenario',fg='black', font=(
            'Arial', 10), activebackground='yellow', border=0).place(x=13, y=240)
        Button(screen1, text='Credit Limits',fg='black', font=(
            'Arial', 10), activebackground='yellow', border=0).place(x=13, y=260) 
                        
    Button(screen1, text='Show More', command=showMore, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=308, y=70)
    
    Button(screen1, text='Group', command=group, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=120)
    Button(screen1, text='Ledger', command=ledger, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=140)
    Button(screen1, text='Currency', command=currency_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=160)
    Button(screen1, text='Rate Of Exchange', command=rateof_exchnge, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=180)
    Button(screen1, text='Voucher Type', command=voucher_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=200)
    Label(screen1, text='Inventory Masters',
          font=('Arial', 11), fg="black").place(x=10, y=290)
    Button(screen1, text='Stock Group', command=stock_creation, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=310)
    Button(screen1, text='Stock Catagory', command=stock_catagory, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=330)
    Button(screen1, text='Stock Item', command=stock_item, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=350)
    Button(screen1, text='Unit', command=unit, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=370)
    Button(screen1, text='Godown', command=godown, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=390)
    Label(screen1, text='Statutory Details',
          font=('Arial', 11), fg="black").place(x=10, y=420)
    Button(screen1, text='GST Details', command=gst_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=440)
    Button(screen1, text='PAN/CIN Details', command=Pan_details, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=460)
        
def change_company():
    global changescrn
    changescrn = Toplevel()
    changescrn.title('CREATE')
    changescrn.geometry('380x300')
    Label(changescrn, text='Change Company', bg="navyblue",
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
    chng_btn = Button(changescrn, text='Submit', width=17, fg="white", font=( "arial", 13),bg='green',activebackground="yellow",command=change,relief=GROOVE).place(x=140, y=120)

def change() :
    messagebox.showinfo('Change Company Successfully')

def group():
    grpscrn = Toplevel()
    grpscrn.title('CREATE')
    grpscrn.geometry('600x500')
    Label(grpscrn, text='Group Creation', bg="blue",
    font='17', fg="white", width=430).pack()
    global grpname, grpcmb, grpcmb1, grpcmb2, grpcmb3,grpcmb4
    gname = Label(grpscrn, text='Name:').place(x=20, y=70)
    grpname = StringVar()
    grpentry1 = Entry(grpscrn, textvariable=grpname,width=38).place(x=250, y=70)
    gunder = Label(grpscrn, text='Under:').place(x=20, y=100)
    grp_under = ['Bank Accounts','Bank OCC A/c','Bank OD A/c','Branch/Divisions','Capital Account',
    'Cash-in-Hand','Current Assets','Current Liabilities','Deposits(Asset)','Direct Expenses','Direct Income','Duties & Taxes','Expenses(Direct)','Expenses(Indirect)','Fixed Assets','Income(Direct)',
    'Income(Indirect)','Indirect Expenses','Indirect Incomes','Investments','Loans & Advances(Asset)','Loans(Liability)','Misc Expenses(ASSET)','Provisions','Purchase Account','Reserves & Surplus','Retained Earnings','Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debitors','Suspense A/c','Unsecured Loans']
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
    grpcalc = Label(grpscrn,text='Used for Calculation:').place(x=20, y=190)
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
    grp_cmny = comcmb.get()
    sql = 'INSERT INTO mastergroup(name,grp_under,grp_ledger,balance_reporting ,calculn_used,method,company_name)  VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val = (grp_name, grp_under, grp_ledger,
           grp_blnce, grp_calcn, grp_method, grp_cmny)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('Create Group Successfully')
    
def gstfun(event):
    ledg_cmb3 = cmb3.get()
    if ledg_cmb3 == 'Yes':
        gstscreen = Toplevel()
        gstscreen.title('CREATE')
        gstscreen.geometry('500x380')
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
        gstt_btn = Button(gstscreen, text='Submit', width=18, fg="white", font=("arial", 13),bg='green',activebackground="yellow",command=gstt_submit,relief=GROOVE).place(x=160, y=280)
        
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
    screen2 = Toplevel()
    screen2.title('CREATE')
    screen2.geometry('700x630')
    Label(screen2, text='Ledger Creation', bg="blue",
          font='17', fg="white", width=430).pack()
    global ledg_name,cmb,cmb1, cmb2, cmb3,cmb4,ledg_nme,ledg_adrs,ledg_state,ledg_country,ledg_pincod,cmb5,ledg_intax
    lname = Label(screen2, text='Name:').place(x=20, y=50)
    ledg_name = StringVar()
    entry1 = Entry(screen2, textvariable=ledg_name,
                   width=38).place(x=130, y=50)
    under = Label(screen2, text='Under:').place(x=20, y=80)
    ledger_grp = ['Bank Accounts','Bank OCC A/c','Bank OD A/c','Branch/Divisions','Capital Account','Cash-in-Hand','Current Assets','Current Liabilities','Deposits(Asset)','Direct Expenses','Direct Income','Duties & Taxes','Expenses(Direct)','Expenses(Indirect)','Fixed Assets','Income(Direct)','Income(Indirect)','Indirect Expenses','Indirect Incomes','Investments','Loans & Advances(Asset)','Loans(Liability)','Misc Expenses(ASSET)','Provisions','Purchase Account','Reserves & Surplus','Retained Earnings','Sales Accounts','Secured Loans','Stock-in-Hand','Sundry Creditors','Sundry Debitors','Suspense A/c','Unsecured Loans']
    cmb = ttk.Combobox(screen2, value=ledger_grp, width=35)
    cmb.place(x=130, y=80)
    type = Label(screen2, text='Type Of Ledger:').place(x=20, y=110)
    ledger_typ = ['Not Applicable','Discount','Invoice Rounding']
    cmb1 = ttk.Combobox(screen2, value=ledger_typ, width=35)
    cmb1.place(x=130, y=110)
    st_details = Label(screen2, text='Statutory Details',font=('arial',11)).place(x=20, y=140)
    gst_applcbl = Label(screen2, text='Is GST Applicable:',).place(x=20, y=170)
    gst_combo = ['Applicable', 'Not Applicable', 'Undefined']
    cmb2 = ttk.Combobox(screen2, value=gst_combo, width=35)
    cmb2.place(x=135, y=170)
    set = Label(screen2, text='Set/Alter GST Details:').place(x=20, y=200)
    set_combo = ['Yes', 'No']
    cmb3 = ttk.Combobox(screen2, value=set_combo, width=35)
    cmb3.place(x=135, y=200)
    cmb3.bind("<<ComboboxSelected>>",gstfun)
    supply_typ = Label(screen2, text='Type Of Supply:').place(x=20, y=230)
    supply_combo = ['Goods', 'Services']
    cmb4 = ttk.Combobox(screen2, value=supply_combo, width=35)
    cmb4.place(x=135, y=230)
    Label(screen2, text='Mailing Details',
          font=('arial',11), fg="black").place(x=20,y=260)
    led_name = Label(screen2, text='Name:').place(x=20, y=290)
    ledg_nme = StringVar()
    entry2 = Entry(screen2, textvariable=ledg_nme,
                   width=38).place(x=130, y=290)
    led_addrss = Label(screen2, text='Address:').place(x=20, y=320)
    ledg_adrs = StringVar()
    entry3 = Entry(screen2, textvariable=ledg_adrs,
                   width=38).place(x=130, y=320)
    led_state = Label(screen2, text='State:').place(x=20, y=350)
    ledg_state = StringVar()
    entry4 = Entry(screen2, textvariable=ledg_state,
                   width=38).place(x=130, y=350)
    led_country = Label(screen2, text='Country:').place(x=20, y=380)
    ledg_country = StringVar()
    entry5 = Entry(screen2, textvariable=ledg_country,
                   width=38).place(x=130, y=380)
    led_pincode = Label(screen2, text='Pincode:').place(x=20, y=410)
    ledg_pincod = StringVar()
    entry6 = Entry(screen2, textvariable=ledg_pincod,
                   width=38).place(x=130, y=410)
    Label(screen2, text='Banking Details',
          font=('arial',11), fg="black").place(x=20,y=440)
    led_bnk = Label(screen2, text='Provide Bank Details:').place(x=20, y=470)
    ledg_bnkdetail = ['Yes','No']
    cmb5 = ttk.Combobox(screen2, value=ledg_bnkdetail, width=35)
    cmb5.place(x=135, y=470)
    Label(screen2, text='Tax Registration Details:',
          font=('arial', 11), fg="black").place(x=20, y=500)
    led_tax = Label(screen2, text='PAN/IN no:').place(x=20, y=530)
    ledg_intax = StringVar()
    entry7 = Entry(screen2, textvariable=ledg_intax,
                   width=38).place(x=130, y=530)
    ledger_btn = Button(screen2, text='Submit', width=18, fg="white", font=("arial", 13),bg='green',activebackground="yellow",command=ledger_submit,relief=GROOVE).place(x=160, y=570)

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
    ledg_cmny = comcmb.get()
    
    sql = 'INSERT INTO master_ledger(name,under,type,gst_applicable,set_gst,supply_type,mail_name,addrss,state,country,pincode,bank_details,pan_no,company_name)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (ledg_nmee, ledg_cmb, ledg_cmb1, ledg_cmb2, ledg_cmb3, ledg_cmb4, ledg_namee,
           ledg_addrss, ledg_stte, ledg_cuntry, ledg_pncode, ledg_cmb5, ledg_itax, ledg_cmny)
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
    curn_cmny = comcmb.get()
    
    sql = 'INSERT INTO currency(symbol,formal_name,currency_code,decimal_places,amount_in_millions,suffix_symbol,space,word_repsn,decimal_words,company_name)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (currncy_sym,formal_name,code,dec_plc,show_plc,suffx_plc,shw_plc,word_repsn,deci_plces,curn_cmny)
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
    vouc_cmny = comcmb.get()
    sql = 'INSERT INTO voucher(name,type,abbreviation,voucher_activate,voucher_method,Use_effective_dates,allow_zero_valued,voucher_type_optional,voucher_narration,ledger_narration,voucher_saving,company_name)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (vouc_namee, vouc_type, vouc_abbrvn, vouc_actvn,
           vouc_method, vouc_date, vouc_value, vouc_typ_optional, vouc_narrtn, vouc_ledger, vouc_save, vouc_cmny)
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
    stck_cmny = comcmb.get()
    sql = 'INSERT INTO stockGroup(name,stock_under,stock_quantities,stock_details,company_name) VALUES(%s,%s,%s,%s,%s)'
    val = (stck_name, stck_under, stck_qnty, stck_details, stck_cmny)
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
    stck_cmny = comcmb.get()
    sql = 'INSERT INTO stock_Catagory(name,company_name) VALUES(%s,%s)'
    val = (stck_catag,stck_cmny)
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
    stck_cmny = comcmb.get()
    sql = 'INSERT INTO stock_item(name,stock_under,units,gst_applicable,gst_details,supply_type,company_name) VALUES(%s,%s,%s,%s,%s,%s,%s)'
    val = (stck_nme, stck_under, stck_units, stck_gst,
           stck_detail, stck_supply, stck_cmny)
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
    unit_cmny = comcmb.get()
    sql = 'INSERT INTO unit(type,symbol,formal_name,quantity_code,no_of_decimal_places,company_name) VALUES(%s,%s,%s,%s,%s,%s)'
    val = (unit_typ, unit_symbol, unit_formall,
           unit_quntity, unit_deci, unit_cmny)
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
    gd_cmny = comcmb.get()
    sql = 'INSERT INTO godown(name,under,company_name) VALUES(%s,%s,%s)'
    val = (gd_name, gd_under, gd_cmny)
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
    gstt_cmny = comcmb.get()
    sql = 'INSERT INTO gst(state,bill_applicable,reg_type,applicable_from,assessee,threshold_limit_includes,gst_applicable,threshold_limit,periodicity,applcble_intrastate,cess_applicable,threshold_limit1,gst_details,print_bill,advance_receipts,invoice_applicable,reverse_charge,gst_class,bond_details,company_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val = (gstt_state,gstt_applcble,gstt_type,
           gstt_appfrom,gstt_assesee,gstt_threshold,gstt_applfrom,gstt_threshold1,gstt_periodcity,gstt_intrastate,gstt_cess,gstt_threshold2,gstt_detls, gstt_print, gstt_advnce,gstt_invoice,gstt_revrse,gstt_cls,gstt_bond,gstt_cmny)
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
    pan_cmny = comcmb.get()
    sql = 'INSERT INTO PAN(PAN_NUMBER,company_name) VALUES(%s,%s)'
    val = (pan_no,pan_cmny)
    mycursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo('PAN Details Successfully Created')
def rateof_exchnge():
    ratescrn = Toplevel()
    ratescrn.title('CREATE')
    ratescrn.geometry('1050x500')
    Label(ratescrn, text='Rate of Exchange', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(ratescrn, text='Date of Exchange :',
          font=('arial',11), fg="black").place(x=20,y=40) 
    Label(ratescrn, text='1-Apr-2022',
          font=('arial',11), fg="black").place(x=160,y=40) 
    Label(ratescrn, text='Sl.no',
          font=('arial', 11), fg="black").place(x=20, y=70)
    Label(ratescrn, text='Currency',
          font=('arial', 11), fg="black").place(x=120, y=70)
    Label(ratescrn, text='Std Rate',
          font=('arial', 11), fg="black").place(x=360, y=70)
    Label(ratescrn, text='Selling Rate',
          font=('arial', 11), fg="black").place(x=490, y=70)
    Label(ratescrn, text='Buying Rate',
          font=('arial', 11), fg="black").place(x=760, y=70)
    Label(ratescrn, text='Last Voucher  Rate',
          font=('arial', 11), fg="black").place(x=490, y=100)
    Label(ratescrn, text='Specified Rate',
          font=('arial', 11), fg="black").place(x=640, y=100)
    Label(ratescrn, text='Last Voucher Rate',
          font=('arial', 11), fg="black").place(x=760, y=100)
    Label(ratescrn, text='Specified Rate',
          font=('arial', 11), fg="black").place(x=900, y=100)


b1 = Button(root, text="Create", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1, command=create_master).place(x=830, y=180)
            
def master_alter():
    altscrn = Toplevel(root)
    altscrn.title('ALTER')
    altscrn.geometry('500x500')
    Label(altscrn, text='List Of Masters', bg="blue",
          font='17', fg="white", width=430).pack()
    Label(altscrn, text='Accounting Masters',
          font=('Arial', 11),fg="black").place(x=10, y=110)
          
    Button(altscrn, text='Change Company', command=change_company, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=315, y=40)
    Button(altscrn, text='Expand all', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=315, y=60)
    Button(altscrn, text='Show More', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=315, y=80)
    Button(altscrn, text='Group', command=group_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=130)
    Button(altscrn, text='Ledger', command=ledger_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=150)
    Button(altscrn, text='Currency', command=currency_creation_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=170)
    Button(altscrn, text='Rate Of Exchange', command='', fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=190)
    Button(altscrn, text='Voucher Type', command=voucher_creation_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=210)
    Label(altscrn, text='Inventory Masters',
          font=('Arial', 11), fg="black").place(x=10, y=240)
    Button( altscrn, text='Stock Group', command=stock_creation_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=260)
    Button(altscrn, text='Stock Catagory', command=stock_catagory_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=280)
    Button(altscrn, text='Stock Item', command=stock_item_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=300)
    Button(altscrn, text='Unit', command=unit_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=320)
    Button(altscrn, text='Godown', command=godown_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=340)
    Label(altscrn, text='Statutory Details',
          font=('Arial', 11), fg="black").place(x=10, y=370)
    Button(altscrn, text='GST Details', command=gst_details_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=390)
    Button(altscrn, text='PAN/CIN Details', command=Pan_details_alter, fg='black', font=(
        'Arial', 10), activebackground='yellow', border=0).place(x=13, y=410)
        


def group_alter():
    altgrpscrn = Toplevel(root)
    altgrpscrn.title('ALTER')
    altgrpscrn.geometry('500x500')
    Label(altgrpscrn, text='ALTER GROUP', bg="navyblue",
          font='17', fg="white", width=430).pack()
    
def ledger_alter():
    altledgscrn = Toplevel(root)
    altledgscrn.title('ALTER')
    altledgscrn.geometry('500x500')
    Label(altledgscrn, text='ALTER LEDGER', bg="navyblue",
          font='17', fg="white", width=430).pack()

def currency_creation_alter():
    altcurncyscrn = Toplevel(root)
    altcurncyscrn.title('ALTER')
    altcurncyscrn.geometry('500x500')
    Label(altcurncyscrn, text='ALTER CURRENCY', bg="navyblue",
          font='17', fg="white", width=430).pack()
          
def voucher_creation_alter():
    altvouchrscrn = Toplevel(root)
    altvouchrscrn.title('ALTER')
    altvouchrscrn.geometry('500x500')
    Label(altvouchrscrn, text='ALTER VOUCHER', bg="navyblue",
          font='17', fg="white", width=430).pack()
          
def stock_creation_alter():
    altstckscrn = Toplevel(root)
    altstckscrn.title('ALTER')
    altstckscrn.geometry('500x500')
    Label(altstckscrn,text='ALTER STOCK', bg="navyblue",
          font='17', fg="white", width=430).pack()
          
def stock_catagory_alter():
    altstckcatgscrn = Toplevel(root)
    altstckcatgscrn.title('ALTER')
    altstckcatgscrn.geometry('500x500')
    Label(altstckcatgscrn,text='ALTER STOCK CATAGORY', bg="navyblue",
          font='17', fg="white", width=430).pack()
          
def stock_item_alter():
    altstckitmscrn = Toplevel(root)
    altstckitmscrn.title('ALTER')
    altstckitmscrn.geometry('500x500')
    Label(altstckitmscrn,text='ALTER STOCK ITEM', bg="navyblue",
          font='17', fg="white", width=430).pack()
    
def unit_alter():
    altunitscrn = Toplevel(root)
    altunitscrn.title('ALTER')
    altunitscrn.geometry('500x500')
    Label(altunitscrn,text='ALTER UNIT', bg="navyblue",
          font='17', fg="white", width=430).pack()
          
def godown_alter():
    altgodwnscrn = Toplevel(root)
    altgodwnscrn.title('ALTER')
    altgodwnscrn.geometry('500x500')
    Label(altgodwnscrn,text='ALTER GODOWN', bg="navyblue",
          font='17', fg="white", width=430).pack()
    
def gst_details_alter():
    altgstscrn = Toplevel(root)
    altgstscrn.title('ALTER')
    altgstscrn.geometry('500x500')
    Label(altgstscrn,text='ALTER GST DETAILS', bg="navyblue",
          font='17', fg="white", width=430).pack()

def Pan_details_alter():
    altpanscrn = Toplevel(root)
    altpanscrn.title('ALTER')
    altpanscrn.geometry('500x500')
    Label(altpanscrn,text='ALTER PAN DETAILS', bg="navyblue",
          font='17', fg="white", width=430).pack()


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


def func2():
    global cmpscrn
    cmpscrn = Toplevel(root)
    cmpscrn.resizable(False, False)
    cmpscrn.title('Company')
    cmpscrn.geometry('430x430')
    Label(cmpscrn, text='List Of Companies',bg="blue",font='17',fg="white",width=430).pack()
    sbmibtn = Button(cmpscrn, text='Create Company',command=create,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=40)
    sbmibtn2 = Button(cmpscrn, text='Alter Company',command=alter,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=70)
    sbmibtn3 = Button(cmpscrn, text='Select Company',command=select,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=100)
    sbmibtn4 = Button(cmpscrn, text='Shut Company', command=shut_company, fg='black',font=('Arial',9),activebackground='yellow', width=30, border=0).place(x=240, y=130)
   
    my_frame = Frame(cmpscrn)
    my_scrollbar = Scrollbar(my_frame,orient='vertical')
    global my_listbox1
    my_listbox1 = Listbox(my_frame,yscrollcommand=my_scrollbar.set,width=60)
    my_scrollbar.config(command = my_listbox1.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame.place(x=20,y=180)
    my_listbox1.pack(pady=10)
    mycursor.execute("select name from companyAble")
    for x in mycursor:
        print(x)
        my_listbox1.insert(0,x[0])
        
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
    
    sql1 = 'INSERT INTO companyAble(name, mailing_name, address, email, state, country, pincode, telephone, mobile, fax, website, financial_year, year_begin, currencysign, currency) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val1 = (coname, madrs, adrs, mail, state, country, picode,
           tno, mno, fax, site, Fyear, Byear, cusymbol, formal)
    mycursor.execute(sql1,val1)
    mydb.commit()
    
    messagebox.showinfo('Create Company Successfully')

def alter():
    global screen4
    screen4 = Toplevel(root)
    screen4.resizable(False, False)
    screen4.title('Alter Company')
    screen4.geometry('430x240')
    Label(screen4, text='ALTER COMPANY',bg="navyblue",font='17',fg="white",width=640).pack()
    global Cnamee
    Cnamee = StringVar()
    cname = Label(screen4, text='Enter Company Name:').place(x=20, y=70)
    e1 = Entry(screen4, textvariable=Cnamee, width=40).place(x=170, y=70)
    btn = Button(screen4, text='Submit', width=10, fg="white", font=(
        "arial", 13), bg='green', activebackground="yellow", command=submit1).place(x=170, y=130)

def submit1():
    global Company_name
    Company_name = Cnamee.get()
    if Company_name == "":
        Label(screen4, text='Plz enter both username and password',fg='red').place(x=85, y=260)
    else:
        sql = 'SELECT * FROM company WHERE name=%s'
        val = (Company_name,)
        mycursor.execute(sql,val)
        if mycursor.fetchone() is not None:
            submit2()
            
def submit2():
    global screen5
    screen5 = Toplevel(root)
    screen5.resizable(False, False)
    screen5.title('Alter Company')
    screen5.geometry('940x670')
    Company_name = Cnamee.get()
    sql = 'SELECT * FROM company WHERE name=%s'
    val = (Company_name,) 
    mycursor.execute(sql,val)
    c =  mycursor.fetchone()
    print(c[1])
    Label(screen5, text=c[1],bg="navyblue",font='17',fg="white",width=640).pack()
    global  Cnamee1,Cmailingg,Caddresss, mailll,stateee,countryyy,picodee,tephonee,mophonee,faxxx,siteee,symbolll,formalll
    Cnamee1 = StringVar()
    Cmailingg = StringVar()
    Caddresss = StringVar()
    mailll = StringVar()
    stateee = StringVar()
    countryyy = StringVar()
    picodee = IntVar()
    tephonee = StringVar()
    mophonee = StringVar()
    faxxx = StringVar()
    siteee = StringVar()
    symbolll = StringVar()
    formalll = StringVar()
    
    cname = Label(screen5, text='Company Name:').place(x=20, y=70)
    e1 = Entry(screen5, textvariable=Cnamee1,width=40)
    e1.place(x=130, y=70)
    e1.insert(0,c[1])
    y1 = Label(screen5, text='Financial Year begining From:').place(x=450, y=70)
    e2 = Label(screen5,text=c[12]).place(x=650, y=70)
    adrs1 = Label(screen5, text='Mailing Name:').place(x=20, y=110)
    e3 = Entry(screen5, textvariable=Cmailingg, width=40)
    e3.place(x=130, y=110)
    e3.insert(0, c[2])
    y2 = Label(screen5, text='Books Begining From:').place(x=450, y=110)
    e14 = Label(screen5,text=c[13] ).place(x=650, y=110)
    adrs = Label(screen5, text='Address:').place(x=20, y=150)
    e4 = Entry(screen5,textvariable=Caddresss,width=40)
    e4.place(x=130, y=150)
    e4.insert(0, c[3])
    state = Label(screen5, text='State:').place(x=20, y=190)
    e5 = Entry(screen5, textvariable=stateee, width=40)
    e5.place(x=130, y=190)
    e5.insert(0, c[5])
    country = Label(screen5, text='Country:').place(x=20, y=230)
    e6 = Entry(screen5, textvariable= countryyy, width=40)
    e6.place(x=130, y=230)
    e6.insert(0,c[6])
    pcode = Label(screen5, text='Pincode:').place(x=20, y=270)
    e7 = Entry(screen5, textvariable= picodee , width=40)
    e7.place(x=130, y=270)
    e7.insert(0,c[7])
    tphone = Label(screen5, text='Telephone:').place(x=20, y=310)
    e8 = Entry(screen5, textvariable=tephonee , width=40)
    e8.place(x=130, y=310)
    e8.insert(0, c[8])
    mphone = Label(screen5, text='Mobile:').place(x=20, y=350)
    e9 = Entry(screen5, textvariable=mophonee, width=40)
    e9.place(x=130, y=350)
    e9.insert(0, c[9])
    fax = Label(screen5, text='Fax:').place(x=20, y=390)
    e10 = Entry(screen5, textvariable=faxxx, width=40)
    e10.place(x=130, y=390)
    e10.insert(0, c[10])
    email = Label(screen5, text='Email:').place(x=20, y=430)
    e11 = Entry(screen5, textvariable=mailll, width=40)
    e11.place(x=130, y=430)
    e11.insert(0, c[4])
    site = Label(screen5, text='Website:').place(x=20, y=470)
    e12 = Entry(screen5, textvariable=siteee, width=40)
    e12.place(x=130, y=470)
    e12.insert(0, c[11])
    symbol = Label(screen5, text='Currency Symbol:').place(x=20, y=510)
    e13 = Entry(screen5, textvariable=symbolll, width=40)
    e13.place(x=130, y=510)
    e13.insert(0, c[14])
    formal = Label(screen5, text='Formal Name:').place(x=20, y=550)
    e14 = Entry(screen5, textvariable=formalll, width=40)
    e14.place(x=130, y=550)
    e14.insert(0, c[15])
    btn = Button(screen5, text='Submit', width=20, fg="white", font=("arial", 13), bg='green',
                 activebackground="yellow", command=submit3).place(x=160, y=590)
def submit3():
    global conamee,madrss,adrss,statee,countryy,picodee1,teno,mbno,faax,maill,sitee,cursymbol,formall
    Company_name = Cnamee.get()
    conamee = Cnamee.get()
    madrss = Cmailingg.get()
    adrss = Caddresss.get()
    maill = mailll.get()
    statee = stateee.get()
    countryy = countryyy.get()
    picodee1 = picodee.get()
    teno = tephonee.get()
    mbno = mophonee.get()
    faax = faxxx.get()
    sitee = siteee.get()
    cursymbol = symbolll.get()
    formall = formalll.get()
    sql = 'UPDATE company SET name=%s,mailing_name=%s,address=%s,email=%s,state=%s,country=%s,pincode=%s,telephone=%s,mobile=%s,fax=%s,website=%s,currencysign=%s,currency=%s WHERE name=%s'
    val = (conamee, madrss, adrss, maill,
           statee, countryy, picodee1, teno, mbno, faax, sitee, cursymbol, formall, Company_name,)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo('Updated successfully')
    
def select():
    screen6 = Toplevel(root)
    screen6.resizable(False, False)
    screen6.title('List Of Companies')
    screen6.geometry('430x330')
    Label(screen6, text='Select Company', bg="navyblue",
          font='17', fg="white", width=640).pack()
    
    def select1(event):
       LST = my_listbox.get(ANCHOR)
       print(LST)
    #    sql = 'select * from orders where order_number = %s'
    #    val =  (ord_editid,)
    #    fbcursor.execute(sql,val)
    #    edit_ord = fbcursor.fetchone()
       ord_previewtree.insert(parent='', index='end', iid=LST, text='', values=(LST,''))
       screen6.destroy()
       
    my_frame = Frame(screen6)
    my_scrollbar = Scrollbar(my_frame,orient='vertical')
    my_listbox = Listbox(my_frame, yscrollcommand=my_scrollbar.set,
                         width=55, height=16, bg="lavender", borderwidth=0)
    my_scrollbar.config(command = my_listbox.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame.place(x=20,y=30)
    my_listbox.pack(pady=10)
    mycursor.execute("select name from company")
    for x in mycursor:
        print(x)
        my_listbox.insert(0,x[0])
        my_listbox.config(font=('arial', 10, 'bold'))
    my_listbox.bind('<<ListboxSelect>>', select1)
    

def shut_company() :
    global screen7
    screen7 = Toplevel(root)
    screen7.resizable(False, False)
    screen7.title('Shut Company')
    screen7.geometry('430x430')
    Label(screen7, text='List Of Companies', bg="navyblue",
          font='17', fg="white", width=640).pack()

    def shut(event):
       global pop
       pop = Toplevel()
       pop.title("shut company")
       pop.geometry("380x280")
       pop.resizable(False, False)
       canvas = Canvas(pop, width = 100, height = 100)      
       canvas.pack()      
       img = PhotoImage(file='images/warning2.png')      
       canvas.create_image(20,20, anchor=NW, image=img)
       LST1 = my_listbox.get(ANCHOR)
       print(LST1)
       pop_label = Label(pop, text="Do you want to shut the company?",
                      fg="red", font=("helvetica", 12))
       pop_label.pack(pady=40)
       new_frame = Frame(pop)
       new_frame.pack(pady=5)
       def choice():
            LSTT = my_listbox.curselection()
            my_listbox1.delete(LSTT)
            print(LSTT)
            pop.destroy()
            screen7.destroy()
        
   
       yes = Button(new_frame, text="YES", fg="white", width=20,
                 bg="red", relief=SUNKEN, command=choice)
       yes.grid(row=2, column=2)
       no = Button(new_frame, text="NO", fg="white", width=20,
                bg="green", relief=SUNKEN, command=pop.destroy)
       no.grid(row=2, column=3, padx=10)    

    
    my_frame1 = Frame(screen7)
    my_scrollbar = Scrollbar(my_frame1,orient='vertical')
    my_listbox = Listbox(my_frame1, yscrollcommand=my_scrollbar.set,
                         width=55, height=16, bg="lavender", borderwidth=0)
    my_scrollbar.config(command = my_listbox.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame1.place(x=20,y=30)
    my_listbox.pack(pady=10)
    mycursor.execute("select name from companyAble")
    for x in mycursor.fetchall():
        print(x)
        my_listbox.insert(0,x[0])
        my_listbox.config(font=('arial', 10, 'bold'))
    my_listbox.bind('<<ListboxSelect>>',shut)
    

company = Button(frame3, text="Company", width=20, fg="black", font=(
    "impact", 8), command=func2, activebackground="yellow", activeforeground="red").place(x=13, y=50)


root.mainloop()







