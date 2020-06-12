from turtle import*
from tkinter import messagebox
import turtle
import time
import os
import pickle
import pygame
pygame.init()

setup(width=1500,height=1500,startx=0,starty=0)

tracer(20)
bgcolor("pink")
home()
up()
goto(-650,280)
write(" OPTIONS",False,align='left',font=("Domestic Manners",32,"bold"))

color('black','violet')
pensize(3)
begin_fill()
goto(-200,200)
down()
goto(200,200)
goto(200,-200)
goto(-200,-200)
goto(-200,200)
end_fill()
(x,y)=(200,200)
loadgame=False
mute=False
y=y-80
for i in range(4):
    goto(-x,y)
    fd(400)
    y=y-80
    goto(x,y)
    bk(400)
up()
(x,y)=(100,140)
goto(-x,y)
write("  2-PLAYER ",True,align="left",font=("Domestic Manners",25,"bold"))
y=y-80
goto(-x,y)
write("  3-PLAYER  ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)

write("  4-PLAYER    ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)
write(" MUTE SOUND   ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)

write("    EXIT   ",True,align="left",font=("Domestic Manners",25,"bold"))
tracer(1)
(x,y)=(200,160)
ht()
lc=turtle.Turtle()
rc=turtle.Turtle()
lc.shapesize(3)
rc.shapesize(3)
lc.up()
rc.up()
rc.right(180)
lc.goto(-x,y)
rc.goto(x,y)
lc.speed(8)
rc.speed(8)
def up():
    global x,y
    os.system("play misc_menu.mp3&")
    y=y+80
    if(y>200):
        y=-160
    lc.goto(-x,y)
    rc.goto(x,y)
    
def down():
    global x,y
    os.system("play misc_menu.mp3&")
    y=y-80
    if(y<-200):
        y=160
    lc.goto(-x,y)
    rc.goto(x,y)

player=0    
def press():
    global x,y,loadgame,player
    os.system("play misc_menu_4.mp3&")
    if(y==160):
        player=2
        pickle.dump(player,open("Misc/player.dat","wb"))
    elif(y==80):

        player=3
        pickle.dump(player,open("Misc/player.dat","wb"))
    
    
    elif(y==0):
        
        player=4
        pickle.dump(player,open("Misc/player.dat","wb"))
        
    elif(y==-80):
        #os.system("amixer set Master 0%")
        if not mute:
            pygame.mixer.music.set_volume(0.0)
        else:
            pygame.mixer.music.set_volume(1.0)
    elif(y==-160):
        bye()
        pygame.mixer.music.stop()
        os.system("python3 main.py")
                
onkey(up,"Up")
onkey(down,"Down")
onkey(press,"Return")
listen()



mainloop()

