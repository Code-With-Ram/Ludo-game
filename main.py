from turtle import*
from tkinter import messagebox
import turtle
import time
import os
import pickle
import sys
import pygame
pygame.init()
setup(width=1500,height=1500,startx=0,starty=0)

tracer(20)
bgcolor("pink")
home()
up()
goto(-650,280)
write(" MAINMENU",False,align='left',font=("Domestic Manners",32,"bold"))

color('black','violet')
pensize(3)
begin_fill()
#os.system("play Audio/bgmenu.mp3&")
music = pygame.mixer.music.load('Audio/bgmenu.mp3')
pygame.mixer.music.play(-1)

goto(-200,200)
down()
goto(200,200)
goto(200,-200)
goto(-200,-200)
goto(-200,200)
end_fill()
(x,y)=(200,200)
loadgame=False
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
write(" NEW  GAME  ",True,align="left",font=("Domestic Manners",25,"bold"))
y=y-80
goto(-x,y)
write("LOAD  GAME  ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)

write("  OPTIONS    ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)
write("    HELP   ",True,align="left",font=("Domestic Manners",25,"bold"))

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
    os.system("play Audio/misc_menu.mp3&")
    y=y+80
    if(y>200):
        y=-160
    lc.goto(-x,y)
    rc.goto(x,y)
    
def down():
    global x,y
    os.system("play Audio/misc_menu.mp3&")
    y=y-80
    if(y<-200):
        y=160
    lc.goto(-x,y)
    rc.goto(x,y)
def press():
    global x,y,loadgame
    os.system("play Audio/misc_menu_4.mp3&")
    if(y==160):
        print("NEW GAME")
        bye()
        pygame.mixer.music.fadeout(5000)
        os.system("python3 ludo.py")
        

    elif(y==80):
        print("LOAD GAME")
        loadgame=True
        pickle.dump(loadgame,open("Misc/loadgame.dat","wb"))
        bye()
        pygame.mixer.music.fadeout(5000)
        os.system("python3 ludo.py")


    elif(y==0):
        print("options")
        bye()
        os.system("python3 options.py")
        
    elif(y==-80):
        print("HELP")
        bye()
        os.system("python3 help.py")
    elif(y==-160):
        print("Exit")
        Exit=messagebox.askyesno("Quit","Do You Want To Quit?")
        if(Exit):
            pygame.mixer.music.fadeout(1000)
            bye()    
        
onkey(up,"Up")
onkey(down,"Down")
onkey(press,"Return")
listen()




mainloop()


