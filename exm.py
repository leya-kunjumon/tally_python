from tkinter import *
root = Tk()
root.geometry("1360x730")
root.resizable(True, True)
root.title("TALLY PRIME")
curnt_period = Label(root, text="Particulars",fg="blue",font=('arial',14)).place(x=20, y=34)
cash = Label(root, text="Cash", fg="black",
             font=('arial', 12)).place(x=970, y=1)
cpny = Label(root, text="ABC Pvt Ltd", fg="black",
             font=('arial', 12)).place(x=970, y=25)
dte = Label(root, text="For 1-Apr-22", fg="black",
            font=('arial', 12)).place(x=970, y=49)
trncs = Label(root, text="Transactions", fg="black",
              font=('arial', 12)).place(x=930, y=73)
debt = Label(root, text="Debit", fg="black",
              font=('arial', 12)).place(x=900, y=95)
crdt = Label(root, text="Credit", fg="black",
             font=('arial', 12)).place(x=975, y=95)
blc = Label(root, text="Closing Balance", fg="black",
            font=('arial', 12), borderwidth=2).place(x=1050, y=73)

root.mainloop()
