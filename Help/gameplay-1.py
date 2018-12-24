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
page.write("1-/-4",True,align='left',font=("Domestic Manners",35,"bold"))
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
write("Each player rolls the die - the highest roller begins the game.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,110)
write("Players alternate turns in a clockwise direction.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,60)
write("To enter a token into play from its yard to its starting square, a ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,10)
write("player must roll a 6.If the player has no tokens yet in play",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-40)
write("and rolls other than a 6, the turn passes to the next player.Once a ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-90)
write("player has one or more tokens in play, he selects a token and moves",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-140)
write("it forwards along the track the number of squares indicated by the die.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-190)
write(" die.",False,align='left',font=("Domestic Manners",27,"bold"))



def Pageturnright():
    bye()
    os.system("play Audio/misc_menu.mp3&")
    os.system("python3 Help/gameplay-2.py")
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
