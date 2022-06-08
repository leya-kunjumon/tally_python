# shut_frame = Frame(screen7)
# shut_frame.pack(fill=BOTH,expand=1)
# my_canvas = Canvas(shut_frame)
# my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
# shut_scroll = ttk.Scrollbar(shut_frame,orient=VERTICAL,command=my_canvas.yview)
# shut_scroll.pack(side=RIGHT,fill=Y)
# my_canvas.configure(yscrollcommand=shut_scroll.set)
# my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# shut2_frame = Frame(my_canvas)
# my_canvas.create_window((0,0),window=shut2_frame,anchor="nw")

# mycursor.execute('SELECT name FROM company')
# for i in mycursor.fetchall():
#    Button(shut2_frame,text=i[0],fg="black",width=20,border=0,font=( "arial", 13),
#    activebackground="yellow",command=shut).grid(column=0,pady=10,padx=40)
