

from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

scale = Scale(window, 
              from_=100, 
              to=0,
              length=500,
              orient=VERTICAL, # * orientation of scale
              font=('Consolas', 20),
              tickinterval=10, # * numeric indicator on the scale
              showvalue = 0, # * hide current value
              troughcolor = '#69EAFF',
              fg = '#FF1C00',
              
              )
scale.set(((scale['from'] - scale['to']) / 2) + scale['to']) # * set current value of the slider
scale.pack()

button =Button(window, text='submit', command=submit)
button.pack()

window.mainloop()