lettlist = ['W', 'O', 'B','O','W','O','B','O','W']
viclist = []
for count in range(0, len(lettlist)):
    viclist.append(lettlist[count])

viclist.sort(key=str.lower)

print (viclist)

blackWin = 0
whiteWin = 0

if viclist.index(0) == "O":
    blackWin = 1
elif viclist.index(len.viclist) == "O":
    whiteWin = 1
