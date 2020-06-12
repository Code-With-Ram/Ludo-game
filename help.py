


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

tracer(20)
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
write("ABOUT GAME ",True,align="left",font=("Domestic Manners",25,"bold"))
y=y-80
goto(-x,y)
write("   RULES  ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x,y)

write(" GAMEPLAY    ",True,align="left",font=("Domestic Manners",25,"bold"))

y=y-80
goto(-x-30,y)
write("MORE FEATURES   ",True,align="left",font=("Domestic Manners",25,"bold"))

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

player=0    
def press():
    global x,y,loadgame,player
    os.system("play Audio/misc_menu_4.mp3&")
    if(y==160):
        print("About")
        bye()
        os.system("python3 Help/about.py")
    elif(y==80):
        print("Rules")
        bye()
        os.system("python3 Help/rules-1.py")
    
    
    elif(y==0):
        print("Gameplay")
        bye()
        os.system("python3 Help/gameplay-1.py")
        
    elif(y==-80):
        print("More features")
        #bye()
        #os.system("python3 Help/morefeatures.py")
        
    elif(y==-160):
        print("Exit")
        pygame.mixer.music.stop()

        

        bye()
        os.system("python3 main.py")
        sys.exit()
                
onkey(up,"Up")
onkey(down,"Down")
onkey(press,"Return")
listen()



mainloop()

