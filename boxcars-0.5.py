from Tkinter import *
win = Tk()
win.title('Boxcars')
import random
lettlist = ['W', 'O', 'B','O','W','O','B','O','W','O','B','O','W','O','B']
#random.shuffle(lettlist)
blackWin = 0
whiteWin = 0
turn = 0
bEnd = 0
wEnd = len(lettlist) - 1

def check(event):
   print (event.widget.cget("text"))
   listcount = int(event.widget.cget("text")) #finds number of button and sets equal to a variable
   if lettlist[listcount]=="W" and lettlist[listcount+1]=="B" or lettlist[listcount-1]=="B":
       random.shuffle(lettlist) #randomizes game setup
       
#check(lettlist) #this is not working yet




def buttonClicked(event):
   print (event.widget.cget("text"))  
   listcount = int(event.widget.cget("text")) #finds number of button and sets equal to a variable
   print(listcount)
   global turn
   global bEnd
   global wEnd
   if listcount == 0 and lettlist[listcount] == "B":
      print("error")
   elif listcount == bEnd and lettlist[bEnd] == "B":
      print("error")
   elif listcount == (len(lettlist)-1) and lettlist[listcount] == "W":
      print("error") #can't move at the end of the track
   elif listcount == wEnd and lettlist[wEnd] == "W":
      print("error")
   elif turn == 0 and lettlist[listcount] == "W":
      enter.config(state = 'normal')
      lettlist[listcount], lettlist[listcount + 1] = lettlist[listcount + 1], lettlist[listcount]
      turn = turn + 1
      return turn #moves for White (right one space)
   elif turn == 1 and lettlist[listcount] == "B":
      enter.config(state = 'normal')
      lettlist[listcount], lettlist[listcount - 1] = lettlist[listcount - 1], lettlist[listcount]
      turn = turn - 1
      return turn #moves for Black (left one space)
   else:
      print("error") #error message if O (space), or wrong color is clicked
   print(lettlist)

print(turn)

def goClicked(event):
   letters = []
   numbers = []
   global wEnd
   global bEnd
   global turn
   print(turn)
   length = (len(lettlist))
   for label in range (1,(length-1)):
      last = lettlist[label - 1]
      check = lettlist[label]
      if check == "B" and last == "W" and turn == 0:
         lettlist[label - 1] = "buffer"
         lettlist.remove("buffer")
         lettlist.append("X")
         wEnd = wEnd - 1
         #lettlist[label - 1], lettlist[0] = lettlist[0], lettlist[label - 1]
      elif check == "B" and last == "W" and turn == 1:
         lettlist[label] = "buffer"
         lettlist.remove("buffer")
         lettlist.insert(0, "X")
         bEnd = bEnd + 1
         #lettlist[label], lettlist[(len(lettlist)-1)] = lettlist[(len(lettlist)-1)], lettlist[label]
         #moves out conquered boxcars and puts them at the end of the track
   enter.config(state = 'disabled')


   print(lettlist)

   length = (len(lettlist))

   print(length)

   for label in range(0,length):
      button = Label(win, text=str(lettlist[label]), width = 10)
      button.bind("<Button-1>", buttonClicked)
      letters.append(button)
      button.grid(row=1, column=label) #creates all lettered buttons

        
   for label in range(0,length):
      button = Button(win, text=str(label), width = 10)
      button.bind("<Button-1>", buttonClicked)
      numbers.append(button)
      button.grid(row=2, column=label) #creates all numbered buttons

   #These are the victory condition checking lines
   blacktest = lettlist.count("W")
   whitetest = lettlist.count("B")
   if blacktest == 0:
       blackWin = 1
       print ("Black Wins!")
       blackwin = Label(win, text = "Black Wins!", width = 80, height = 30, font = ("Times New Roman", 25))
       blackwin.grid(row = 2, column = int(len(lettlist)/2))
   if whitetest == 0:
       whiteWin = 1
       print ("White Wins!")
       whitewin = Label(win, text = "White Wins!", width = 80, height = 30, font = ("Times New Roman", 25))
       whitewin.grid(row = 2, column = int(len(lettlist)/2))
   #Box for turn count:
   tlist = ["White", "Black"]
   player = tlist[turn]
   whoseturn = Label(win, text = player)
   whoseturn.grid(row = 3, column = int(len(lettlist)/2))
   
   



enter = Button(win, state = 'normal', text="GO!")
enter.bind("<Button-1>", goClicked)
enter.grid(row=2, column=15) #tells Go! button to run goClicked (re/set game)

#Infobox:
infolabels = []
info = ["White (W) moves to the right, Black (B) moves to the left.", \
        "Each turn, the player must select one of his pieces to move,", \
        "which will then move one space in their respective directions.", \
        "When a piece moves into a space next to a piece of the opposite color,", \
        "that piece will be deleted from the game."]
infocount = 3
"""frame =  TK.Frame()
frame.grid(row=3, column=int(len(lettlist)/2), columnspan=3, sticky='w')
"""
for label in range (0, len(info)):
   button = Label(win, text = str(info[label]))
   button.grid(row = (label) + 4, column = 0, columnspan = len(lettlist))
   infocount = infocount + 1
   infolabels.append(button)
#messagebox for left/right turn, error messages, game rules, etc.





win.mainloop ()
