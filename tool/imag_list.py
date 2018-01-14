from tkinter import *

photox = ['cutters.png','plane.png','hammer.png','wrench.png','measure.png','plyers.png']




root = Tk()
frame = Frame(root)
frame.grid()

x = 0

while x < 6:
    print(photox[x])
    x = x + 1
    

bottomframe = Frame(root)
bottomframe.grid()
photo=PhotoImage(file=photox[0])
redbutton = Button(frame,image = photo,)
redbutton.grid()

photo1=PhotoImage(file=photox[1])
greenbutton = Button(frame, image = photo1,)
greenbutton.grid()

photo2=PhotoImage(file='hammer.png')
bluebutton = Button(frame, image = photo2,)
bluebutton.grid()

photo3=PhotoImage(file='wrench.png')
blackbutton = Button(frame, image = photo3,)
blackbutton.grid()

photo4=PhotoImage(file='measure.png')
orangebutton = Button(frame, image = photo4)
orangebutton.grid()

photo5=PhotoImage(file='plyers.png')
plyersbutton = Button(frame, image = photo5)
plyersbutton.grid()


root.mainloop()




