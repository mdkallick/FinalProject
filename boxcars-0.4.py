from Tkinter import *
win = Tk()
win.title('Boxcars')
#import random, random.shuffle
lettlist = ['W','O','B','O','W','O','B','O','W','O','B','O','W','O','B']
turn = 0


def buttonClicked(event):
    print (event.widget.cget("text"))  
    listcount = int(event.widget.cget("text")) #finds number of button and sets equal to a variable
    print(listcount)
    global turn
    if turn == 0 and lettlist[listcount] == "W":
        lettlist[listcount], lettlist[listcount + 1] = lettlist[listcount + 1], lettlist[listcount]
        turn = turn + 1
        return turn #moves for White (right one space)
    if turn == 1 and lettlist[listcount] == "B":
        lettlist[listcount], lettlist[listcount - 1] = lettlist[listcount - 1], lettlist[listcount]
        turn = turn - 1
        return turn #moves for Black (left one space)
    else:
        print("error") #error message if O (space), or wrong color is clicked
    print(lettlist)

def goClicked(event):
    letters = []
    numbers = []
    global turn
    length = (len(lettlist))
    
    for label in range (1,(length-2)):
        last = lettlist[label - 1]
        check = lettlist[label]
        if check == "W" and last == "B":
            if turn == 0:
                lettlist.pop(label - 1)
            elif turn == 1:
                lettlist.pop(label)
        elif check == "B" and last == "W":
            if turn == 0:
                lettlist.pop(label)
            elif turn == 1:
                lettlist.pop(label - 1)

    print(lettlist)

    length = (len(lettlist))

    print(length)

    for label in range(0,length):
        button = Label(win, text=str(lettlist[label]))
        button.bind("<Button-1>", buttonClicked)
        letters.append(button)
        button.grid(row=1, column=label) #creates all lettered buttons

        
    for label in range(0,length):
        button = Button(win, text=str(label))
        button.bind("<Button-1>", buttonClicked)
        numbers.append(button)
        button.grid(row=2, column=label) #creates all numbered buttons

enter = Button(win, text="GO!")
enter.bind("<Button-1>", goClicked)
enter.grid(row=2, column=15) #tells Go! button to run goClicked (re/set game)


#change letter buttons to labels
#if statement to consolidate trains
#if loop for randomized game
#messagebox for left/right turn, error messages, game rules, etc.





win.mainloop ()
