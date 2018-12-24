
from turtle import*
from tkinter import messagebox
import turtle
import time
import os
import pickle

setup(width=1500,height=1500,startx=0,starty=0)

delay(3)
tracer(1)
bgcolor("pink")
up()

page=turtle.Turtle()
page.up()
page.goto(510,280)
page.write("1-/-2",True,align='left',font=("Domestic Manners",35,"bold"))
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
write("                       Rules",True,align='left',font=("Domestic Manners",35,"bold"))

goto(-640,160)
write("Two, three, or four can play, without partnerships.At the beginning of",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,110)
write("the game,each player's four tokens are out of play and staged ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,60)
write("in the player's yard [one of the large corner areas of the board in",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,10)
write("the player's colour]. When able to, the players will enter their ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-40)
write("tokens one per time on their respective starting squares, and ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-90)
write("proceed to race them clockwise around the board along the game ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-140)
write("track [the path of squares not part of any player's home column].",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-190)
write(" When reaching the square below his home column, a player continues by ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-240)
write("by moving tokens up the column to the finishing square. ",False,align='left',font=("Domestic Manners",27,"bold"))






def Pageturnright():
    bye()
    os.system("play Audio/misc_menu.mp3&")
    os.system("python3 Help/rules-2.py")
def Exit():
    bye()
    os.system("play Audio/misc_menu_4.mp3&")
    os.system("python3 help.py")
    print("booM")
onkey(Exit,"space")

onkey(Pageturnright,"Right")


listen()

goto(-430,-320)
write("Press Aroow keys to turn the page and space to exit",False,align='left',font=("Domestic Manners",24,"bold"))

ht()

mainloop()
done()
