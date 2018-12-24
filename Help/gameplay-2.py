from turtle import*
from tkinter import messagebox
import turtle
import time
import os
import pickle

setup(width=1500,height=1500,startx=0,starty=0)

delay(3)
tracer(20)
bgcolor("pink")
up()

page=turtle.Turtle()
page.up()
page.goto(510,280)
page.write("2-/-4",True,align='left',font=("Domestic Manners",35,"bold"))
page.ht()

prt=turtle.Turtle()
prt.up()
prt.shapesize(3)
prt.goto(530,-300)


plt=turtle.Turtle()
plt.up()
plt.shapesize(3)
plt.goto(-510,-300)
plt.lt(180)



goto(-650,280)
write(" HELP",True,align='left',font=("Domestic Manners",35,"bold"))

goto(-640,220)
write("                       Game play",True,align='left',font=("Domestic Manners",35,"bold"))

goto(-640,160)
write("Players always move a token according to the die value rolled.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,110)
write("Passes are not allowed; if no move is possible, the turn moves to ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,60)
write("the next player.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,10)
write("When a 6 is rolled, the player may choose to advance a token already ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-40)
write("in play, or may enter another staged token to its starting square. ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-90)
write("Rolling a 6 earns the player an additional or bonus roll in that ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-140)
write("turn. If the bonus roll results in a 6 again, the player earns an ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-190)
write("additional bonus roll.",False,align='left',font=("Domestic Manners",27,"bold"))


def Pageturnright():
    bye()
    os.system("play Audio/misc_menu.mp3&")
    os.system("python3 Help/gameplay-3.py")
def Pageturnleft():
    bye()
    os.system("play Audio/misc_menu.mp3&")
    os.system("python3 Help/gameplay-1.py")
def Exit():
    bye()
    os.system("play Audio/misc_menu_4.mp3&") 
    os.system("python3 help.py")
    print("booM")
onkey(Pageturnleft,"Left")
onkey(Exit,"space")

listen()


onkey(Pageturnright,"Right")


goto(-430,-320)
write("Press Aroow keys to turn the page and space to exit",False,align='left',font=("Domestic Manners",24,"bold"))

ht()


mainloop()
done()

