from tkinter import *


root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)

bottomframe = Frame(root)
bottomframe.grid( )

photo=PhotoImage(file="cutters.png")
redbutton = Button(frame,  image = photo)
redbutton.grid(row=0, column=0 )

photo1=PhotoImage(file='plane.png')
greenbutton = Button(frame, image = photo1)
greenbutton.grid(row=0,  column=1
)

photo2=PhotoImage(file='hammer.png')
bluebutton = Button(frame, image = photo2)
bluebutton.grid(row=0, column=2
)

photo3=PhotoImage(file='wrench.png')
blackbutton = Button(frame, image = photo3)
blackbutton.grid(row=1,  column=0)

photo4=PhotoImage(file='measure.png')
orangebutton = Button(frame, image = photo4)
orangebutton.grid(row=1, column=1)

photo5=PhotoImage(file='plyers.png')
plyersbutton = Button(frame, image = photo5)
plyersbutton.grid(row=1, column=2)

############            - second frame created and populated here

                  
frame1 = Frame(root)
frame1.grid(row=2, column=0)

#photo6=PhotoImage(file='hacksaw.png')

photo7=PhotoImage(file='download.png')
powerdrvbutton = Button(frame1,  image = photo7)
powerdrvbutton.grid(row=0, column=0)



photo8=PhotoImage(file='0550359_1.png')
screwdrvbutton = Button(frame1,  image = photo8)
screwdrvbutton.grid(row=0,  column=1)


photo9=PhotoImage(file='0550317_1.png')
gen1but = Button(frame1, image = photo9)
gen1but.grid(row=0, column=2)

##########          - third frame created here

frame2 = Frame(root)
frame2.grid(row=0, column=1)

#photo9=PhotoImage(file='canflag.png')
Add = Button(frame2, text = 'Add')
Del = Button(frame2, text = 'Delete')
Edi = Button(frame2, text = 'Edit')
Rep = Button(frame2, text = 'Report')

Add.grid(row=0, column=0)
Del.grid(row=1, column=0)
Edi.grid(row=2, column=0)
Rep.grid(row=3, column=0)


frame3 = Frame(root,  bd=2,  relief=RIDGE)
frame3.grid(row=1, column=1)

Form = Frame(frame3, height=200)
Form.pack(side=TOP, pady=20)

def Login():
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()

#==============================FRAMES=========================================

#==============================LABELS=========================================

lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)




root.mainloop()
