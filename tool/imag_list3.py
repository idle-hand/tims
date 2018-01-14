from tkinter import *

photox = ['cutters.png','plane.png','hammer.png','wrench.png','measure.png','plyers.png']


root = Tk()
frame = Frame(root)
frame.grid()



for x in range(6):
    #print(photox[x])
    photo=PhotoImage(file=photox[x])
    b = Button(frame,image = photox[x])
    b.grid()
                  


root.mainloop()




