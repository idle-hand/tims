import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Tool Inventory Managment System - TIMS(2018)')
root.minsize(200,300)



#root.geometry("500x500")



##from tkinter import *
## toplevel window widget coding

##root = Tk()
#top = tk.Toplevel()
##top.mainloop()

        

f1 = tk.Frame(root)
f1.grid(row=0,column=0)
b1 = ttk.Button(f1, text="Hello World - f1")
b1.grid(row=0,column=0)

f2 = tk.Frame(root)
f2.grid(row=1,column=0)
b2 = ttk.Button(f2, text="Hello World - f2")
b2.grid(row=0,column=0)

f3 = tk.Frame(root)
f3.grid(row=0,column=1)
b3 = ttk.Button(f3, text="Hello World - f3")
b3.grid(row=0,column=0)

f4 = tk.Frame(root)
f4.grid(row=1,column=1)
b4 = ttk.Button(f4, text="Hello World - f4")
b4.grid(row=0,column=0)


    


root.mainloop()
