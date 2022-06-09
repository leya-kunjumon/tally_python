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

separator = ttk.Separator(root,orient='vertical')
separator.place(relx=0.47,rely=0,relwidth=0.2,relheight=1)
frame = Label(root, text="Accounts Book",bg="blue",fg="white",width=40,padx=20,pady=10).place(x=740, y=65)
frame1 = Frame(root, bg="black", width=305, height=570)
frame1.place(x=740, y=100)
frame2 = Frame(frame1, bg="skyblue", width=305, height=570)
frame2.pack(pady=10, padx=10)
mstrs = Label(root, text="Summary",bg="skyblue",fg="black",font="17").place(x=870,y=150)


b1 = Button(root, text="Cash/Bank Book", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=180)

b2 = Button(root, text="Ledger", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=210)
b3 = Button(root, text="Group Summary", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=250)
b5 = Button(root, text="Group Vouchers", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=280)
mstrs2 = Label(root, text="Register",bg="skyblue",fg="black",font="17").place(x=870,y=320)
b6 = Button(root, text="Contra Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=350)

b7 = Button(root, text="Payment Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=380)
b71 = Button(root, text="Receipt Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=410)


b8 = Button(root, text="Sales Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=460)
b9 = Button(root, text="Purchase Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=490)
          
b10 = Button(root, text="Journal Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=530)

b11 = Button(root, text="Debit Note Register", fg="black", activebackground="yellow",
            bg="silver", width=20, height=1).place(x=830, y=560)
b12= Button(root, text="Credit Note Register", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1).place(x=830, y=590)

b13 = Button(root, text="Voucher Clarification", fg="black", activebackground="yellow",
             bg="silver", width=20, height=1).place(x=830, y=630)
frame3 = Frame(root, bg="skyblue", width=130, height=750)
frame3.place(x=1200, y=0)
date = Button(frame3, text="Date", width=20, fg="black", font=(
    "impact", 8), activebackground="yellow", activeforeground="red")
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
    sbmibtn3 = Button(screen2, text='Select Company',command=select,fg='black',font=('Arial',9),activebackground='yellow',width=30,border=0).place(x=240,y=100)
    sbmibtn4 = Button(screen2, text='Shut Company', command=shut_company, fg='black',font=('Arial',9),activebackground='yellow', width=30, border=0).place(x=240, y=130)
   
    my_frame = Frame(screen2)
    my_scrollbar = Scrollbar(my_frame,orient='vertical')
    my_listbox = Listbox(my_frame,yscrollcommand=my_scrollbar.set,width=60)
    my_scrollbar.config(command = my_listbox.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame.place(x=20,y=180)
    my_listbox.pack(pady=10)
    mycursor.execute("select name from company")
    for x in mycursor:
        print(x)
        my_listbox.insert(0,x[0])
        
company = Button(frame3, text="Company", width=20, fg="black", font=(
    "impact", 8), command=func2, activebackground="yellow", activeforeground="red").place(x=13, y=50)

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
        Label(screen2, text='Plz enter both username and password',fg='red').place(x=85, y=260)
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
       image = Image.open('images/warning2.png')
       image = image.resize((70, 80), Image.ANTIALIAS)
       img = ImageTk.PhotoImage(image)
       my_img = Label(pop, image=img)
       my_img.pack()
       LST1 = my_listbox.get(ANCHOR)
       print(LST1)
       pop_label = Label(pop, text="Do you want to shut the company?",
                      fg="red", font=("helvetica", 12))
       pop_label.pack(pady=40)
       new_frame = Frame(pop)
       new_frame.pack(pady=5)
       yes = Button(new_frame, text="YES", fg="white", width=20,
                 bg="red", relief=SUNKEN, command=lambda: choice("yes"))
       yes.grid(row=2, column=2)
       no = Button(new_frame, text="NO", fg="white", width=20,
                bg="green", relief=SUNKEN, command=lambda: choice("no"))
       no.grid(row=2, column=3, padx=10)    

    
    my_frame1 = Frame(screen7)
    my_scrollbar = Scrollbar(my_frame1,orient='vertical')
    my_listbox = Listbox(my_frame1, yscrollcommand=my_scrollbar.set,
                         width=55, height=16, bg="lavender", borderwidth=0)
    my_scrollbar.config(command = my_listbox.yview)
    my_scrollbar.pack(side = RIGHT,fill=Y)
    my_frame1.place(x=20,y=30)
    my_listbox.pack(pady=10)
    mycursor.execute("select name from company")
    for x in mycursor.fetchall():
        print(x)
        my_listbox.insert(0,x[0])
        my_listbox.config(font=('arial', 10, 'bold'))
    my_listbox.bind('<<ListboxSelect>>',shut)
    

def choice(option):
    if option =="yes":
        pop.destroy()
        screen7.destroy()
        
    else:
        messagebox.showinfo('Yow will now return to application screen')
        
def shut1():
    pop1 = Toplevel()
    pop1.title("shut company")
    pop1.geometry("380x250")
    pop1.resizable(False, False)
    image = Image.open('images/warning2.png')
    image = image.resize((70, 80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    my_img = Label(pop1, image=img)
    my_img.pack()    


def unitt_alter():
    altunitscrn = Toplevel(root)
    altunitscrn.title('ALTER')
    altunitscrn.geometry('500x500')
    Label(altunitscrn, text='CREATE', bg="navyblue",
          font='17', fg="white", width=430).pack()


root.mainloop()


