from turtle import*
from tkinter import messagebox
import turtle
import time
import os
import pickle

setup(width=1500,height=1500,startx=0,starty=0)

delay(3)

bgcolor("pink")
up()

goto(-650,280)
write(" HELP",True,align='left',font=("Domestic Manners",35,"bold"))

goto(-640,220)
write("                       About Game",True,align='left',font=("Domestic Manners",35,"bold"))

goto(-640,160)
write("   Ludo is A strategy board game for two to four players,in which",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,110)
write("the players race their four tokens from start to finish according",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,60)
write("to the rolls of a single die.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,10)
write("Each player is assigned a colour and has four tokens in their colour.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-60)
write("The board is  sqaure with a cross-shaped playspace,with each arm of ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-110)
write("the cross  having three columns of sqaures,usually six per coulmn.",False,align='left',font=("Domestic Manners",27,"bold"))




def Enter():
    bye()
    os.system("play Audio/misc_menu_4.mp3&")
    os.system("python3 help.py")
onkey(Enter,"space")
listen()

goto(-300,-300)
write(" Press  Space  To  Exit",False,align='left',font=("Domestic Manners",32,"bold"))



mainloop()
done()

