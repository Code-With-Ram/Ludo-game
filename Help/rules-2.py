
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
page.write("2-/-2",True,align='left',font=("Domestic Manners",35,"bold"))
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
write("requires a precise roll from the player.The first to bring all their",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,110)
write("tokens to the finish wins the game. The others often continue",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,60)
write(" play to determine second-, third-, and fourth-place finishers.",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,10)
write(" ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-40)
write("",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-90)
write("",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-140)
write("",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-190)
write(" ",False,align='left',font=("Domestic Manners",27,"bold"))

goto(-650,-240)
write("",False,align='left',font=("Domestic Manners",27,"bold"))







def Pageturnleft():
    bye()
    os.system("play Audio/misc_menu.mp3&")
    os.system("python3 Help/rules-1.py")

def Exit():
    bye()
    os.system("play Audio/misc_menu_4.mp3&") 
    os.system("python3 help.py")
    print("booM")
onkey(Pageturnleft,"Left")
onkey(Exit,"space")

listen()

goto(-430,-320)
write("Press Aroow keys to turn the page and space to exit",False,align='left',font=("Domestic Manners",24,"bold"))



mainloop()
done()
