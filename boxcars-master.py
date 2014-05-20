__author__ = 'leilaselchaif'
from Tkinter import *
win = Tk()
win.title('Boxcars')
#import random

lettlist = ['W''O''B''O''W''O''B''O''W''O''B''O''W''O''B']


def buttonClicked(event):
    print(int(button.cget("text")))
    lettlist[int(button.cget("text"))], lettlist[int(button.cget("text")) + 1] = lettlist[int(button.cget("text")) + 1], lettlist[int(button.cget("text"))]

listpos = IntVar()
listpos.set(1)

letters = []

for label in range(0,15):
    button = Button(win, text=str(lettlist[label]))
    button.pack()
    button.bind("<Button-1>", buttonClicked)
    letters.append(button)
    button.grid(row=1, column=label)

numbers = []

for label in range(0,15):
    button = Button(win, text=str(label))
    button.pack()
    button.bind("<Button-1>", buttonClicked)
    numbers.append(button)
    button.grid(row=2, column=label)

enter = Button(win, text="GO!")
enter.pack()
enter.grid(row=2, column=15)


#swap buttons in array
#.cget or something to identify buttons
#randomizing setup
#create trains
# random.shuffle?


win.mainloop ()
