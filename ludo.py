#LUDO Game by RamKishor H




#importing modules
from turtle import*
from tkinter import*
from tkinter import messagebox
import math
import turtle
import random
import time
import os
import pickle

#setting up the background and title
setup(width=1500,height=1500,startx=0,starty=0)
bgcolor('pink')
title("LUDO GAME")


#loading game screen
#boom
up()
goto(-150,0)
write("LOADING ",True,align='left',font=("Domestic Manners",42,"bold"))
write(". ",True,align='left',font=("Domestic Manners",42,"bold"))
time.sleep(1/3)
for i in range(random.randint(1,4)):
    goto(150,0)
    write(" . ",True,align='left',font=("Domestic Manners",42,"bold"))
    time.sleep(1/3)
    write(". ",True,align='left',font=("Domestic Manners",42,"bold"))
    time.sleep(1/3)
    undo()
    undo()
    undo()


clear()




#LUDO Board

#create safezone
def safezone():   #circle
    for i in range(1):
        begin_fill()
        up()
        fd(10)
        rt(90)
        fd(18.5)
        down()
        color("black","orange")
        dot(15)
        up()
        bk(18.5)
        lt(90)
        down()

        color("black","pink")
        
        circle(-19)
        end_fill()

        up()
        bk(10)
        down()




#paths/blocks
def box():
    pensize(3)
    color("black","white")
    begin_fill()
    for i in range(4):
        fd(40)
        right(90)
    end_fill()    

def redbox():
    color("black","red")
    begin_fill()
    for i in range(4):
        fd(40)
        right(90)
    end_fill()    
def greenbox():
    pensize(4)
    color("black","green")
    begin_fill()
    for i in range(4):
        fd(40)
        right(90)
    end_fill()    
def yellowbox():
    color("black","yellow")
    begin_fill()
    for i in range(4):
        fd(40)
        right(90)
    end_fill()    
def bluebox():
    color("black","blue")
    begin_fill()
    for i in range(4):
        fd(40)
        right(90)
    end_fill()    

tracer(2)

#green boxes
up()
y=340
goto(20,y)
down()
pensize(2)       

for i in range(7):
    box()
    if (i==1):
        up()
        pencolor('black')
        right(180)
        goto(50,260+5/2-1.5)
        down()
        safezone()
        right(180)
        up()
        goto(20,y)
        down()
        
    y=y-40
    goto(20,y)


pensize(3)    
up()
y=340
goto(-20,y)
down()
for i in range(7):
    if(i==0):
        pensize(2)
        box()
        pensize(3)
    else:    
        greenbox()
    if(i!=0):
        up()
        goto(0,y-20+5/2-1)
        down()
        pencolor('black')
        pensize(1)
        dot(15)

    y=y-40
    up()
    goto(-20,y)
    down()
    #
    pensize(3)


pensize(2)
up()
y=340
goto(-60,60)
down()
goto(-60,y)
for i in range(7):
    box()

    if (i==2):
        up()
        pencolor('black')
        right(180)
        goto(-50+20,260+5/2-1.5-40)
        down()
        safezone()
        right(180)
        up()
        goto(-60,y)
        down()
        
    
    y=y-40
    goto(-60,y)
#end of green boxes


#yellow boxes

up()
x=340
goto(x,-20)
down()

pensize(2)       

right(90)
for i in range(7):
    box()

    if (i==1):
        up()
        pencolor('black')
        right(180)
        goto(260+5/2-1.6,-50)
        down()
        safezone()
        right(180)
        up()
        goto(x,-20)
        down()
        #
    
    x=x-40
    goto(x,-20)


pensize(3)    
up()
x=340
goto(x,20)
down()
for i in range(7):
    if(i==0):
        pensize(2)
        box()
        pensize(3)
    else:
        yellowbox()

    if(i!=0):
        up()
        goto(x-20+5/2-1,0)
        down()
        pencolor('black')
        pensize(1)
        dot(15)

    x=x-40
    up()
    goto(x,20)
    down()
    
    pensize(3)


pensize(2)

up()
x=340
goto(x,60)
down()
for i in range(7):
    box()

    if (i==2):
        up()
        pencolor('black')
        right(180)
        goto(260+5/2-1.6-40,-50+80)
        down()
        safezone()
        right(180)
        up()
        goto(x,60)
        down()
        
    
    
    x=x-40
    goto(x,60)

#end of yellow boxes



#blue boxes
left(90+90)
up()
y=-340
goto(20,y)
down()

pensize(2)       

for i in range(7):
    box()

    if (i==2):
        up()
        pencolor('black')
        right(90)
        goto((-50+30-0.1)+50,-(260-1.6+5/2)+40)
        down()
        safezone()
        right(180+90)
        up()
        goto(20,y)
        down()
        
    
    y=y+40
    goto(20,y)


pensize(3)    
up()
y=-340
goto(-20,y)
down()
for i in range(7):
    if(i==0):
        pensize(2)
        box()
        pensize(3)
    else:
        bluebox()

    if(i!=0):
        up()
        goto(5-5/2-1,y+20)
        down() 
        pencolor('black')
        pensize(1)
        dot(15)    
    y=y+40
    up()
    goto(-20,y)
    down()
    
    pensize(3)


pensize(2)

up()
y=-340
goto(-60,y)
down()
for i in range(7):
    box()


    if (i==1):
        up()
        pencolor('black')
        right(90)
        goto((-50+30+0.2)-30,-(260-1.5+5/2))
        down()
        safezone()
        right(180+90)
        up()
        goto(-60,y)
        down()
            
    y=y+40
    goto(-60,y)

   
#end of blue boxes


#red boxes

up()
x=-340
goto(x,-20)
down()

pensize(2)       

right(90)
for i in range(7):
    box()
    
    if (i==2):
        up()
        pencolor('black')
        right(90)
        goto(-(260+5/2-1.5-40),-(50+80)+100)
        down()
        safezone()
        right(180+90)
        up()
        goto(x,-20)
        down()
            
    
    x=x+40
    goto(x,-20)

pensize(3)    
up()
x=-340
goto(x,20)
down()

for i in range(7):
    if(i==0):
        pensize(2)
        box()
        pensize(3)
    else:
        redbox()

    if(i!=0):
        up()
        goto(x+20,-5+5/2+1)
        down()
        pencolor('black')
        pensize(1)
        dot(15)    
    x=x+40
    up()
    goto(x,20)
    down()
    
    pensize(3)

left(90)
pensize(2)

up()
x=-340
goto(x,20)
down()
for i in range(7):
    box()

    if (i==1):
        up()
        pencolor('black')
        right(180)
        goto(-(260+5/2-1.5),-(50+80)+180)
        down()
        safezone()
        right(180)
        up()
        goto(x,20)
        down()
            
    x=x+40
    goto(x,20)

#end of red boxes

tracer(2)
#birth boxes
#delay(30)

def birthbox():
    color("black","white")
    
    begin_fill()    
    for i in range(4):
        
        fd(140)
        bk(55)    #original bk(70)

        rt(90)
        up()
        fd(35)
        down()

        
        circle(20)
        


        up()
        bk(35)
        down()
        lt(90)

        bk(15)
        
        right(90)

        fd(140)
        bk(140)
        left(90)
        fd(70)     
        right(90)
    end_fill()   
        
        
'''        #if(i==0):
            fd(70)
            lt(90)
            up()
            fd(40)
            down()
            circle(20)
            up()
            bk(40)
            rt(90)
            down()
'''           

pensize(3)
up()
goto(140,140)
down()


birthbox()

    
up()
goto(140,-140-200+60)
down()
birthbox()


up()
goto(-140-200+60,-140-200+60)
down()
birthbox()


up()
goto(-140-200+60,140)
down()
birthbox()


#extra centrebox


up()
goto(60,60)
down()
right(90+90)
def triangle():
    pensize(4)
    begin_fill()
    fd(120)
    right(45+90)
    t=((math.sqrt(2))*120)/2
    fd(t)
    right(90)
    fd(t)
    end_fill()
color('black','yellow')
triangle()

color('black','blue')
up()
right(45+180)
goto(60,-60)
down()
triangle()

color('black','red')
up()
left(45+90)
goto(-60,-60)
down()
triangle()

color('black','green')
up()
left(45+90)
goto(-60,60)
down()
triangle()

right(45)

#title "LUDO" drawing
up()
goto(-680,180+120)
down()
right(180)
fd(120)
left(90)
fd(60)

up()
fd(20)
down()
right(90)
bk(120)
fd(120)
left(90)
fd(60)
left(90)
fd(120)
bk(120)
right(90)

up()
fd(40)
down()
left(90)
fd(120)
right(90)
circle(-60,180)
right(180)

up()
fd(70)
down()
for i in range(4):
    if(i==0 or i==2):
        fd(60)
    else:
        fd(120)
    left(90)    
#end of title


#end of LUDO Board......
    
delay(10)







#The main logic
    
'''Here we make use of 16 turtles as keys representing position of each keys of
each players at a time....this is becoz it is very efficient to use due to its
wide functions ....especially shape!!!!!!!!'''

'''we use first letter of color and its number as turtle name
for example in green
                    g1=green one......g4=green four
simillarly for other players
'''


#declaration of 16 turtles and their specifications
g1=turtle.Turtle()
g1.shape("circle")
g1.shapesize(3/2)
g1.color("black","green")
g1.up()
g1.goto(140+35,140+105)


g2=turtle.Turtle()
g2.shape("circle")
g2.shapesize(3/2)
g2.color("black","green")
g2.up()
g2.goto(140+70+35,140+105)

g3=turtle.Turtle()
g3.shape("circle")
g3.shapesize(3/2)
g3.color("black","green")
g3.up()
g3.goto(140+35,140+35)

g4=turtle.Turtle()
g4.shape("circle")
g4.shapesize(3/2)
g4.color("black","green")
g4.up()
g4.goto(140+105,140+35)

b1=turtle.Turtle()
b1.shape("circle")
b1.shapesize(3/2)
b1.color("black","blue")
b1.up()
b1.goto(-280+35,-280+105)

b2=turtle.Turtle()
b2.shape("circle")
b2.shapesize(3/2)
b2.color("black","blue")
b2.up()
b2.goto(-280+105,-280+105)


b3=turtle.Turtle()
b3.shape("circle")
b3.shapesize(3/2)
b3.color("black","blue")
b3.up()
b3.goto(-280+105,-280+35)


b4=turtle.Turtle()
b4.shape("circle")
b4.shapesize(3/2)
b4.color("black","blue")
b4.up()
b4.goto(-280+35,-280+35)


y1=turtle.Turtle()
y1.shape("circle")
y1.shapesize(3/2)
y1.color("black","yellow")
y1.up()
y1.goto(140+35,-280+105)

y2=turtle.Turtle()
y2.shape("circle")
y2.shapesize(3/2)
y2.color("black","yellow")
y2.up()
y2.goto(140+105,-280+105)

y3=turtle.Turtle()
y3.shape("circle")
y3.shapesize(3/2)
y3.color("black","yellow")
y3.up()
y3.goto(140+35,-280+35)

y4=turtle.Turtle()
y4.shape("circle")
y4.shapesize(3/2)
y4.color("black","yellow")
y4.up()
y4.goto(140+105,-280+35)

r1=turtle.Turtle()
r1.shape("circle")
r1.shapesize(3/2)
r1.color("black","red")
r1.up()
r1.goto(-280+35,140+105)

r2=turtle.Turtle()
r2.shape("circle")
r2.shapesize(3/2)
r2.color("black","red")
r2.up()
r2.goto(-280+105,140+105)

r3=turtle.Turtle()
r3.shape("circle")
r3.shapesize(3/2)
r3.color("black","red")
r3.up()
r3.goto(-280+35,140+35)

r4=turtle.Turtle()
r4.shape("circle")
r4.shapesize(3/2)
r4.color("black","red")
r4.up()
r4.goto(-280+105,140+35)

#end of 16 turtles keys declarations 

#turtles for  waiting and dice
'''Here we make use of 2 turtles wait and d(dice)
wait->This is to make animation of roatating rectangle while player chooses the key to move
dice->This is to show the dice in picture format
'''


#wait specifications
wait=turtle.Turtle()
wait.shapesize(2)
wait.up()
wait.goto(480,-200)


'''for pendowns of keys

g1.down()
g2.down()
g3.down()
g4.down()

b1.down()
b2.down()
b3.down()
b4.down()

y1.down()
y2.down()
y3.down()
y4.down()

r1.down()
r2.down()
r3.down()
r4.down()
'''
'''shapes of keys'''


'''Functions related to turns of players'''
#postions of keys
global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
(r1x,r1y)=(-280+35,140+105)
(r2x,r2y)=(-280+105,140+105)
(r3x,r3y)=(-280+35,140+35)
(r4x,r4y)=(-280+105,140+35)
give_birth_red=True

(y1x,y1y)=(140+35,-280+105)
(y2x,y2y)=(140+105,-280+105)
(y3x,y3y)=(140+35,-280+35)
(y4x,y4y)=(140+105,-280+35)
give_birth_yellow=True

g1x=175
g1y=245    
g2x=245
g2y=245
g3x=175
g3y=175
g4x=245
g4y=175
give_birth_green=True
    
b1x=-245
b1y=-175   
b2x=-175
b2y=-175
b3x=-245
b3y=-245
b4x=-175
b4y=-245
give_birth_blue=True
#end of postions of keys

#winning variables
global red_won,green_won,yellow_won,blue_won
red_won=False
green_won=False
yellow_won=False
blue_won=False




#sensitive and turning points positons
global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
global endredx,endredy,endgreenx,endgreeny,endyellowx,endyellowy,endbluex,endbluey
global redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted
(redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted)=(False,False,False,False)
(red1x,red1y)=(-(320),40)
(red2x,red2y)=(-(320),-40)
(blue2x,blue2y)=(40,-(320))
(blue1x,blue1y)=(-40,-(320))
(green1x,green1y)=(40,(320))
(green2x,green2y)=(-40,(320))
(yellow2x,yellow2y)=((320),40)
(yellow1x,yellow1y)=((320),-40)


(senred1x,senred1y)=(-80,40)
(senred2x,senred2y)=(-80,-40)
(sengreen1x,sengreen1y)=(40,80)
(sengreen2x,sengreen2y)=(-40,80)
(senblue1x,senblue1y)=(-40,-80)
(senblue2x,senblue2y)=(40,-80)
(senyellow1x,senyellow1y)=(80,-40)
(senyellow2x,senyellow2y)=(80,40)

(endredx,endredy)=(-(320),0)
(endgreenx,endgreeny)=(0,(320))
(endyellowx,endyellowy)=((320),0)
(endbluex,endbluey)=(0,-(320))

#end of sensitive and turning points


#safe zones
global safered1x,safered1y,safegreen1x,safegreen1y,safeyellow1x,safeyellow1y,safeblue1x,safeblue1y
global safered2x,safered2y,safegreen2x,safegreen2y,safeyellow2x,safeyellow2y,safeblue2x,safeblue2y,can_clash
can_clash=False


(safered1x,safered1y)=(-280,40)
(safegreen1x,safegreen1y)=(40,280)
(safeyellow1x,safeyellow1y)=(yellow1x-40,yellow1y)
(safeblue1x,safeblue1y)=(-40,-280)


(safered2x,safered2y)=(red2x+80,red2y)
(safegreen2x,safegreen2y)=(green2x,green2y-80)
(safeyellow2x,safeyellow2y)=(yellow2x-80,yellow2y)
(safeblue2x,safeblue2y)=(blue2x,blue2y+80)


loadgame=True
#If user wants to load the previous game
loadgame=pickle.load(open("Misc/loadgame.dat","rb"))
if(loadgame):
   loadgame=False
   pickle.dump(loadgame,open("Misc/loadgame.dat","wb"))

   r1x=pickle.load(open("Save/r1x.dat","rb"))
   r1y=pickle.load(open("Save/r1y.dat","rb"))
   r2x=pickle.load(open("Save/r2x.dat","rb"))
   r2y=pickle.load(open("Save/r2y.dat","rb"))
   r3x=pickle.load(open("Save/r3x.dat","rb"))
   r3y=pickle.load(open("Save/r3y.dat","rb"))
   r4x=pickle.load(open("Save/r4x.dat","rb"))
   r4y=pickle.load(open("Save/r4y.dat","rb"))
   
   y1x=pickle.load(open("Save/y1x.dat","rb"))
   y1y=pickle.load(open("Save/y1y.dat","rb"))
   y2x=pickle.load(open("Save/y2x.dat","rb"))
   y2y=pickle.load(open("Save/y2y.dat","rb"))
   y3x=pickle.load(open("Save/y3x.dat","rb"))
   y3y=pickle.load(open("Save/y3y.dat","rb"))
   y4x=pickle.load(open("Save/y4x.dat","rb"))
   y4y=pickle.load(open("Save/y4y.dat","rb"))

   b1x=pickle.load(open("Save/b1x.dat","rb"))
   b1y=pickle.load(open("Save/b1y.dat","rb"))
   b2x=pickle.load(open("Save/b2x.dat","rb"))
   b2y=pickle.load(open("Save/b2y.dat","rb"))
   b3x=pickle.load(open("Save/b3x.dat","rb"))
   b3y=pickle.load(open("Save/b3y.dat","rb"))
   b4x=pickle.load(open("Save/b4x.dat","rb"))
   b4y=pickle.load(open("Save/b4y.dat","rb"))
   
   g1x=pickle.load(open("Save/g1x.dat","rb"))
   g1y=pickle.load(open("Save/g1y.dat","rb"))
   g2x=pickle.load(open("Save/g2x.dat","rb"))
   g2y=pickle.load(open("Save/g2y.dat","rb"))
   g3x=pickle.load(open("Save/g3x.dat","rb"))
   g3y=pickle.load(open("Save/g3y.dat","rb"))
   g4x=pickle.load(open("Save/g4x.dat","rb"))
   g4y=pickle.load(open("Save/g4y.dat","rb"))
   tracer(1)
   r1.goto(r1x,r1y)
   r2.goto(r2x,r2y)
   r3.goto(r3x,r3y)
   r4.goto(r4x,r4y)

   b1.goto(b1x,b1y)
   b2.goto(b2x,b2y)
   b3.goto(b3x,b3y)
   b4.goto(b4x,b4y)

   g1.goto(g1x,g1y)
   g2.goto(g2x,g2y)
   g3.goto(g3x,g3y)
   g4.goto(g4x,g4y)

   y1.goto(y1x,y1y)
   y2.goto(y2x,y2y)
   y3.goto(y3x,y3y)
   y4.goto(y4x,y4y)

    
   print("loaded")
   tracer(2)




#To check whether all keys are at their starting positions
def check_red_start_pos():
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    if((r1x!=-280+35) and (r1y!=140+105)):
        return False    
    if((r2x!=-280+105) and (r2y!=140+105)):
        return False
    if((r3x!=-280+35) and (r3y!=140+35)):
        return False
    if(r4x!=-280+105 and (r4y!=140+35)):
        return False

    return True

def check_green_start_pos():
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    if((g1x!=175) and (g1y!=245)):
        return False    
    if((g2x!=245) and (g2y!=245)):
        return False
    if((g3x!=175) and (g3y!=175)):
        return False
    if(g4x!=245 and (g4y!=175)):
        return False
    return True
all_blue_start_pos=True

def check_blue_start_pos():
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    if((b1x!=-245) and (b1y!=-175)):
        return False    
    if((b2x!=-175) and (b2y!=-175)):
        return False
    if((b3x!=-245) and (b3y!=-245)):
        return False
    if(b4x!=-175 and (b4y!=-245)):
        return False
    return True

def check_yellow_start_pos():
    if((y1x,y1y)!=(140+35,-280+105)):
        return False
    if((y2x,y2y)!=(140+105,-280+105)):
        return False
    if((y3x,y3y)!=(140+35,-280+35)):
        return False
    if((y4x,y4y)!=(140+105,-280+35)):
        return False
    return True
all_yellow_start_pos=True
#End of checking starting positions

#binding functions

def key1(x,y):
    global moving_key
    moving_key=1
def key2(x,y):
    global moving_key
    moving_key=2
def key3(x,y):
    global moving_key
    moving_key=3
def key4(x,y):
    global moving_key
    moving_key=4


#dice turtle and its specifications
d=turtle.Turtle()
tracer(2)
delay(8)
up()
goto(-280-35-100,-280+35)
down()

right(90+90)


color("black","white")
begin_fill()
for i in range(4):
    fd(200)
    right(90)
end_fill()


up()
d.screen.delay(1)
goto(-280-35-300,-280+35+165)
right(180)
down()
fd(40)
write("     DICE     ",True,align="left",font=("Times new roman",18,"bold"))
fd(40)
up()
goto(-555,-110)
down()
for i in range(4):
    fd(80)
    right(90)



show_turn=turtle.Turtle()
show_turn.pensize(4)

#for showing turns
def  show_red_turn():
    show_turn.screen.tracer(2)
    show_turn.screen.delay(4)
    show_turn.up()
    show_turn.goto(-280-35-100,-280+35)
    show_turn.down()

    show_turn.right(90+90)

    
    show_turn.up()
    show_turn.goto(-280-35-300,-280+35+165)

    show_turn.right(180)

    show_turn.color("black","red")
    show_turn.begin_fill()

    
    show_turn.down()
    show_turn.fd(40)
    show_turn.write("     DICE     ",True,align="left",font=("Times new roman",18,"bold"))
    show_turn.fd(40)
    
    for i in range(4):
        show_turn.rt(90)
        if(i==0 or i==2):
            show_turn.fd(130)
        else:
            show_turn.fd(197)
    show_turn.end_fill()
    show_turn.up()
    show_turn.goto(-555,-110)
    show_turn.down()

    show_turn.color("black","white")
    show_turn.begin_fill()

    for i in range(4):
        show_turn.fd(80)
        show_turn.right(90)

    show_turn.end_fill()

    

def show_green_turn():
    show_turn.screen.tracer(2)
    show_turn.screen.delay(4)
    show_turn.up()
    show_turn.goto(-280-35-100,-280+35)
    show_turn.down()

    show_turn.right(90+90)

    
    show_turn.up()
    show_turn.goto(-280-35-300,-280+35+165)

    show_turn.right(180)

    show_turn.color("black","green")
    show_turn.begin_fill()

    
    show_turn.down()
    show_turn.fd(40)
    show_turn.write("     DICE     ",True,align="left",font=("Times new roman",18,"bold"))
    show_turn.fd(40)
    
    for i in range(4):
        show_turn.rt(90)
        if(i==0 or i==2):
            show_turn.fd(130)
        else:
            show_turn.fd(197)
    show_turn.end_fill()
    show_turn.up()
    show_turn.goto(-555,-110)
    show_turn.down()

    show_turn.color("black","white")
    show_turn.begin_fill()

    for i in range(4):
        show_turn.fd(80)
        show_turn.right(90)

    show_turn.end_fill()









def  show_yellow_turn():
    show_turn.screen.tracer(2)
    show_turn.screen.delay(4)
    show_turn.up()
    show_turn.goto(-280-35-100,-280+35)
    show_turn.down()

    show_turn.right(90+90)

    
    show_turn.up()
    show_turn.goto(-280-35-300,-280+35+165)

    show_turn.right(180)

    show_turn.color("black","yellow")
    show_turn.begin_fill()

    
    show_turn.down()
    show_turn.fd(40)
    show_turn.write("     DICE     ",True,align="left",font=("Times new roman",18,"bold"))
    show_turn.fd(40)
    
    for i in range(4):
        show_turn.rt(90)
        if(i==0 or i==2):
            show_turn.fd(130)
        else:
            show_turn.fd(197)
    show_turn.end_fill()
    show_turn.up()
    show_turn.goto(-555,-110)
    show_turn.down()

    show_turn.color("black","white")
    show_turn.begin_fill()

    for i in range(4):
        show_turn.fd(80)
        show_turn.right(90)

    show_turn.end_fill()









def  show_blue_turn():
    show_turn.screen.tracer(2)
    show_turn.screen.delay(4)
    show_turn.up()
    show_turn.goto(-280-35-100,-280+35)
    show_turn.down()

    show_turn.right(90+90)

    
    show_turn.up()
    show_turn.goto(-280-35-300,-280+35+165)

    show_turn.right(180)

    show_turn.color("black","blue")
    show_turn.begin_fill()

    
    show_turn.down()
    show_turn.fd(40)
    show_turn.write("     DICE     ",True,align="left",font=("Times new roman",18,"bold"))
    show_turn.fd(40)
    
    for i in range(4):
        show_turn.rt(90)
        if(i==0 or i==2):
            show_turn.fd(130)
        else:
            show_turn.fd(197)
    show_turn.end_fill()
    show_turn.up()
    show_turn.goto(-555,-110)
    show_turn.down()

    show_turn.color("black","white")
    show_turn.begin_fill()

    for i in range(4):
        show_turn.fd(80)
        show_turn.right(90)

    show_turn.end_fill()


show_turn.ht()



def roll_dice():
    
    time.sleep(1/2)
    os.system("play Audio/Roll.wav&")
    
    dice=random.randint(1,6)
    #dice=6
        
    return dice

#d.hideturtle()



    
def show_dice(dice):    
    if(dice==1):
        d.up()
        d.goto(-555+40,-110-40)
        d.down()
        d.dot(15)
    elif(dice==2):
        d.up()
        d.goto(-555+30,-110-40)
        d.down()
        d.dot(15)
        d.up()
        d.fd(20)
        d.down()
        d.dot(15)
    elif(dice==3):
        d.up()
        d.goto(-555+20,-110-40)
        d.down()
        d.dot(15)
        d.up()
        d.fd(20)
        d.down()
        d.dot(15)
        d.up()
        d.fd(20)
        d.down()
        d.dot(15)
    elif(dice==4):
        d.up()
        d.goto(-555+20,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+60,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+60,-110-60)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+20,-110-60)
        d.down()
        d.dot(15)
    elif(dice==5):
        d.up()
        d.goto(-555+20,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+60,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+60,-110-60)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+20,-110-60)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+40,-110-40)
        d.down()
        d.dot(15)
    elif(dice==6):
        d.up()
        d.goto(-555+25,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+25,-110-40)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+25,-110-60)
        d.down()
        d.dot(15)
    
        d.up()
        d.goto(-555+30+25,-110-20)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+30+25,-110-40)
        d.down()
        d.dot(15)
        d.up()
        d.goto(-555+30+25,-110-60)
        d.down()
        d.dot(15)
    

up()
goto(-280-35-300,-280+35+35)
down()
fd(200)
up()
goto(-280-35-300,-280+35)
down()
fd(200)

#turtles for save game,pause game,resume game,Quit
save=turtle.Turtle()
save.shape('circle')
save.shapesize(2)
save.color('black','orange')
save.up()
save.goto(380,210)
save.write("  SAVE  GAME                  ",False,align='left',font=("Times new roman",22,"bold"))
save.goto(380+265,227)
def sav(x,y):
   os.system("play Audio/misc_menu_4.mp3&")
   os.system("clear")
   if(messagebox.askyesno("Save","Do you want to save Progress")):
       os.system("play Audio/misc_menu_4.mp3&")
       pickle.dump(r1x,open("Save/r1x.dat","wb"))
       pickle.dump(r1y,open("Save/r1y.dat","wb"))
       pickle.dump(r2x,open("Save/r2x.dat","wb"))
       pickle.dump(r2y,open("Save/r2y.dat","wb"))
       pickle.dump(r3x,open("Save/r3x.dat","wb"))
       pickle.dump(r3y,open("Save/r3y.dat","wb"))
       pickle.dump(r4x,open("Save/r4x.dat","wb"))
       pickle.dump(r4y,open("Save/r4y.dat","wb"))
       
       pickle.dump(y1x,open("Save/y1x.dat","wb"))
       pickle.dump(y1y,open("Save/y1y.dat","wb"))
       pickle.dump(y2x,open("Save/y2x.dat","wb"))
       pickle.dump(y2y,open("Save/y2y.dat","wb"))
       pickle.dump(y3x,open("Save/y3x.dat","wb"))
       pickle.dump(y3y,open("Save/y3y.dat","wb"))
       pickle.dump(y4x,open("Save/y4x.dat","wb"))
       pickle.dump(y4y,open("Save/y4y.dat","wb"))

       pickle.dump(b1x,open("Save/b1x.dat","wb"))
       pickle.dump(b1y,open("Save/b1y.dat","wb"))
       pickle.dump(b2x,open("Save/b2x.dat","wb"))
       pickle.dump(b2y,open("Save/b2y.dat","wb"))
       pickle.dump(b3x,open("Save/b3x.dat","wb"))
       pickle.dump(b3y,open("Save/b3y.dat","wb"))
       pickle.dump(b4x,open("Save/b4x.dat","wb"))
       pickle.dump(b4y,open("Save/b4y.dat","wb"))
       
       pickle.dump(g1x,open("Save/g1x.dat","wb"))
       pickle.dump(g1y,open("Save/g1y.dat","wb"))
       pickle.dump(g2x,open("Save/g2x.dat","wb"))
       pickle.dump(g2y,open("Save/g2y.dat","wb"))
       pickle.dump(g3x,open("Save/g3x.dat","wb"))
       pickle.dump(g3y,open("Save/g3y.dat","wb"))
       pickle.dump(g4x,open("Save/g4x.dat","wb"))
       pickle.dump(g4y,open("Save/g4y.dat","wb"))

       print("Saved")

   else:
       os.system("play Audio/misc_menu.mp3&")
  
save.onclick(sav)



#decision of max players
maxplace=0
player=pickle.load(open("Misc/player.dat","rb"))
if(player==2):
     maxplace=2
     b1.ht()
     b2.ht()
     b3.ht()
     b4.ht()
     y1.ht()
     y2.ht()
     y3.ht()
     y4.ht()
     blue_won=True
     yellow_won=True
elif(player==3):
     b1.ht()
     b2.ht()
     b3.ht()
     b4.ht()
     blue_won=True
     maxplace=3
elif(player==4):
     maxplace=4


pickle.dump(maxplace,open("Misc/maxplace.dat","wb"))



pause=turtle.Turtle()
pause.shape('circle')
pause.shapesize(2)
pause.color('black','indigo')
pause.up()
pause.goto(380,160)
pause.write("  PAUSE  GAME                ",False,align='left',font=("Times new roman",22,"bold"))
pause.goto(380+265,180)
def paus(x,y):
    os.system("play Audio/misc_menu_4.mp3&")
    messagebox.showinfo("Pause","Game Paused.\nClick ok to Resume")
    os.system("play Audio/misc_menu_4.mp3&")

pause.onclick(paus)


Quit=turtle.Turtle()
Quit.shape('circle')
Quit.shapesize(2)
Quit.color('black','white')
Quit.up()
Quit.goto(380,110)
Quit.write("  QUIT  GAME     ",False,align='left',font=("Times new roman",22,"bold"))
Quit.goto(380+265,130)
def escape(x,y):
    os.system("play Audio/misc_menu_4.mp3&")
    if(messagebox.askyesno("Quit","Do you want to quit game?")):
        os.system("play Audio/misc_menu_4.mp3&")
        bye()
        os.system("python3 main.py")
    else:
        os.system("play Audio/misc_menu.mp3&")

Quit.onclick(escape)
listen()








#commond turtle used to give info what to do
ht()
com=turtle.Turtle()
com.pensize(3)
com.up()
com.goto(380,-340)
com.down()
com.goto(380,340)

com.goto(380,-80)
com.goto(680,-80)
com.up()
com.goto(380,-160)
com.down()
com.fd(300)
com.up()
com.goto(380,-120)


#turn turtle is used to display whos turn is now
turn=turtle.Turtle()
turn.up()
turn.ht()





gameover=False




global dice,rem
rem=0
moving_key=0
place=0
redplace=0
greenplace=0
yellowplace=0
blueplace=0
#To check the players won or not 
def check_red_won():
    global red_won,place,redplace
    if(not(r1.isvisible()) and not(r2.isvisible()) and not(r3.isvisible()) and not(r4.isvisible())):
        print("redwon")
        red_won=True
        if(place==0):
            redplace=1
        elif(place==1):
            redplace=2
        elif(place==2):
            redplace=3
        place+=1
            
        messagebox.showinfo("Win","Red has won")

def check_green_won():
    global green_won,place,greenplace
    if(not(g1.isvisible()) and not(g2.isvisible()) and not(g3.isvisible()) and not(g4.isvisible())):
        print("greenwon")
        green_won=True
        if(place==0):
            greenplace=1
        elif(place==1):
            greenplace=2
        elif(place==2):
            greenplace=3
        place+=1
        
        messagebox.showinfo("Win","Green has won")
        
        
def check_blue_won():
    global blue_won,place,blueplace
    if(not(b1.isvisible()) and not(b2.isvisible()) and not(b3.isvisible()) and not(b4.isvisible())):
        print("bluewon")
        blue_won=True
        if(place==0):
            blueplace=1
        elif(place==1):
            blueplace=2
        elif(place==2):
            blueplace=3
        place+=1
        
        messagebox.showinfo("Win","Blue has won")
        
def check_yellow_won():
    global yellow_won,place,yellowplace
    if(not(y1.isvisible()) and not(y2.isvisible()) and not(y3.isvisible()) and not(y4.isvisible())):
        print("yellowwon")
        yellow_won=True
        if(place==0):
            yellowplace=1
        elif(place==1):
            yellowplace=2
        elif(place==2):
            yellowplace=3
        place+=1
        
        messagebox.showinfo("Win","Yellow has won")


        
def clash_beep():
      global re_roll
      os.system("play Audio/negative2.wav&")
      re_roll=True


def can_clash_red():
    global safered1x,safered1y,safegreen1x,safegreen1y,safeyellow1x,safeyellow1y,safeblue1x,safeblue1y
    global safered2x,safered2y,safegreen2x,safegreen2y,safeyellow2x,safeyellow2y,safeblue2x,safeblue2y,can_clash
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y

    if(moving_key==1):
        if((r1x,r1y)==(safered1x,safered1y) or (r1x,r1y)==(safegreen1x,safegreen1y) or (r1x,r1y)==(safeyellow1x,safeyellow1y) or (r1x,r1y)==(safeblue1x,safeblue1y) or (r1x,r1y)==(safered2x,safered2y) or (r1x,r1y)==(safegreen2x,safegreen2y) or (r1x,r1y)==(safeyellow2x,safeyellow2y) or (r1x,r1y)==(safeblue2x,safeblue2y)):
            return False    
    
    if(moving_key==2):
        if((r2x,r2y)==(safered1x,safered1y) or (r2x,r2y)==(safegreen1x,safegreen1y) or (r2x,r2y)==(safeyellow1x,safeyellow1y) or (r2x,r2y)==(safeblue1x,safeblue1y) or (r2x,r2y)==(safered2x,safered2y) or (r2x,r2y)==(safegreen2x,safegreen2y) or (r2x,r2y)==(safeyellow2x,safeyellow2y) or (r2x,r2y)==(safeblue2x,safeblue2y)):
            return False       

    if(moving_key==3):
        if((r3x,r3y)==(safered1x,safered1y) or (r3x,r3y)==(safegreen1x,safegreen1y) or (r3x,r3y)==(safeyellow1x,safeyellow1y) or (r3x,r3y)==(safeblue1x,safeblue1y) or (r3x,r3y)==(safered2x,safered2y) or (r3x,r3y)==(safegreen2x,safegreen2y) or (r3x,r3y)==(safeyellow2x,safeyellow2y) or (r3x,r3y)==(safeblue2x,safeblue2y)):
            return False   

    if(moving_key==4):
        if((r4x,r4y)==(safered1x,safered1y) or (r4x,r4y)==(safegreen1x,safegreen1y) or (r4x,r4y)==(safeyellow1x,safeyellow1y) or (r4x,r4y)==(safeblue1x,safeblue1y) or (r4x,r4y)==(safered2x,safered2y) or (r4x,r4y)==(safegreen2x,safegreen2y) or (r4x,r4y)==(safeyellow2x,safeyellow2y) or (r4x,r4y)==(safeblue2x,safeblue2y)):
            return False

    return True    

def can_clash_green():
    global safered1x,safered1y,safegreen1x,safegreen1y,safeyellow1x,safeyellow1y,safeblue1x,safeblue1y
    global safered2x,safered2y,safegreen2x,safegreen2y,safeyellow2x,safeyellow2y,safeblue2x,safeblue2y,can_clash
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y

    if(moving_key==1):
        if((g1x,g1y)==(safered1x,safered1y) or (g1x,g1y)==(safegreen1x,safegreen1y) or (g1x,g1y)==(safeyellow1x,safeyellow1y) or (g1x,g1y)==(safeblue1x,safeblue1y) or (g1x,g1y)==(safered2x,safered2y) or (g1x,g1y)==(safegreen2x,safegreen2y) or (g1x,g1y)==(safeyellow2x,safeyellow2y) or (g1x,g1y)==(safeblue2x,safeblue2y)):
            return False    
    
    if(moving_key==2):
        if((g2x,g2y)==(safered1x,safered1y) or (g2x,g2y)==(safegreen1x,safegreen1y) or (g2x,g2y)==(safeyellow1x,safeyellow1y) or (g2x,g2y)==(safeblue1x,safeblue1y) or (g2x,g2y)==(safered2x,safered2y) or (g2x,g2y)==(safegreen2x,safegreen2y) or (g2x,g2y)==(safeyellow2x,safeyellow2y) or (g2x,g2y)==(safeblue2x,safeblue2y)):
            return False       

    if(moving_key==3):
        if((g3x,g3y)==(safered1x,safered1y) or (g3x,g3y)==(safegreen1x,safegreen1y) or (g3x,g3y)==(safeyellow1x,safeyellow1y) or (g3x,g3y)==(safeblue1x,safeblue1y) or (g3x,g3y)==(safered2x,safered2y) or (g3x,g3y)==(safegreen2x,safegreen2y) or (g3x,g3y)==(safeyellow2x,safeyellow2y) or (g3x,g3y)==(safeblue2x,safeblue2y)):
            return False   

    if(moving_key==4):
        if((g4x,g4y)==(safered1x,safered1y) or (g4x,g4y)==(safegreen1x,safegreen1y) or (g4x,g4y)==(safeyellow1x,safeyellow1y) or (g4x,g4y)==(safeblue1x,safeblue1y) or (g4x,g4y)==(safered2x,safered2y) or (g4x,g4y)==(safegreen2x,safegreen2y) or (g4x,g4y)==(safeyellow2x,safeyellow2y) or (g4x,g4y)==(safeblue2x,safeblue2y)):
            return False

    return True    

def can_clash_yellow():
    global safered1x,safered1y,safegreen1x,safegreen1y,safeyellow1x,safeyellow1y,safeblue1x,safeblue1y
    global safered2x,safered2y,safegreen2x,safegreen2y,safeyellow2x,safeyellow2y,safeblue2x,safeblue2y,can_clash
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y

    if(moving_key==1):
        if((y1x,y1y)==(safered1x,safered1y) or (y1x,y1y)==(safegreen1x,safegreen1y) or (y1x,y1y)==(safeyellow1x,safeyellow1y) or (y1x,y1y)==(safeblue1x,safeblue1y) or (y1x,y1y)==(safered2x,safered2y) or (y1x,y1y)==(safegreen2x,safegreen2y) or (y1x,y1y)==(safeyellow2x,safeyellow2y) or (y1x,y1y)==(safeblue2x,safeblue2y)):
            return False    
    
    if(moving_key==2):
        if((y2x,y2y)==(safered1x,safered1y) or (y2x,y2y)==(safegreen1x,safegreen1y) or (y2x,y2y)==(safeyellow1x,safeyellow1y) or (y2x,y2y)==(safeblue1x,safeblue1y) or (y2x,y2y)==(safered2x,safered2y) or (y2x,y2y)==(safegreen2x,safegreen2y) or (y2x,y2y)==(safeyellow2x,safeyellow2y) or (y2x,y2y)==(safeblue2x,safeblue2y)):
            return False       

    if(moving_key==3):
        if((y3x,y3y)==(safered1x,safered1y) or (y3x,y3y)==(safegreen1x,safegreen1y) or (y3x,y3y)==(safeyellow1x,safeyellow1y) or (y3x,y3y)==(safeblue1x,safeblue1y) or (y3x,y3y)==(safered2x,safered2y) or (y3x,y3y)==(safegreen2x,safegreen2y) or (y3x,y3y)==(safeyellow2x,safeyellow2y) or (y3x,y3y)==(safeblue2x,safeblue2y)):
            return False   

    if(moving_key==4):
        if((y4x,y4y)==(safered1x,safered1y) or (y4x,y4y)==(safegreen1x,safegreen1y) or (y4x,y4y)==(safeyellow1x,safeyellow1y) or (y4x,y4y)==(safeblue1x,safeblue1y) or (y4x,y4y)==(safered2x,safered2y) or (y4x,y4y)==(safegreen2x,safegreen2y) or (y4x,y4y)==(safeyellow2x,safeyellow2y) or (y4x,y4y)==(safeblue2x,safeblue2y)):
            return False

    return True    


def can_clash_blue():
    global safered1x,safered1y,safegreen1x,safegreen1y,safeyellow1x,safeyellow1y,safeblue1x,safeblue1y
    global safered2x,safered2y,safegreen2x,safegreen2y,safeyellow2x,safeyellow2y,safeblue2x,safeblue2y,can_clash
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y

    if(moving_key==1):
        if((b1x,b1y)==(safered1x,safered1y) or (b1x,b1y)==(safegreen1x,safegreen1y) or (b1x,b1y)==(safeyellow1x,safeyellow1y) or (b1x,b1y)==(safeblue1x,safeblue1y) or (b1x,b1y)==(safered2x,safered2y) or (b1x,b1y)==(safegreen2x,safegreen2y) or (b1x,b1y)==(safeyellow2x,safeyellow2y) or (b1x,b1y)==(safeblue2x,safeblue2y)):
            return False    
    
    if(moving_key==2):
        if((b2x,b2y)==(safered1x,safered1y) or (b2x,b2y)==(safegreen1x,safegreen1y) or (b2x,b2y)==(safeyellow1x,safeyellow1y) or (b2x,b2y)==(safeblue1x,safeblue1y) or (b2x,b2y)==(safered2x,safered2y) or (b2x,b2y)==(safegreen2x,safegreen2y) or (b2x,b2y)==(safeyellow2x,safeyellow2y) or (b2x,b2y)==(safeblue2x,safeblue2y)):
            return False       

    if(moving_key==3):
        if((b3x,b3y)==(safered1x,safered1y) or (b3x,b3y)==(safegreen1x,safegreen1y) or (b3x,b3y)==(safeyellow1x,safeyellow1y) or (b3x,b3y)==(safeblue1x,safeblue1y) or (b3x,b3y)==(safered2x,safered2y) or (b3x,b3y)==(safegreen2x,safegreen2y) or (b3x,b3y)==(safeyellow2x,safeyellow2y) or (b3x,b3y)==(safeblue2x,safeblue2y)):
            return False   

    if(moving_key==4):
        if((b4x,b4y)==(safered1x,safered1y) or (b4x,b4y)==(safegreen1x,safegreen1y) or (b4x,b4y)==(safeyellow1x,safeyellow1y) or (b4x,b4y)==(safeblue1x,safeblue1y) or (b4x,b4y)==(safered2x,safered2y) or (b4x,b4y)==(safegreen2x,safegreen2y) or (b4x,b4y)==(safeyellow2x,safeyellow2y) or (b4x,b4y)==(safeblue2x,safeblue2y)):
            return False

    return True    



      
def clash_red(moving_key):
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y


    if(moving_key==1):
        if((r1x,r1y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            g1.goto(g1x,g1y)
            
        if((r1x,r1y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                

            g2.goto(g2x,g2y)


        if((r1x,r1y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            g3.goto(g3x,g3y)
            
        if((r1x,r1y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            g4.goto(g4x,g4y)

    if(moving_key==2):
        if((r2x,r2y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                
            g1.goto(g1x,g1y)
            
        if((r2x,r2y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            g2.goto(g2x,g2y)


        if((r2x,r2y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            g3.goto(g3x,g3y)

        if((r2x,r2y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            g4.goto(g4x,g4y)

    if(moving_key==3):
        if((r3x,r3y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            g1.goto(g1x,g1y)
            
        if((r3x,r3y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            g2.goto(g2x,g2y)


        if((r3x,r3y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            g3.goto(g3x,g3y)

        if((r3x,r3y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            g4.goto(g4x,g4y)


    if(moving_key==4):
        if((r4x,r4y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            g1.goto(g1x,g1y)
            
        if((r4x,r4y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            g2.goto(g2x,g2y)


        if((r4x,r4y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            g3.goto(g3x,g3y)

        if((r4x,r4y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            g4.goto(g4x,g4y)


    if(moving_key==1):
        if((r1x,r1y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            y1.goto(y1x,y1y)
            
        if((r1x,r1y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                

            y2.goto(y2x,y2y)


        if((r1x,r1y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            y3.goto(y3x,y3y)
            
        if((r1x,r1y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            y4.goto(y4x,y4y)

    if(moving_key==2):
        if((r2x,r2y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                
            y1.goto(y1x,y1y)
            
        if((r2x,r2y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            y2.goto(y2x,y2y)


        if((r2x,r2y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            y3.goto(y3x,y3y)

        if((r2x,r2y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            y4.goto(y4x,y4y)

    if(moving_key==3):
        if((r3x,r3y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            y1.goto(y1x,y1y)
            
        if((r3x,r3y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            y2.goto(y2x,y2y)


        if((r3x,r3y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            y3.goto(y3x,y3y)

        if((r3x,r3y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            y4.goto(y4x,y4y)


    if(moving_key==4):
        if((r4x,r4y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            y1.goto(y1x,y1y)
            
        if((r4x,r4y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            y2.goto(y2x,y2y)


        if((r4x,r4y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            y3.goto(y3x,y3y)

        if((r4x,r4y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            y4.goto(y4x,y4y)



    if(moving_key==1):
        if((r1x,r1y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            b1.goto(b1x,b1y)
            
        if((r1x,r1y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                

            b2.goto(b2x,b2y)


        if((r1x,r1y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            b3.goto(b3x,b3y)
            
        if((r1x,r1y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r1.ht()
                time.sleep(1/2)
                r1.st()                
            b4.goto(b4x,b4y)

    if(moving_key==2):
        if((r2x,r2y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                
            b1.goto(b1x,b1y)
            
        if((r2x,r2y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            b2.goto(b2x,b2y)


        if((r2x,r2y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            b3.goto(b3x,b3y)

        if((r2x,r2y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r2.ht()
                time.sleep(1/2)
                r2.st()                            
            b4.goto(b4x,b4y)

    if(moving_key==3):
        if((r3x,r3y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            b1.goto(b1x,b1y)
            
        if((r3x,r3y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            b2.goto(b2x,b2y)


        if((r3x,r3y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            b3.goto(b3x,b3y)

        if((r3x,r3y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r3.ht()
                time.sleep(1/2)
                r3.st()                            
            b4.goto(b4x,b4y)


    if(moving_key==4):
        if((r4x,r4y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            b1.goto(b1x,b1y)
            
        if((r4x,r4y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            b2.goto(b2x,b2y)


        if((r4x,r4y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            b3.goto(b3x,b3y)

        if((r4x,r4y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                r4.ht()
                time.sleep(1/2)
                r4.st()                            
            b4.goto(b4x,b4y)









def clash_green(moving_key):
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y


    if(moving_key==1):
        if((g1x,g1y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            r1.goto(r1x,r1y)
            
        if((g1x,g1y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                

            r2.goto(r2x,r2y)


        if((g1x,g1y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            r3.goto(r3x,r3y)
            
        if((g1x,g1y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            r4.goto(r4x,r4y)

    if(moving_key==2):
        if((g2x,g2y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                
            r1.goto(r1x,r1y)
            
        if((g2x,g2y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            r2.goto(r2x,r2y)


        if((g2x,g2y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            r3.goto(r3x,r3y)

        if((g2x,g2y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            r4.goto(r4x,r4y)

    if(moving_key==3):
        if((g3x,g3y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            r1.goto(r1x,r1y)
            
        if((g3x,g3y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            r2.goto(r2x,r2y)


        if((g3x,g3y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            r3.goto(r3x,r3y)

        if((g3x,g3y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            r4.goto(r4x,r4y)


    if(moving_key==4):
        if((g4x,g4y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            r1.goto(r1x,r1y)
            
        if((g4x,g4y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            r2.goto(r2x,r2y)


        if((g4x,g4y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            r3.goto(r3x,r3y)

        if((g4x,g4y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)
             
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            r4.goto(r4x,r4y)


    if(moving_key==1):
        if((g1x,g1y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            y1.goto(y1x,y1y)
            
        if((g1x,g1y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                

            y2.goto(y2x,y2y)


        if((g1x,g1y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            y3.goto(y3x,y3y)
            
        if((g1x,g1y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            y4.goto(y4x,y4y)

    if(moving_key==2):
        if((g2x,g2y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                
            y1.goto(y1x,y1y)
            
        if((g2x,g2y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            y2.goto(y2x,y2y)


        if((g2x,g2y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            y3.goto(y3x,y3y)

        if((g2x,g2y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            y4.goto(y4x,y4y)

    if(moving_key==3):
        if((g3x,g3y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            y1.goto(y1x,y1y)
            
        if((g3x,g3y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            y2.goto(y2x,y2y)


        if((g3x,g3y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            y3.goto(y3x,y3y)

        if((g3x,g3y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            y4.goto(y4x,y4y)


    if(moving_key==4):
        if((g4x,g4y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            y1.goto(y1x,y1y)
            
        if((g4x,g4y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            y2.goto(y2x,y2y)


        if((g4x,g4y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            y3.goto(y3x,y3y)

        if((g4x,g4y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            y4.goto(y4x,y4y)



    if(moving_key==1):
        if((g1x,g1y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            b1.goto(b1x,b1y)
            
        if((g1x,g1y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                

            b2.goto(b2x,b2y)


        if((g1x,g1y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            b3.goto(b3x,b3y)
            
        if((g1x,g1y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g1.ht()
                time.sleep(1/2)
                g1.st()                
            b4.goto(b4x,b4y)

    if(moving_key==2):
        if((g2x,g2y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                
            b1.goto(b1x,b1y)
            
        if((g2x,g2y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            b2.goto(b2x,b2y)


        if((g2x,g2y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            b3.goto(b3x,b3y)

        if((g2x,g2y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g2.ht()
                time.sleep(1/2)
                g2.st()                            
            b4.goto(b4x,b4y)

    if(moving_key==3):
        if((g3x,g3y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            b1.goto(b1x,b1y)
            
        if((g3x,g3y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            b2.goto(b2x,b2y)


        if((g3x,g3y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            b3.goto(b3x,b3y)

        if((g3x,g3y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g3.ht()
                time.sleep(1/2)
                g3.st()                            
            b4.goto(b4x,b4y)


    if(moving_key==4):
        if((g4x,g4y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            b1.goto(b1x,b1y)
            
        if((g4x,g4y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            b2.goto(b2x,b2y)


        if((g4x,g4y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            b3.goto(b3x,b3y)

        if((g4x,g4y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                g4.ht()
                time.sleep(1/2)
                g4.st()                            
            b4.goto(b4x,b4y)



def clash_yellow(moving_key):
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y

    if(moving_key==1):
        if((y1x,y1y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            r1.goto(r1x,r1y)
            
        if((y1x,y1y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                

            r2.goto(r2x,r2y)


        if((y1x,y1y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            r3.goto(r3x,r3y)
            
        if((y1x,y1y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            r4.goto(r4x,r4y)

    if(moving_key==2):
        if((y2x,y2y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                
            r1.goto(r1x,r1y)
            
        if((y2x,y2y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            r2.goto(r2x,r2y)


        if((y2x,y2y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            r3.goto(r3x,r3y)

        if((y2x,y2y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            r4.goto(r4x,r4y)

    if(moving_key==3):
        if((y3x,y3y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            r1.goto(r1x,r1y)
            
        if((y3x,y3y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            r2.goto(r2x,r2y)


        if((y3x,y3y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            r3.goto(r3x,r3y)

        if((y3x,y3y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            r4.goto(r4x,r4y)


    if(moving_key==4):
        if((y4x,y4y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            r1.goto(r1x,r1y)
            
        if((y4x,y4y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            r2.goto(r2x,r2y)


        if((y4x,y4y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            r3.goto(r3x,r3y)

        if((y4x,y4y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            r4.goto(r4x,r4y)




    if(moving_key==1):
        if((y1x,y1y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            g1.goto(g1x,g1y)
            
        if((y1x,y1y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                

            g2.goto(g2x,g2y)


        if((y1x,y1y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            g3.goto(g3x,g3y)
            
        if((y1x,y1y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            g4.goto(g4x,g4y)

    if(moving_key==2):
        if((y2x,y2y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                
            g1.goto(g1x,g1y)
            
        if((y2x,y2y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            g2.goto(g2x,g2y)


        if((y2x,y2y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            g3.goto(g3x,g3y)

        if((y2x,y2y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            g4.goto(g4x,g4y)

    if(moving_key==3):
        if((y3x,y3y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            g1.goto(g1x,g1y)
            
        if((y3x,y3y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            g2.goto(g2x,g2y)


        if((y3x,y3y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            g3.goto(g3x,g3y)

        if((y3x,y3y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            g4.goto(g4x,g4y)


    if(moving_key==4):
        if((y4x,y4y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            g1.goto(g1x,g1y)
            
        if((y4x,y4y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            g2.goto(g2x,g2y)


        if((y4x,y4y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            g3.goto(g3x,g3y)

        if((y4x,y4y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            g4.goto(g4x,g4y)





    if(moving_key==1):
        if((y1x,y1y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            b1.goto(b1x,b1y)
            
        if((y1x,y1y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                

            b2.goto(b2x,b2y)


        if((y1x,y1y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            b3.goto(b3x,b3y)
            
        if((y1x,y1y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y1.ht()
                time.sleep(1/2)
                y1.st()                
            b4.goto(b4x,b4y)

    if(moving_key==2):
        if((y2x,y2y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                
            b1.goto(b1x,b1y)
            
        if((y2x,y2y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            b2.goto(b2x,b2y)


        if((y2x,y2y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            b3.goto(b3x,b3y)

        if((y2x,y2y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y2.ht()
                time.sleep(1/2)
                y2.st()                            
            b4.goto(b4x,b4y)

    if(moving_key==3):
        if((y3x,y3y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            b1.goto(b1x,b1y)
            
        if((y3x,y3y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            b2.goto(b2x,b2y)


        if((y3x,y3y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            b3.goto(b3x,b3y)

        if((y3x,y3y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y3.ht()
                time.sleep(1/2)
                y3.st()                            
            b4.goto(b4x,b4y)


    if(moving_key==4):
        if((y4x,y4y)==(b1x,b1y)):
            b1x=-245
            b1y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            b1.goto(b1x,b1y)
            
        if((y4x,y4y)==(b2x,b2y)):
            b2x=-175
            b2y=-175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            b2.goto(b2x,b2y)


        if((y4x,y4y)==(b3x,b3y)):
            b3x=-245
            b3y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            b3.goto(b3x,b3y)

        if((y4x,y4y)==(b4x,b4y)):
            b4x=-175
            b4y=-245

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                y4.ht()
                time.sleep(1/2)
                y4.st()                            
            b4.goto(b4x,b4y)




def clash_blue(moving_key):
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y

    if(moving_key==1):
        if((b1x,b1y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            r1.goto(r1x,r1y)
            
        if((b1x,b1y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                

            r2.goto(r2x,r2y)


        if((b1x,b1y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            r3.goto(r3x,r3y)
            
        if((b1x,b1y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            r4.goto(r4x,r4y)

    if(moving_key==2):
        if((b2x,b2y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                
            r1.goto(r1x,r1y)
            
        if((b2x,b2y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            r2.goto(r2x,r2y)


        if((b2x,b2y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            r3.goto(r3x,r3y)

        if((b2x,b2y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            r4.goto(r4x,r4y)

    if(moving_key==3):
        if((b3x,b3y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            r1.goto(r1x,r1y)
            
        if((b3x,b3y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            r2.goto(r2x,r2y)


        if((b3x,b3y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            r3.goto(r3x,r3y)

        if((b3x,b3y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            r4.goto(r4x,r4y)


    if(moving_key==4):
        if((b4x,b4y)==(r1x,r1y)):
            (r1x,r1y)=(-280+35,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            r1.goto(r1x,r1y)
            
        if((b4x,b4y)==(r2x,r2y)):
            (r2x,r2y)=(-280+105,140+105)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            r2.goto(r2x,r2y)


        if((b4x,b4y)==(r3x,r3y)):
            (r3x,r3y)=(-280+35,140+35)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            r3.goto(r3x,r3y)

        if((b4x,b4y)==(r4x,r4y)):
            (r4x,r4y)=(-280+105,140+35)

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            r4.goto(r4x,r4y)




    if(moving_key==1):
        if((b1x,b1y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            g1.goto(g1x,g1y)
            
        if((b1x,b1y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                

            g2.goto(g2x,g2y)


        if((b1x,b1y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            g3.goto(g3x,g3y)
            
        if((b1x,b1y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            g4.goto(g4x,g4y)

    if(moving_key==2):
        if((b2x,b2y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                
            g1.goto(g1x,g1y)
            
        if((b2x,b2y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            g2.goto(g2x,g2y)


        if((b2x,b2y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            g3.goto(g3x,g3y)

        if((b2x,b2y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            g4.goto(g4x,g4y)

    if(moving_key==3):
        if((b3x,b3y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            g1.goto(g1x,g1y)
            
        if((b3x,b3y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            g2.goto(g2x,g2y)


        if((b3x,b3y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            g3.goto(g3x,g3y)

        if((b3x,b3y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            g4.goto(g4x,g4y)


    if(moving_key==4):
        if((b4x,b4y)==(g1x,g1y)):
            (g1x,g1y)=(175,245)
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            g1.goto(g1x,g1y)
            
        if((b4x,b4y)==(g2x,g2y)):
            g2x=245
            g2y=245
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            g2.goto(g2x,g2y)


        if((b4x,b4y)==(g3x,g3y)):
            g3x=175
            g3y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            g3.goto(g3x,g3y)

        if((b4x,b4y)==(g4x,g4y)):
            g4x=245
            g4y=175
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            g4.goto(g4x,g4y)





    if(moving_key==1):
        if((b1x,b1y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            y1.goto(y1x,y1y)
            
        if((b1x,b1y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                

            y2.goto(y2x,y2y)


        if((b1x,b1y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            y3.goto(y3x,y3y)
            
        if((b1x,b1y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b1.ht()
                time.sleep(1/2)
                b1.st()                
            y4.goto(y4x,y4y)

    if(moving_key==2):
        if((b2x,b2y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                
            y1.goto(y1x,y1y)
            
        if((b2x,b2y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            y2.goto(y2x,y2y)


        if((b2x,b2y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            y3.goto(y3x,y3y)

        if((b2x,b2y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b2.ht()
                time.sleep(1/2)
                b2.st()                            
            y4.goto(y4x,y4y)

    if(moving_key==3):
        if((b3x,b3y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            y1.goto(y1x,y1y)
            
        if((b3x,b3y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            y2.goto(y2x,y2y)


        if((b3x,b3y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            y3.goto(y3x,y3y)

        if((b3x,b3y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b3.ht()
                time.sleep(1/2)
                b3.st()                            
            y4.goto(y4x,y4y)


    if(moving_key==4):
        if((b4x,b4y)==(y1x,y1y)):
            (y1x,y1y)=(140+35,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            y1.goto(y1x,y1y)
            
        if((b4x,b4y)==(y2x,y2y)):
            (y2x,y2y)=(140+105,-280+105)
            
            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            y2.goto(y2x,y2y)


        if((b4x,b4y)==(y3x,y3y)):
            (y3x,y3y)=(140+35,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            y3.goto(y3x,y3y)

        if((b4x,b4y)==(y4x,y4y)):
            (y4x,y4y)=(140+105,-280+35)
            

            for i in range(5):
                clash_beep()
                time.sleep(1/2)               
                b4.ht()
                time.sleep(1/2)
                b4.st()                            
            y4.goto(y4x,y4y)






































#glow function used to blink the keys
#not over 
def glow():
    r1.color('black','white')
    #time.sleep(1/3)
    r1.color('black','red')    

#It is used to select moving key using mouse buttons
def make_your_move():
    global moving_key
    r1.onclick(key1)
    g1.onclick(key1)
    y1.onclick(key1)
    b1.onclick(key1)

    r2.onclick(key2)
    g2.onclick(key2)
    y2.onclick(key2)
    b2.onclick(key2)

    r3.onclick(key3)
    g3.onclick(key3)
    y3.onclick(key3)
    b3.onclick(key3)

    r4.onclick(key4)
    g4.onclick(key4)
    y4.onclick(key4)
    b4.onclick(key4)
    listen()
    #if the user till not selected the keys
    if(moving_key==0):
        com.goto(380,-120)
        com.write("       Please   click   on ",False,align='left',font=("Times new roman",22,"bold"))
        com.goto(380,-150)
        com.write("       token      to    move",False,align='left',font=("Times new roman",22,"bold"))
        while(True): 
            wait.screen.tracer(1)
            wait.screen.delay(10)
            wait.fd(100)
            wait.right(90)
            if(moving_key!=0):
                com.undo()
                com.undo()
                com.undo()
                break      
tracer(1)
delay(10)

up()
goto(380,300)
write("       click on buttons  ",False,align='left',font=("Times new roman",22,"bold"))
goto(380,270)
write("             for action ",False,align='left',font=("Times new roman",22,"bold"))
down()
fd(350)        
st()











dice=6

def move_red(moving_key):
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    global all_red_start_pos,give_birth_red
    global dice,rem
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted
    global endredx,endredy,endgreenx,endgreeny,endyellowx,endyellowy,endbluex,endbluey
    global re_roll
    print("give birth red=",give_birth_red)
    if(give_birth_red):
        os.system("play Audio/load.wav&") 
        if(moving_key==1 and r1.isvisible()):
            (r1x,r1y)=(-(280),40)
            r1.clear()
            r1.goto(r1x,r1y)
        elif(moving_key==2 and r2.isvisible()):
            (r2x,r2y)=(-(280),40)
            r2.clear()
            r2.goto(r2x,r2y)
        elif(moving_key==3 and r3.isvisible()):
            (r3x,r3y)=(-(280),40)
            r3.clear()
            r3.goto(r3x,r3y)
        elif(moving_key==4 and r4.isvisible()):
            (r4x,r4y)=(-(280),40)
            r4.clear()
            r4.goto(r4x,r4y)

    else:
        if(rem==0):
            print("distance")
            distance=40*dice
        else:
            print("rem",rem)
            distance=rem
            rem=0
        if(moving_key==1 and r1.isvisible()):
            if(r1x<-60 and r1y>20 and r1y<60):
                print("redup")
                r1x=r1x+distance
                print("r1y=",r1y,"r1x=",r1x)
                if(r1x>senred1x and round(r1y,0)==senred1y):
                    rem=abs(r1x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (r1x,r1y)=(sengreen2x,sengreen2y)
                    move_red(moving_key)

            elif(r1x<-60 and r1y<20 and r1y>-20):
                print("redmid")
                r1x=r1x+distance
                print("r1y=",r1y,"r1x=",r1x)
                if(r1x>-60 and r1x<-20):
                    print("r1 won")
                    time.sleep(1)
                    r1.clear()
                    r1.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Red token reached home")
                    re_roll=True
                    check_red_won()
                    
                elif(r1x>-20):
                    r1x=r1x-distance

            elif(r1x<-60 and r1y<-20 and r1y>-60):
                print("reddown")
                if(round(r1x,0)==red2x and round(r1y,0)==red2y):
                    r1y=r1y+distance
                    if(round(r1x,0)==endredx and r1y>endredy):
                        rem=abs(r1y-endredy)
                        (r1x,r1y)=(endredx,endredy)
                        move_red(moving_key)
                else:
                    r1x=r1x-distance
                if(r1x<red2x and round(r1y,0)==red2y):
                    rem=abs(red2x-r1x)
                    (r1x,r1y)=(red2x,red2y)
                    move_red(moving_key)
            elif(r1x<-20 and r1x>-60 and r1y>60):
                print("greenleft")
                print("r1y=",r1y,"r1x=",r1x)
                if(round(r1x,0)==green2x and round(r1y,0)==green2y):
                    r1x=r1x+distance
                    print("r1y=",r1y,"r1x=",r1x)
                    if(r1x>green1x and round(r1y,0)==green1y):
                        rem=abs(r1x-green1x)
                        (r1x,r1y)=(green1x,green1y)
                        move_red(moving_key)
                else:    
                    r1y=r1y+distance   
                if(round(r1x,0)==green2x and r1y>green2y):            
                    rem=abs(r1y-green2y) #deleted 40
                    (r1x,r1y)=(green2x,green2y)
                    move_red(moving_key)

            elif(r1x<20 and r1x>-20 and r1y>60):
                print("greenmid")
                #if(r1x==endgreenx and r1y==endgreeny):
                print("reached endgreen")
                r1x=r1x+distance
                if(r1x>green1x and round(r1y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(r1x-green1x)
                    (r1x,r1y)=(green1x,green1y)
                    move_red(moving_key)
                    
            elif(r1x>20 and r1x<60 and r1y>60):
                print("greenright")
                r1y=r1y-distance
                print("r1y=",r1y,"r1x=",r1x)
                if(round(r1x,0)==sengreen1x and r1y<sengreen1y):
                    rem=abs(sengreen1y-r1y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (r1x,r1y)=(senyellow2x,senyellow2y)
                    move_red(moving_key)
        
            elif(r1x>60 and r1y>20 and r1y<60):
                print("yellowup")
                if(round(r1x,0)==yellow2x and round(r1y,0)==yellow2y):
                    r1y=r1y-distance
                    if(round(r1x,0)==yellow1x and r1y<yellow1y):
                        rem=abs(yellow1y-r1y)
                        (r1x,r1y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                else:
                    r1x=r1x+distance

                if(r1x>yellow2x and round(r1y,0)==yellow2y):
                    rem=abs(r1x-yellow2x)
                    (r1x,r1y)=(yellow2x,yellow2y)
                    move_red(moving_key)
    
            elif(r1x>60 and r1y>-20 and r1y<20):
                print("yellowmid")
                r1y=r1y-distance
                if(round(r1x,0)==yellow1x and r1y<yellow1y):
                        rem=abs(yellow1y-r1y)
                        (r1x,r1y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                        
                        
            elif(r1x>60 and r1y<-20 and r1y>-60):
                print("yellowdown")
                r1x=r1x-distance
                if(r1x<senyellow1x and round(r1y,0)==senyellow1y):
                    rem=abs(r1x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (r1x,r1y)=(senblue2x,senblue2y)
                    move_red(moving_key)


            elif(r1x>20 and r1x<60 and r1y<-60):
                print("blueright")
                if(round(r1x,0)==blue2x and round(r1y,0)==blue2y):
                    r1x=r1x-distance
                    if(r1x<blue1x and round(r1y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(r1x-blue1x)
                        (r1x,r1y)=(blue1x,blue1y)
                        move_red(moving_key)
                    
                else:
                    r1y=r1y-distance

                if(round(r1x,0)==blue2x and r1y<blue2y):
                    rem=abs(blue2y-r1y)
                    (r1x,r1y)=(blue2x,blue2y)
                    move_red(moving_key)

            elif(r1x>-20 and r1x<20 and r1y<-20):
                print("bluemid")                               
                r1x=r1x-distance
                if(r1x<blue1x and round(r1y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(r1x-blue1x)
                    (r1x,r1y)=(blue1x,blue1y)
                    move_red(moving_key)

                
            elif(r1x<-20 and r1x>-60 and r1y<-20):
                print("blueleft")
                r1y=r1y+distance
                if(round(r1x,0)==senblue1x and r1y>senblue1y):
                    rem=abs(r1y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (r1x,r1y)=(senred2x,senred2y)
                    move_red(moving_key)                        #end of checking sensitive points
            r1.clear()
            os.system("play Audio/Jump.wav&")
            r1.goto(r1x,r1y)


        elif(moving_key==2 and r2.isvisible()):
            if(r2x<-60 and r2y>20 and r2y<60):
                print("redup")
                r2x=r2x+distance
                print("r2y=",r2y,"r2x=",r2x)
                if(r2x>senred1x and round(r2y,0)==senred1y):
                    rem=abs(r2x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (r2x,r2y)=(sengreen2x,sengreen2y)
                    move_red(moving_key)

            elif(r2x<-60 and r2y<20 and r2y>-20):
                print("redmid")
                r2x=r2x+distance
                print("r2y=",r2y,"r2x=",r2x)
                if(r2x>-60 and r2x<-20):
                    print("r2 won")
                    time.sleep(1)
                    r2.clear()
                    r2.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Red token reached home")
                    re_roll=True

                    check_red_won()
                    
                elif(r2x>-20):
                    r2x=r2x-distance

            elif(r2x<-60 and r2y<-20 and r2y>-60):
                print("reddown")
                if(round(r2x,0)==red2x and round(r2y,0)==red2y):
                    r2y=r2y+distance
                    if(round(r2x,0)==endredx and r2y>endredy):
                        rem=abs(r2y-endredy)
                        (r2x,r2y)=(endredx,endredy)
                        move_red(moving_key)
                else:
                    r2x=r2x-distance
                if(r2x<red2x and round(r2y,0)==red2y):
                    rem=abs(red2x-r2x)
                    (r2x,r2y)=(red2x,red2y)
                    move_red(moving_key)
            elif(r2x<-20 and r2x>-60 and r2y>60):
                print("greenleft")
                print("r2y=",r2y,"r2x=",r2x)
                if(round(r2x,0)==green2x and round(r2y,0)==green2y):
                    r2x=r2x+distance
                    print("r2y=",r2y,"r2x=",r2x)
                    if(r2x>green1x and round(r2y,0)==green1y):
                        rem=abs(r2x-green1x)
                        (r2x,r2y)=(green1x,green1y)
                        move_red(moving_key)
                else:    
                    r2y=r2y+distance   
                if(round(r2x,0)==green2x and r2y>green2y):            
                    rem=abs(r2y-green2y) 
                    (r2x,r2y)=(green2x,green2y)
                    move_red(moving_key)

            elif(r2x<20 and r2x>-20 and r2y>60):
                print("greenmid")
                print("reached endgreen")
                r2x=r2x+distance
                if(r2x>green1x and round(r2y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(r2x-green1x)
                    (r2x,r2y)=(green1x,green1y)
                    move_red(moving_key)
                    
            elif(r2x>20 and r2x<60 and r2y>60):
                print("greenright")
                r2y=r2y-distance
                print("r2y=",r2y,"r2x=",r2x)
                if(round(r2x,0)==sengreen1x and r2y<sengreen1y):
                    rem=abs(sengreen1y-r2y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (r2x,r2y)=(senyellow2x,senyellow2y)
                    move_red(moving_key)
        
            elif(r2x>60 and r2y>20 and r2y<60):
                print("yellowup")
                if(round(r2x,0)==yellow2x and round(r2y,0)==yellow2y):
                    r2y=r2y-distance
                    if(round(r2x,0)==yellow1x and r2y<yellow1y):
                        rem=abs(yellow1y-r2y)
                        (r2x,r2y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                else:
                    r2x=r2x+distance

                if(r2x>yellow2x and round(r2y,0)==yellow2y):
                    rem=abs(r2x-yellow2x)
                    (r2x,r2y)=(yellow2x,yellow2y)
                    move_red(moving_key)
    
            elif(r2x>60 and r2y>-20 and r2y<20):
                print("yellowmid")
                r2y=r2y-distance
                if(round(r2x,0)==yellow1x and r2y<yellow1y):
                        rem=abs(yellow1y-r2y)
                        (r2x,r2y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                        
                        
            elif(r2x>60 and r2y<-20 and r2y>-60):
                print("yellowdown")
                r2x=r2x-distance
                if(r2x<senyellow1x and round(r2y,0)==senyellow1y):
                    rem=abs(r2x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (r2x,r2y)=(senblue2x,senblue2y)
                    move_red(moving_key)


            elif(r2x>20 and r2x<60 and r2y<-60):
                print("blueright")
                if(round(r2x,0)==blue2x and round(r2y,0)==blue2y):
                    r2x=r2x-distance
                    if(r2x<blue1x and round(r2y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(r2x-blue1x)
                        (r2x,r2y)=(blue1x,blue1y)
                        move_red(moving_key)
                    
                else:
                    r2y=r2y-distance

                if(round(r2x,0)==blue2x and r2y<blue2y):
                    rem=abs(blue2y-r2y)
                    (r2x,r2y)=(blue2x,blue2y)
                    move_red(moving_key)

            elif(r2x>-20 and r2x<20 and r2y<-20):
                print("bluemid")                               
                r2x=r2x-distance
                if(r2x<blue1x and round(r2y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(r2x-blue1x)
                    (r2x,r2y)=(blue1x,blue1y)
                    move_red(moving_key)

                
            elif(r2x<-20 and r2x>-60 and r2y<-20):
                print("blueleft")
                r2y=r2y+distance
                if(round(r2x,0)==senblue1x and r2y>senblue1y):
                    rem=abs(r2y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (r2x,r2y)=(senred2x,senred2y)
                    move_red(moving_key)                        #end of checking sensitive points
            r2.clear()
            r2.goto(r2x,r2y)
                
        elif(moving_key==3 and r3.isvisible()):
            if(r3x<-60 and r3y>20 and r3y<60):
                print("redup")
                r3x=r3x+distance
                print("r3y=",r3y,"r3x=",r3x)
                if(r3x>senred1x and round(r3y,0)==senred1y):
                    rem=abs(r3x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (r3x,r3y)=(sengreen2x,sengreen2y)
                    move_red(moving_key)

            elif(r3x<-60 and r3y<20 and r3y>-20):
                print("redmid")
                r3x=r3x+distance
                print("r3y=",r3y,"r3x=",r3x)
                if(r3x>-60 and r3x<-20):
                    print("r3 won")
                    time.sleep(1)
                    r3.clear()
                    r3.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Red token reached home")
                    re_roll=True

                    check_red_won()
                    
                elif(r3x>-20):
                    r3x=r3x-distance

            elif(r3x<-60 and r3y<-20 and r3y>-60):
                print("reddown")
                if(round(r3x,0)==red2x and round(r3y,0)==red2y):
                    r3y=r3y+distance
                    if(round(r3x,0)==endredx and r3y>endredy):
                        rem=abs(r3y-endredy)
                        (r3x,r3y)=(endredx,endredy)
                        move_red(moving_key)
                else:
                    r3x=r3x-distance
                if(r3x<red2x and round(r3y,0)==red2y):
                    rem=abs(red2x-r3x)
                    (r3x,r3y)=(red2x,red2y)
                    move_red(moving_key)
            elif(r3x<-20 and r3x>-60 and r3y>60):
                print("greenleft")
                print("r3y=",r3y,"r3x=",r3x)
                if(round(r3x,0)==green2x and round(r3y,0)==green2y):
                    r3x=r3x+distance
                    print("r3y=",r3y,"r3x=",r3x)
                    if(r3x>green1x and round(r3y,0)==green1y):
                        rem=abs(r3x-green1x)
                        (r3x,r3y)=(green1x,green1y)
                        move_red(moving_key)
                else:    
                    r3y=r3y+distance   
                if(round(r3x,0)==green2x and r3y>green2y):            
                    rem=abs(r3y-green2y) 
                    (r3x,r3y)=(green2x,green2y)
                    move_red(moving_key)

            elif(r3x<20 and r3x>-20 and r3y>60):
                print("greenmid")
                print("reached endgreen")
                r3x=r3x+distance
                if(r3x>green1x and round(r3y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(r3x-green1x)
                    (r3x,r3y)=(green1x,green1y)
                    move_red(moving_key)
                    
            elif(r3x>20 and r3x<60 and r3y>60):
                print("greenright")
                r3y=r3y-distance
                print("r3y=",r3y,"r3x=",r3x)
                if(round(r3x,0)==sengreen1x and r3y<sengreen1y):
                    rem=abs(sengreen1y-r3y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (r3x,r3y)=(senyellow2x,senyellow2y)
                    move_red(moving_key)
        
            elif(r3x>60 and r3y>20 and r3y<60):
                print("yellowup")
                if(round(r3x,0)==yellow2x and round(r3y,0)==yellow2y):
                    r3y=r3y-distance
                    if(round(r3x,0)==yellow1x and r3y<yellow1y):
                        rem=abs(yellow1y-r3y)
                        (r3x,r3y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                else:
                    r3x=r3x+distance

                if(r3x>yellow2x and round(r3y,0)==yellow2y):
                    rem=abs(r3x-yellow2x)
                    (r3x,r3y)=(yellow2x,yellow2y)
                    move_red(moving_key)
    
            elif(r3x>60 and r3y>-20 and r3y<20):
                print("yellowmid")
                r3y=r3y-distance
                if(round(r3x,0)==yellow1x and r3y<yellow1y):
                        rem=abs(yellow1y-r3y)
                        (r3x,r3y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                        
                        
            elif(r3x>60 and r3y<-20 and r3y>-60):
                print("yellowdown")
                r3x=r3x-distance
                if(r3x<senyellow1x and round(r3y,0)==senyellow1y):
                    rem=abs(r3x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (r3x,r3y)=(senblue2x,senblue2y)
                    move_red(moving_key)


            elif(r3x>20 and r3x<60 and r3y<-60):
                print("blueright")
                if(round(r3x,0)==blue2x and round(r3y,0)==blue2y):
                    r3x=r3x-distance
                    if(r3x<blue1x and round(r3y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(r3x-blue1x)
                        (r3x,r3y)=(blue1x,blue1y)
                        move_red(moving_key)
                    
                else:
                    r3y=r3y-distance

                if(round(r3x,0)==blue2x and r3y<blue2y):
                    rem=abs(blue2y-r3y)
                    (r3x,r3y)=(blue2x,blue2y)
                    move_red(moving_key)

            elif(r3x>-20 and r3x<20 and r3y<-20):
                print("bluemid")                               
                r3x=r3x-distance
                if(r3x<blue1x and round(r3y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(r3x-blue1x)
                    (r3x,r3y)=(blue1x,blue1y)
                    move_red(moving_key)

                
            elif(r3x<-20 and r3x>-60 and r3y<-20):
                print("blueleft")
                r3y=r3y+distance
                if(round(r3x,0)==senblue1x and r3y>senblue1y):
                    rem=abs(r3y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (r3x,r3y)=(senred2x,senred2y)
                    move_red(moving_key)                        #end of checking sensitive points
            r3.clear()
            r3.goto(r3x,r3y)

        elif(moving_key==4 and r4.isvisible()):
            if(r4x<-60 and r4y>20 and r4y<60):
                print("redup")
                r4x=r4x+distance
                print("r4y=",r4y,"r4x=",r4x)
                if(r4x>senred1x and round(r4y,0)==senred1y):
                    rem=abs(r4x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (r4x,r4y)=(sengreen2x,sengreen2y)
                    move_red(moving_key)

            elif(r4x<-60 and r4y<20 and r4y>-20):
                print("redmid")
                r4x=r4x+distance
                print("r4y=",r4y,"r4x=",r4x)
                if(r4x>-60 and r4x<-20):
                    print("r4 won")
                    time.sleep(1)
                    r4.clear()
                    r4.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Red token reached home")
                    re_roll=True

                    check_red_won()
             
                elif(r4x>-20):
                    r4x=r4x-distance

            elif(r4x<-60 and r4y<-20 and r4y>-60):
                print("reddown")
                if(round(r4x,0)==red2x and round(r4y,0)==red2y):
                    r4y=r4y+distance
                    if(round(r4x,0)==endredx and r4y>endredy):
                        rem=abs(r4y-endredy)
                        (r4x,r4y)=(endredx,endredy)
                        move_red(moving_key)
                else:
                    r4x=r4x-distance
                if(r4x<red2x and round(r4y,0)==red2y):
                    rem=abs(red2x-r4x)
                    (r4x,r4y)=(red2x,red2y)
                    move_red(moving_key)
            elif(r4x<-20 and r4x>-60 and r4y>60):
                print("greenleft")
                print("r4y=",r4y,"r4x=",r4x)
                if(round(r4x,0)==green2x and round(r4y,0)==green2y):
                    r4x=r4x+distance
                    print("r4y=",r4y,"r4x=",r4x)
                    if(r4x>green1x and round(r4y,0)==green1y):
                        rem=abs(r4x-green1x)
                        (r4x,r4y)=(green1x,green1y)
                        move_red(moving_key)
                else:    
                    r4y=r4y+distance   
                if(round(r4x,0)==green2x and r4y>green2y):            
                    rem=abs(r4y-green2y) 
                    (r4x,r4y)=(green2x,green2y)
                    move_red(moving_key)

            elif(r4x<20 and r4x>-20 and r4y>60):
                print("greenmid")
                print("reached endgreen")
                r4x=r4x+distance
                if(r4x>green1x and round(r4y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(r4x-green1x)
                    (r4x,r4y)=(green1x,green1y)
                    move_red(moving_key)
                    
            elif(r4x>20 and r4x<60 and r4y>60):
                print("greenright")
                r4y=r4y-distance
                print("r4y=",r4y,"r4x=",r4x)
                if(round(r4x,0)==sengreen1x and r4y<sengreen1y):
                    rem=abs(sengreen1y-r4y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (r4x,r4y)=(senyellow2x,senyellow2y)
                    move_red(moving_key)
        
            elif(r4x>60 and r4y>20 and r4y<60):
                print("yellowup")
                if(round(r4x,0)==yellow2x and round(r4y,0)==yellow2y):
                    r4y=r4y-distance
                    if(round(r4x,0)==yellow1x and r4y<yellow1y):
                        rem=abs(yellow1y-r4y)
                        (r4x,r4y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                else:
                    r4x=r4x+distance

                if(r4x>yellow2x and round(r4y,0)==yellow2y):
                    rem=abs(r4x-yellow2x)
                    (r4x,r4y)=(yellow2x,yellow2y)
                    move_red(moving_key)
    
            elif(r4x>60 and r4y>-20 and r4y<20):
                print("yellowmid")
                r4y=r4y-distance
                if(round(r4x,0)==yellow1x and r4y<yellow1y):
                        rem=abs(yellow1y-r4y)
                        (r4x,r4y)=(yellow1x,yellow1y)
                        move_red(moving_key)
                        
                        
            elif(r4x>60 and r4y<-20 and r4y>-60):
                print("yellowdown")
                r4x=r4x-distance
                if(r4x<senyellow1x and round(r4y,0)==senyellow1y):
                    rem=abs(r4x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (r4x,r4y)=(senblue2x,senblue2y)
                    move_red(moving_key)


            elif(r4x>20 and r4x<60 and r4y<-60):
                print("blueright")
                if(round(r4x,0)==blue2x and round(r4y,0)==blue2y):
                    r4x=r4x-distance
                    if(r4x<blue1x and round(r4y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(r4x-blue1x)
                        (r4x,r4y)=(blue1x,blue1y)
                        move_red(moving_key)
                    
                else:
                    r4y=r4y-distance

                if(round(r4x,0)==blue2x and r4y<blue2y):
                    rem=abs(blue2y-r4y)
                    (r4x,r4y)=(blue2x,blue2y)
                    move_red(moving_key)

            elif(r4x>-20 and r4x<20 and r4y<-20):
                print("bluemid")                               
                r4x=r4x-distance
                if(r4x<blue1x and round(r4y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(r4x-blue1x)
                    (r4x,r4y)=(blue1x,blue1y)
                    move_red(moving_key)

                
            elif(r4x<-20 and r4x>-60 and r4y<-20):
                print("blueleft")
                r4y=r4y+distance
                if(round(r4x,0)==senblue1x and r4y>senblue1y):
                    rem=abs(r4y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (r4x,r4y)=(senred2x,senred2y)
                    move_red(moving_key)                        #end of checking sensitive points
            r4.clear()
            r4.goto(r4x,r4y)



com.st()
global re_roll
re_roll=False
turn.st()
turn.goto(380,-65)
def play_red():
    global moving_key,can_clash
    moving_key=0
    global  r1x,r1y,r2x,r2y,r3x,r3y,r4x,r4y
    global all_red_start_pos,give_birth_red,dice
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global re_roll


    turn.write("       Red's   Turn ",False,align='left',font=("Times new roman",22,"bold"))
    
    #numinput("Rolling the dice","Press enter to roll the dice",1)
    show_red_turn()
    dice=roll_dice()
    show_dice(dice)
    all_red_start_pos=check_red_start_pos()
    print("all_red_start_pos",all_red_start_pos) 
    if(dice!=6 and all_red_start_pos):
        time.sleep(3/9)
        d.clear()
        pass
    elif(dice==6):
        os.system("play Audio/positive.wav&")
        make_your_move()
        if(moving_key==1 and r1.isvisible() and (r1x==-280+35) and (r1y==140+105)):
            give_birth_red=True
        elif(moving_key==2 and r2.isvisible() and (r2x==-280+105) and (r2y==140+105)):
            give_birth_red=True
        elif(moving_key==3 and r3.isvisible() and (r3x==-280+35) and (r3y==140+35)):
            give_birth_red=True
        elif(moving_key==4 and r4.isvisible() and (r4x==-280+105) and (r4y==140+35)):
            give_birth_red=True
        else:
            give_birth_red=False

        move_red(moving_key)
        re_roll=True
        d.clear()
    elif(not all_red_start_pos):
        give_birth_red=False
        make_your_move()
        move_red(moving_key)
        d.clear()
    turn.undo()
    can_clash=can_clash_red()
    if(can_clash):
        clash_red(moving_key)
    if(re_roll):
        d.clear()
        re_roll=False
        play_red()


tracer(1)
delay(4)
d.ht()


def move_green(moving_key):
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global all_green_start_pos,give_birth_green
    global dice,rem
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted
    global endredx,endredy,endgreenx,endgreeny,endyellowx,endyellowy,endbluex,endbluey
    global re_roll
    g1.st()
    g2.st()
    g3.st()
    g4.st()
    
    if(give_birth_green):
        os.system("play Audio/load.wav&")
        if(moving_key==1 and g1.isvisible()):
            (g1x,g1y)=(40,280)
            g1.clear()
            g1.goto(g1x,g1y)
        elif(moving_key==2 and g2.isvisible()):
            (g2x,g2y)=(40,280)
            g2.clear()
            g2.goto(g2x,g2y)
        elif(moving_key==3 and g3.isvisible()):
            (g3x,g3y)=(40,280)
            g3.clear()
            g3.goto(g3x,g3y)
        elif(moving_key==4 and g4.isvisible()):
            (g4x,g4y)=(40,280)
            g4.clear()
            g4.goto(g4x,g4y)

    else:
        if(rem==0):
            print("distance")
            distance=40*dice
        else:
            print("rem",rem)
            distance=rem
            rem=0
        if(moving_key==1 and g1.isvisible()):
            if(g1x<-60 and g1y>20 and g1y<60):
                print("redup")
                g1x=g1x+distance
                print("g1y=",g1y,"g1x=",g1x)
                if(g1x>senred1x and round(g1y,0)==senred1y):
                    rem=abs(g1x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (g1x,g1y)=(sengreen2x,sengreen2y)
                    move_green(moving_key)

            elif(g1x<-60 and g1y<20 and g1y>-20):
                print("redmid")
                g1y=g1y+distance
                if(round(g1x,0)==red1x and g1y>red1y):
                        rem=abs(red1y-g1y)
                        (g1x,g1y)=(red1x,red1y)
                        move_green(moving_key)




            elif(g1x<-60 and g1y<-20 and g1y>-60):
                print("reddown")
                if(round(g1x,0)==red2x and round(g1y,0)==red2y):
                    g1y=g1y+distance
                    if(round(g1x,0)==red1x and g1y>red1y):
                        rem=abs(g1y-red1y)
                        (g1x,g1y)=(red1x,red1y)
                        move_green(moving_key)
                else:
                    g1x=g1x-distance
                if(g1x<red2x and round(g1y,0)==red2y):
                    rem=abs(red2x-g1x)
                    (g1x,g1y)=(red2x,red2y)
                    move_green(moving_key)
            elif(g1x<-20 and g1x>-60 and g1y>60):
                print("greenleft")
                print("g1y=",g1y,"g1x=",g1x)
                if(round(g1x,0)==green2x and round(g1y,0)==green2y):
                    g1x=g1x+distance
                    print("g1y=",g1y,"g1x=",g1x)
                    if(g1x>endgreenx and round(g1y,0)==endgreeny):
                        rem=abs(g1x-endgreenx)
                        (g1x,g1y)=(endgreenx,endgreeny)
                        move_green(moving_key)
                else:    
                    g1y=g1y+distance   
                if(round(g1x,0)==green2x and g1y>green2y):            
                    rem=abs(g1y-green2y) #deleted 40
                    (g1x,g1y)=(green2x,green2y)
                    move_green(moving_key)

            elif(g1x<20 and g1x>-20 and g1y>60):
                print("greenmid")
                #if(g1x==endgreenx and g1y==endgreeny):            
                g1y=g1y-distance
                print("g1y=",g1y,"g1x=",g1x)
                if(g1y<60 and g1y>20):
                    print("g1 won")
                    time.sleep(1)
                    g1.clear()
                    g1.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Green token reached home")
                    re_roll=True
                    
                    check_green_won()
                elif(g1y<20):
                    g1y=g1y+distance


                    
                    
            elif(g1x>20 and g1x<60 and g1y>60):
                print("greenright")
                g1y=g1y-distance
                print("g1y=",g1y,"g1x=",g1x)
                if(round(g1x,0)==sengreen1x and g1y<sengreen1y):
                    rem=abs(sengreen1y-g1y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (g1x,g1y)=(senyellow2x,senyellow2y)
                    move_green(moving_key)
        
            elif(g1x>60 and g1y>20 and g1y<60):
                print("yellowup")
                if(round(g1x,0)==yellow2x and round(g1y,0)==yellow2y):
                    g1y=g1y-distance
                    if(round(g1x,0)==yellow1x and g1y<yellow1y):
                        rem=abs(yellow1y-g1y)
                        (g1x,g1y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                else:
                    g1x=g1x+distance

                if(g1x>yellow2x and round(g1y,0)==yellow2y):
                    rem=abs(g1x-yellow2x)
                    (g1x,g1y)=(yellow2x,yellow2y)
                    move_green(moving_key)
    
            elif(g1x>60 and g1y>-20 and g1y<20):
                print("yellowmid")
                g1y=g1y-distance
                if(round(g1x,0)==yellow1x and g1y<yellow1y):
                        rem=abs(yellow1y-g1y)
                        (g1x,g1y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                        
                        
            elif(g1x>60 and g1y<-20 and g1y>-60):
                print("yellowdown")
                g1x=g1x-distance
                if(g1x<senyellow1x and round(g1y,0)==senyellow1y):
                    rem=abs(g1x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (g1x,g1y)=(senblue2x,senblue2y)
                    move_green(moving_key)


            elif(g1x>20 and g1x<60 and g1y<-60):
                print("blueright")
                if(round(g1x,0)==blue2x and round(g1y,0)==blue2y):
                    g1x=g1x-distance
                    if(g1x<blue1x and round(g1y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(g1x-blue1x)
                        (g1x,g1y)=(blue1x,blue1y)
                        move_green(moving_key)
                    
                else:
                    g1y=g1y-distance

                if(round(g1x,0)==blue2x and g1y<blue2y):
                    rem=abs(blue2y-g1y)
                    (g1x,g1y)=(blue2x,blue2y)
                    move_green(moving_key)

            elif(g1x>-20 and g1x<20 and g1y<-20):
                print("bluemid")                               
                g1x=g1x-distance
                if(g1x<blue1x and round(g1y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(g1x-blue1x)
                    (g1x,g1y)=(blue1x,blue1y)
                    move_green(moving_key)

                
            elif(g1x<-20 and g1x>-60 and g1y<-20):
                print("blueleft")
                g1y=g1y+distance
                if(round(g1x,0)==senblue1x and g1y>senblue1y):
                    rem=abs(g1y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (g1x,g1y)=(senred2x,senred2y)
                    move_green(moving_key)                        #end of checking sensitive points
            g1.clear()
            g1.goto(g1x,g1y)


        elif(moving_key==2 and g2.isvisible()):
            if(g2x<-60 and g2y>20 and g2y<60):
                print("redup")
                g2x=g2x+distance
                print("g2y=",g2y,"g2x=",g2x)
                if(g2x>senred1x and round(g2y,0)==senred1y):
                    rem=abs(g2x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (g2x,g2y)=(sengreen2x,sengreen2y)
                    move_green(moving_key)

            elif(g2x<-60 and g2y<20 and g2y>-20):
                print("redmid")
                g2y=g2y+distance
                if(round(g2x,0)==red1x and g2y>red1y):
                        rem=abs(red1y-g2y)
                        (g2x,g2y)=(red1x,red1y)
                        move_green(moving_key)




            elif(g2x<-60 and g2y<-20 and g2y>-60):
                print("reddown")
                if(round(g2x,0)==red2x and round(g2y,0)==red2y):
                    g2y=g2y+distance
                    if(round(g2x,0)==red1x and g2y>red1y):
                        rem=abs(g2y-red1y)
                        (g2x,g2y)=(red1x,red1y)
                        move_green(moving_key)
                else:
                    g2x=g2x-distance
                if(g2x<red2x and round(g2y,0)==red2y):
                    rem=abs(red2x-g2x)
                    (g2x,g2y)=(red2x,red2y)
                    move_green(moving_key)

            elif(g2x<-20 and g2x>-60 and g2y>60):
                 print("greenleft")
                 print("g2y=",g2y,"g2x=",g2x)
                 if(round(g2x,0)==green2x and round(g2y,0)==green2y):
                     g2x=g2x+distance
                     print("g2y=",g2y,"g2x=",g2x)
                     if(g2x>endgreenx and round(g2y,0)==endgreeny):
                         rem=abs(g2x-endgreenx)
                         (g2x,g2y)=(endgreenx,endgreeny)
                         move_green(moving_key)
                 else:    
                     g2y=g2y+distance   
                 if(round(g2x,0)==green2x and g2y>green2y):            
                     rem=abs(g2y-green2y) #deleted 40
                     (g2x,g2y)=(green2x,green2y)
                     move_green(moving_key)

            elif(g2x<20 and g2x>-20 and g2y>60):
                print("greenmid")
                #if(g2x==endgreenx and g2y==endgreeny):            
                g2y=g2y-distance
                print("g2y=",g2y,"g2x=",g2x)
                if(g2y<60 and g2y>20):
                    print("g2 won")
                    time.sleep(1)
                    g2.clear()
                    g2.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Green token reached home")
                    re_roll=True
                    
                    check_green_won()
                elif(g2y<20):
                    g2y=g2y+distance


                    
                    
            elif(g2x>20 and g2x<60 and g2y>60):
                print("greenright")
                g2y=g2y-distance
                print("g2y=",g2y,"g2x=",g2x)
                if(round(g2x,0)==sengreen1x and g2y<sengreen1y):
                    rem=abs(sengreen1y-g2y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (g2x,g2y)=(senyellow2x,senyellow2y)
                    move_green(moving_key)


        
            elif(g2x>60 and g2y>20 and g2y<60):
                print("yellowup")
                if(round(g2x,0)==yellow2x and round(g2y,0)==yellow2y):
                    g2y=g2y-distance
                    if(round(g2x,0)==yellow1x and g2y<yellow1y):
                        rem=abs(yellow1y-g2y)
                        (g2x,g2y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                else:
                    g2x=g2x+distance

                if(g2x>yellow2x and round(g2y,0)==yellow2y):
                    rem=abs(g2x-yellow2x)
                    (g2x,g2y)=(yellow2x,yellow2y)
                    move_green(moving_key)
    
            elif(g2x>60 and g2y>-20 and g2y<20):
                print("yellowmid")
                g2y=g2y-distance
                if(round(g2x,0)==yellow1x and g2y<yellow1y):
                        rem=abs(yellow1y-g2y)
                        (g2x,g2y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                        
                        
            elif(g2x>60 and g2y<-20 and g2y>-60):
                print("yellowdown")
                g2x=g2x-distance
                if(g2x<senyellow1x and round(g2y,0)==senyellow1y):
                    rem=abs(g2x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (g2x,g2y)=(senblue2x,senblue2y)
                    move_green(moving_key)


            elif(g2x>20 and g2x<60 and g2y<-60):
                print("blueright")
                if(round(g2x,0)==blue2x and round(g2y,0)==blue2y):
                    g2x=g2x-distance
                    if(g2x<blue1x and round(g2y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(g2x-blue1x)
                        (g2x,g2y)=(blue1x,blue1y)
                        move_green(moving_key)
                    
                else:
                    g2y=g2y-distance

                if(round(g2x,0)==blue2x and g2y<blue2y):
                    rem=abs(blue2y-g2y)
                    (g2x,g2y)=(blue2x,blue2y)
                    move_green(moving_key)

            elif(g2x>-20 and g2x<20 and g2y<-20):
                print("bluemid")                               
                g2x=g2x-distance
                if(g2x<blue1x and round(g2y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(g2x-blue1x)
                    (g2x,g2y)=(blue1x,blue1y)
                    move_green(moving_key)

                
            elif(g2x<-20 and g2x>-60 and g2y<-20):
                print("blueleft")
                g2y=g2y+distance
                if(round(g2x,0)==senblue1x and g2y>senblue1y):
                    rem=abs(g2y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (g2x,g2y)=(senred2x,senred2y)
                    move_green(moving_key)                        #end of checking sensitive points
            g2.clear()
            g2.goto(g2x,g2y)

        elif(moving_key==3 and g3.isvisible()):
            if(g3x<-60 and g3y>20 and g3y<60):
                print("redup")
                g3x=g3x+distance
                print("g3y=",g3y,"g3x=",g3x)
                if(g3x>senred1x and round(g3y,0)==senred1y):
                    rem=abs(g3x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (g3x,g3y)=(sengreen2x,sengreen2y)
                    move_green(moving_key)

            elif(g3x<-60 and g3y<20 and g3y>-20):
                print("redmid")
                g3y=g3y+distance
                if(round(g3x,0)==red1x and g3y>red1y):
                        rem=abs(red1y-g3y)
                        (g3x,g3y)=(red1x,red1y)
                        move_green(moving_key)




            elif(g3x<-60 and g3y<-20 and g3y>-60):
                print("reddown")
                if(round(g3x,0)==red2x and round(g3y,0)==red2y):
                    g3y=g3y+distance
                    if(round(g3x,0)==red1x and g3y>red1y):
                        rem=abs(g3y-red1y)
                        (g3x,g3y)=(red1x,red1y)
                        move_green(moving_key)
                else:
                    g3x=g3x-distance
                if(g3x<red2x and round(g3y,0)==red2y):
                    rem=abs(red2x-g3x)
                    (g3x,g3y)=(red2x,red2y)
                    move_green(moving_key)
            elif(g3x<-20 and g3x>-60 and g3y>60):
                print("greenleft")
                print("g3y=",g3y,"g3x=",g3x)
                if(round(g3x,0)==green2x and round(g3y,0)==green2y):
                    g3x=g3x+distance
                    print("g3y=",g3y,"g3x=",g3x)
                    if(g3x>endgreenx and round(g3y,0)==endgreeny):
                        rem=abs(g3x-endgreenx)
                        (g3x,g3y)=(endgreenx,endgreeny)
                        move_green(moving_key)
                else:    
                    g3y=g3y+distance   
                if(round(g3x,0)==green2x and g3y>green2y):            
                    rem=abs(g3y-green2y) #deleted 40
                    (g3x,g3y)=(green2x,green2y)
                    move_green(moving_key)

            elif(g3x<20 and g3x>-20 and g3y>60):
                print("greenmid")
                #if(g3x==endgreenx and g3y==endgreeny):            
                g3y=g3y-distance
                print("g3y=",g3y,"g3x=",g3x)
                if(g3y<60 and g3y>20):
                    print("g3 won")
                    time.sleep(1)
                    g3.clear()
                    g3.hideturtle()
                    
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Green token reached home")
                    re_roll=True
                    check_green_won()
                elif(g3y<20):
                    g3y=g3y+distance


                    
                    
            elif(g3x>20 and g3x<60 and g3y>60):
                print("greenright")
                g3y=g3y-distance
                print("g3y=",g3y,"g3x=",g3x)
                if(round(g3x,0)==sengreen1x and g3y<sengreen1y):
                    rem=abs(sengreen1y-g3y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (g3x,g3y)=(senyellow2x,senyellow2y)
                    move_green(moving_key)
        
            elif(g3x>60 and g3y>20 and g3y<60):
                print("yellowup")
                if(round(g3x,0)==yellow2x and round(g3y,0)==yellow2y):
                    g3y=g3y-distance
                    if(round(g3x,0)==yellow1x and g3y<yellow1y):
                        rem=abs(yellow1y-g3y)
                        (g3x,g3y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                else:
                    g3x=g3x+distance

                if(g3x>yellow2x and round(g3y,0)==yellow2y):
                    rem=abs(g3x-yellow2x)
                    (g3x,g3y)=(yellow2x,yellow2y)
                    move_green(moving_key)
    
            elif(g3x>60 and g3y>-20 and g3y<20):
                print("yellowmid")
                g3y=g3y-distance
                if(round(g3x,0)==yellow1x and g3y<yellow1y):
                        rem=abs(yellow1y-g3y)
                        (g3x,g3y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                        
                        
            elif(g3x>60 and g3y<-20 and g3y>-60):
                print("yellowdown")
                g3x=g3x-distance
                if(g3x<senyellow1x and round(g3y,0)==senyellow1y):
                    rem=abs(g3x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (g3x,g3y)=(senblue2x,senblue2y)
                    move_green(moving_key)


            elif(g3x>20 and g3x<60 and g3y<-60):
                print("blueright")
                if(round(g3x,0)==blue2x and round(g3y,0)==blue2y):
                    g3x=g3x-distance
                    if(g3x<blue1x and round(g3y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(g3x-blue1x)
                        (g3x,g3y)=(blue1x,blue1y)
                        move_green(moving_key)
                    
                else:
                    g3y=g3y-distance

                if(round(g3x,0)==blue2x and g3y<blue2y):
                    rem=abs(blue2y-g3y)
                    (g3x,g3y)=(blue2x,blue2y)
                    move_green(moving_key)

            elif(g3x>-20 and g3x<20 and g3y<-20):
                print("bluemid")                               
                g3x=g3x-distance
                if(g3x<blue1x and round(g3y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(g3x-blue1x)
                    (g3x,g3y)=(blue1x,blue1y)
                    move_green(moving_key)

                
            elif(g3x<-20 and g3x>-60 and g3y<-20):
                print("blueleft")
                g3y=g3y+distance
                if(round(g3x,0)==senblue1x and g3y>senblue1y):
                    rem=abs(g3y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (g3x,g3y)=(senred2x,senred2y)
                    move_green(moving_key)                        #end of checking sensitive points
            g3.clear()
            g3.goto(g3x,g3y)

        if(moving_key==4 and g4.isvisible()):
            if(g4x<-60 and g4y>20 and g4y<60):
                print("redup")
                g4x=g4x+distance
                print("g4y=",g4y,"g4x=",g4x)
                if(g4x>senred1x and round(g4y,0)==senred1y):
                    rem=abs(g4x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (g4x,g4y)=(sengreen2x,sengreen2y)
                    move_green(moving_key)

            elif(g4x<-60 and g4y<20 and g4y>-20):
                print("redmid")
                g4y=g4y+distance
                if(round(g4x,0)==red1x and g4y>red1y):
                        rem=abs(red1y-g4y)
                        (g4x,g4y)=(red1x,red1y)
                        move_green(moving_key)




            elif(g4x<-60 and g4y<-20 and g4y>-60):
                print("reddown")
                if(round(g4x,0)==red2x and round(g4y,0)==red2y):
                    g4y=g4y+distance
                    if(round(g4x,0)==red1x and g4y>red1y):
                        rem=abs(g4y-red1y)
                        (g4x,g4y)=(red1x,red1y)
                        move_green(moving_key)
                else:
                    g4x=g4x-distance
                if(g4x<red2x and round(g4y,0)==red2y):
                    rem=abs(red2x-g4x)
                    (g4x,g4y)=(red2x,red2y)
                    move_green(moving_key)
            elif(g4x<-20 and g4x>-60 and g4y>60):
                print("greenleft")
                print("g4y=",g4y,"g4x=",g4x)
                if(round(g4x,0)==green2x and round(g4y,0)==green2y):
                    g4x=g4x+distance
                    print("g4y=",g4y,"g4x=",g4x)
                    if(g4x>endgreenx and round(g4y,0)==endgreeny):
                        rem=abs(g4x-endgreenx)
                        (g4x,g4y)=(endgreenx,endgreeny)
                        move_green(moving_key)
                else:    
                    g4y=g4y+distance   
                if(round(g4x,0)==green2x and g4y>green2y):            
                    rem=abs(g4y-green2y) #deleted 40
                    (g4x,g4y)=(green2x,green2y)
                    move_green(moving_key)

            elif(g4x<20 and g4x>-20 and g4y>60):
                print("greenmid")
                #if(g4x==endgreenx and g4y==endgreeny):            
                g4y=g4y-distance
                print("g4y=",g4y,"g4x=",g4x)
                if(g4y<60 and g4y>20):
                    print("g4 won")
                    time.sleep(1)
                    g4.clear()
                    g4.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Green token reached home")
                    re_roll=True
                    
                    check_green_won()
                elif(g4y<20):
                    g4y=g4y+distance


                    
                    
            elif(g4x>20 and g4x<60 and g4y>60):
                print("greenright")
                g4y=g4y-distance
                print("g4y=",g4y,"g4x=",g4x)
                if(round(g4x,0)==sengreen1x and g4y<sengreen1y):
                    rem=abs(sengreen1y-g4y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (g4x,g4y)=(senyellow2x,senyellow2y)
                    move_green(moving_key)
        
            elif(g4x>60 and g4y>20 and g4y<60):
                print("yellowup")
                if(round(g4x,0)==yellow2x and round(g4y,0)==yellow2y):
                    g4y=g4y-distance
                    if(round(g4x,0)==yellow1x and g4y<yellow1y):
                        rem=abs(yellow1y-g4y)
                        (g4x,g4y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                else:
                    g4x=g4x+distance

                if(g4x>yellow2x and round(g4y,0)==yellow2y):
                    rem=abs(g4x-yellow2x)
                    (g4x,g4y)=(yellow2x,yellow2y)
                    move_green(moving_key)
    
            elif(g4x>60 and g4y>-20 and g4y<20):
                print("yellowmid")
                g4y=g4y-distance
                if(round(g4x,0)==yellow1x and g4y<yellow1y):
                        rem=abs(yellow1y-g4y)
                        (g4x,g4y)=(yellow1x,yellow1y)
                        move_green(moving_key)
                        
                        
            elif(g4x>60 and g4y<-20 and g4y>-60):
                print("yellowdown")
                g4x=g4x-distance
                if(g4x<senyellow1x and round(g4y,0)==senyellow1y):
                    rem=abs(g4x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (g4x,g4y)=(senblue2x,senblue2y)
                    move_green(moving_key)


            elif(g4x>20 and g4x<60 and g4y<-60):
                print("blueright")
                if(round(g4x,0)==blue2x and round(g4y,0)==blue2y):
                    g4x=g4x-distance
                    if(g4x<blue1x and round(g4y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(g4x-blue1x)
                        (g4x,g4y)=(blue1x,blue1y)
                        move_green(moving_key)
                    
                else:
                    g4y=g4y-distance

                if(round(g4x,0)==blue2x and g4y<blue2y):
                    rem=abs(blue2y-g4y)
                    (g4x,g4y)=(blue2x,blue2y)
                    move_green(moving_key)

            elif(g4x>-20 and g4x<20 and g4y<-20):
                print("bluemid")                               
                g4x=g4x-distance
                if(g4x<blue1x and round(g4y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(g4x-blue1x)
                    (g4x,g4y)=(blue1x,blue1y)
                    move_green(moving_key)

                
            elif(g4x<-20 and g4x>-60 and g4y<-20):
                print("blueleft")
                g4y=g4y+distance
                if(round(g4x,0)==senblue1x and g4y>senblue1y):
                    rem=abs(g4y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (g4x,g4y)=(senred2x,senred2y)
                    move_green(moving_key)                        #end of checking sensitive points
            g4.clear()
            g4.goto(g4x,g4y)


def play_green():
    global moving_key,can_clash
    moving_key=0
    global  g1x,g1y,g2x,g2y,g3x,g3y,g4x,g4y
    global all_green_start_pos,give_birth_green,dice
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global re_roll





    show_green_turn()

    #numinput("Rolling the dice","Press enter to roll the dice",1)
    dice=roll_dice()
    show_dice(dice)
    all_green_start_pos=check_green_start_pos()

    turn.write("       Green's   Turn ",False,align='left',font=("Times new roman",22,"bold"))

    print("all_green_start_pos",all_green_start_pos)
    if(dice!=6 and all_green_start_pos):
        time.sleep(3/9)
        d.clear()
        pass
    elif(dice==6):
        os.system("play Audio/positive.wav&")
        make_your_move()
        
        if(moving_key==1 and g1.isvisible() and (g1x==175) and (g1y==245)):
            give_birth_green=True
        elif(moving_key==2 and g2.isvisible() and (g2x==245) and (g2y==245)):
            give_birth_green=True
        elif(moving_key==3 and g3.isvisible() and (g3x==175) and (g3y==175)):
            give_birth_green=True
        elif(moving_key==4 and g4.isvisible() and g4x==245 and (g4y==175)):
            give_birth_green=True
        else:
            give_birth_green=False
        move_green(moving_key)
        re_roll=True
        d.clear()
    elif(not all_green_start_pos):
        make_your_move()
        give_birth_green=False
        move_green(moving_key)
        d.clear()
    can_clash=can_clash_green()
    if(can_clash):
        clash_green(moving_key)

    turn.undo()
    if(re_roll):
        d.clear()
        re_roll=False
        play_green()
    



def move_blue(moving_key):
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global all_blue_start_pos,give_birth_blue
    global dice,rem
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted
    global endredx,endredy,endgreenx,endgreeny,endyellowx,endyellowy,endbluex,endbluey
    global re_roll
    if(give_birth_blue):
        os.system("play Audio/load.wav&")
        if(moving_key==1 and b1.isvisible()):
            (b1x,b1y)=(-40,-280)
            b1.clear()
            b1.goto(b1x,b1y)
        elif(moving_key==2 and b2.isvisible()):
            (b2x,b2y)=(-40,-280)
            b2.clear()
            b2.goto(b2x,b2y)
        elif(moving_key==3 and b3.isvisible()):
            (b3x,b3y)=(-40,-280)
            b3.clear()
            b3.goto(b3x,b3y)
        elif(moving_key==4 and b4.isvisible()):
            (b4x,b4y)=(-40,-280)
            b4.clear()
            b4.goto(b4x,b4y)

    else:
        if(rem==0):
            print("distance")
            distance=40*dice
        else:
            print("rem",rem)
            distance=rem
            rem=0
        if(moving_key==1 and b1.isvisible()):
            if(b1x<-60 and b1y>20 and b1y<60):
                print("redup")
                b1x=b1x+distance
                print("b1y=",b1y,"b1x=",b1x)
                if(b1x>senred1x and round(b1y,0)==senred1y):
                    rem=abs(b1x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (b1x,b1y)=(sengreen2x,sengreen2y)
                    move_blue(moving_key)

            elif(b1x<-60 and b1y<20 and b1y>-20):
                print("redmid")
                b1y=b1y+distance
                if(round(b1x,0)==red1x and b1y>red1y):
                        rem=abs(red1y-b1y)
                        (b1x,b1y)=(red1x,red1y)
                        move_blue(moving_key)




            elif(b1x<-60 and b1y<-20 and b1y>-60):
                print("reddown")
                if(round(b1x,0)==red2x and round(b1y,0)==red2y):
                    b1y=b1y+distance
                    if(round(b1x,0)==red1x and b1y>red1y):
                        rem=abs(b1y-red1y)
                        (b1x,b1y)=(red1x,red1y)
                        move_blue(moving_key)
                else:
                    b1x=b1x-distance
                if(b1x<red2x and round(b1y,0)==red2y):
                    rem=abs(red2x-b1x)
                    (b1x,b1y)=(red2x,red2y)
                    move_blue(moving_key)


            elif(b1x<-20 and b1x>-60 and b1y>60):
                print("greenleft")
                print("b1y=",b1y,"b1x=",b1x)
                if(round(b1x,0)==green2x and round(b1y,0)==green2y):
                    b1x=b1x+distance
                    print("b1y=",b1y,"b1x=",b1x)
                    if(b1x>green1x and round(b1y,0)==green1y):
                        rem=abs(b1x-green1x)
                        (b1x,b1y)=(green1x,green1y)
                        move_blue(moving_key)
                else:    
                    b1y=b1y+distance   
                if(round(b1x,0)==green2x and b1y>green2y):            
                    rem=abs(b1y-green2y) #deleted 40
                    (b1x,b1y)=(green2x,green2y)
                    move_blue(moving_key)

            elif(b1x<20 and b1x>-20 and b1y>60):
                print("greenmid")
                #if(b1x==endgreenx and b1y==endgreeny):
                print("reached endgreen")
                b1x=b1x+distance
                if(b1x>green1x and round(b1y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(b1x-green1x)
                    (b1x,b1y)=(green1x,green1y)
                    move_blue(moving_key)
                    
            elif(b1x>20 and b1x<60 and b1y>60):
                print("greenright")
                b1y=b1y-distance
                print("b1y=",b1y,"b1x=",b1x)
                if(round(b1x,0)==sengreen1x and b1y<sengreen1y):
                    rem=abs(sengreen1y-b1y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (b1x,b1y)=(senyellow2x,senyellow2y)
                    move_blue(moving_key)

        
            elif(b1x>60 and b1y>20 and b1y<60):
                print("yellowup")
                if(round(b1x,0)==yellow2x and round(b1y,0)==yellow2y):
                    b1y=b1y-distance
                    if(round(b1x,0)==yellow1x and b1y<yellow1y):
                        rem=abs(yellow1y-b1y)
                        (b1x,b1y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                else:
                    b1x=b1x+distance

                if(b1x>yellow2x and round(b1y,0)==yellow2y):
                    rem=abs(b1x-yellow2x)
                    (b1x,b1y)=(yellow2x,yellow2y)
                    move_blue(moving_key)
    
            elif(b1x>60 and b1y>-20 and b1y<20):
                print("yellowmid")
                b1y=b1y-distance
                if(round(b1x,0)==yellow1x and b1y<yellow1y):
                        rem=abs(yellow1y-b1y)
                        (b1x,b1y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                        
                        
            elif(b1x>60 and b1y<-20 and b1y>-60):
                print("yellowdown")
                b1x=b1x-distance
                if(b1x<senyellow1x and round(b1y,0)==senyellow1y):
                    rem=abs(b1x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (b1x,b1y)=(senblue2x,senblue2y)
                    move_blue(moving_key)


            elif(b1x>20 and b1x<60 and b1y<-60):
                print("blueright")
                if(round(b1x,0)==blue2x and round(b1y,0)==blue2y):
                    b1x=b1x-distance
                    if(b1x<endbluex and round(b1y,0)==endbluey):
                        print("endblue")
                        rem=abs(b1x-endbluex)
                        (b1x,b1y)=(endbluex,endbluey)
                        move_blue(moving_key)
                    
                else:
                    b1y=b1y-distance

                if(round(b1x,0)==blue2x and b1y<blue2y):
                    rem=abs(blue2y-b1y)
                    (b1x,b1y)=(blue2x,blue2y)
                    move_blue(moving_key)

            elif(b1x>-20 and b1x<20 and b1y<-20):
                print("bluemid")                               
                b1y=b1y+distance
                print("b1y=",g1y,"b1x=",g1x)
                if(b1y>-60 and b1y<-20):
                    print("g1won")
                    time.sleep(1)
                    b1.clear()
                    b1.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Blue token reached home")
                    re_roll=True
                    
                    check_blue_won()
                elif(b1y>-20):
                    b1y=b1y-distance
                    
                
            elif(b1x<-20 and b1x>-60 and b1y<-20):
                print("blueleft")
                b1y=b1y+distance
                if(round(b1x,0)==senblue1x and b1y>senblue1y):
                    rem=abs(b1y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (b1x,b1y)=(senred2x,senred2y)
                    move_blue(moving_key)                        #end of checking sensitive points
            b1.clear()
            b1.goto(b1x,b1y)
        elif(moving_key==2 and b2.isvisible()):
            if(b2x<-60 and b2y>20 and b2y<60):
                print("redup")
                b2x=b2x+distance
                print("b2y=",b2y,"b2x=",b2x)
                if(b2x>senred1x and round(b2y,0)==senred1y):
                    rem=abs(b2x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (b2x,b2y)=(sengreen2x,sengreen2y)
                    move_blue(moving_key)

            elif(b2x<-60 and b2y<20 and b2y>-20):
                print("redmid")
                b2y=b2y+distance
                if(round(b2x,0)==red1x and b2y>red1y):
                        rem=abs(red1y-b2y)
                        (b2x,b2y)=(red1x,red1y)
                        move_blue(moving_key)




            elif(b2x<-60 and b2y<-20 and b2y>-60):
                print("reddown")
                if(round(b2x,0)==red2x and round(b2y,0)==red2y):
                    b2y=b2y+distance
                    if(round(b2x,0)==red1x and b2y>red1y):
                        rem=abs(b2y-red1y)
                        (b2x,b2y)=(red1x,red1y)
                        move_blue(moving_key)
                else:
                    b2x=b2x-distance
                if(b2x<red2x and round(b2y,0)==red2y):
                    rem=abs(red2x-b2x)
                    (b2x,b2y)=(red2x,red2y)
                    move_blue(moving_key)


            elif(b2x<-20 and b2x>-60 and b2y>60):
                print("greenleft")
                print("b2y=",b2y,"b2x=",b2x)
                if(round(b2x,0)==green2x and round(b2y,0)==green2y):
                    b2x=b2x+distance
                    print("b2y=",b2y,"b2x=",b2x)
                    if(b2x>green1x and round(b2y,0)==green1y):
                        rem=abs(b2x-green1x)
                        (b2x,b2y)=(green1x,green1y)
                        move_blue(moving_key)
                else:    
                    b2y=b2y+distance   
                if(round(b2x,0)==green2x and b2y>green2y):            
                    rem=abs(b2y-green2y) #deleted 40
                    (b2x,b2y)=(green2x,green2y)
                    move_blue(moving_key)

            elif(b2x<20 and b2x>-20 and b2y>60):
                print("greenmid")
                #if(b2x==endgreenx and b2y==endgreeny):
                print("reached endgreen")
                b2x=b2x+distance
                if(b2x>green1x and round(b2y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(b2x-green1x)
                    (b2x,b2y)=(green1x,green1y)
                    move_blue(moving_key)
                    
            elif(b2x>20 and b2x<60 and b2y>60):
                print("greenright")
                b2y=b2y-distance
                print("b2y=",b2y,"b2x=",b2x)
                if(round(b2x,0)==sengreen1x and b2y<sengreen1y):
                    rem=abs(sengreen1y-b2y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (b2x,b2y)=(senyellow2x,senyellow2y)
                    move_blue(moving_key)

        
            elif(b2x>60 and b2y>20 and b2y<60):
                print("yellowup")
                if(round(b2x,0)==yellow2x and round(b2y,0)==yellow2y):
                    b2y=b2y-distance
                    if(round(b2x,0)==yellow1x and b2y<yellow1y):
                        rem=abs(yellow1y-b2y)
                        (b2x,b2y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                else:
                    b2x=b2x+distance

                if(b2x>yellow2x and round(b2y,0)==yellow2y):
                    rem=abs(b2x-yellow2x)
                    (b2x,b2y)=(yellow2x,yellow2y)
                    move_blue(moving_key)
    
            elif(b2x>60 and b2y>-20 and b2y<20):
                print("yellowmid")
                b2y=b2y-distance
                if(round(b2x,0)==yellow1x and b2y<yellow1y):
                        rem=abs(yellow1y-b2y)
                        (b2x,b2y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                        
                        
            elif(b2x>60 and b2y<-20 and b2y>-60):
                print("yellowdown")
                b2x=b2x-distance
                if(b2x<senyellow1x and round(b2y,0)==senyellow1y):
                    rem=abs(b2x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (b2x,b2y)=(senblue2x,senblue2y)
                    move_blue(moving_key)


            elif(b2x>20 and b2x<60 and b2y<-60):
                print("blueright")
                if(round(b2x,0)==blue2x and round(b2y,0)==blue2y):
                    b2x=b2x-distance
                    if(b2x<endbluex and round(b2y,0)==endbluey):
                        print("endblue")
                        rem=abs(b2x-endbluex)
                        (b2x,b2y)=(endbluex,endbluey)
                        move_blue(moving_key)
                    
                else:
                    b2y=b2y-distance

                if(round(b2x,0)==blue2x and b2y<blue2y):
                    rem=abs(blue2y-b2y)
                    (b2x,b2y)=(blue2x,blue2y)
                    move_blue(moving_key)

            elif(b2x>-20 and b2x<20 and b2y<-20):
                print("bluemid")                               
                b2y=b2y+distance
                print("b2y=",g1y,"b2x=",g1x)
                if(b2y>-60 and b2y<-20):
                    print("b2won")
                    time.sleep(1)
                    b2.clear()
                    b2.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Blue token reached home")
                    re_roll=True
                    
                    check_blue_won()
                elif(b2y>-20):
                    b2y=b2y-distance
                    
                
            elif(b2x<-20 and b2x>-60 and b2y<-20):
                print("blueleft")
                b2y=b2y+distance
                if(round(b2x,0)==senblue1x and b2y>senblue1y):
                    rem=abs(b2y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (b2x,b2y)=(senred2x,senred2y)
                    move_blue(moving_key)                        #end of checking sensitive points
            b2.clear()
            b2.goto(b2x,b2y)

        elif(moving_key==3 and b3.isvisible()):
            if(b3x<-60 and b3y>20 and b3y<60):
                print("redup")
                b3x=b3x+distance
                print("b3y=",b3y,"b3x=",b3x)
                if(b3x>senred1x and round(b3y,0)==senred1y):
                    rem=abs(b3x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (b3x,b3y)=(sengreen2x,sengreen2y)
                    move_blue(moving_key)

            elif(b3x<-60 and b3y<20 and b3y>-20):
                print("redmid")
                b3y=b3y+distance
                if(round(b3x,0)==red1x and b3y>red1y):
                        rem=abs(red1y-b3y)
                        (b3x,b3y)=(red1x,red1y)
                        move_blue(moving_key)




            elif(b3x<-60 and b3y<-20 and b3y>-60):
                print("reddown")
                if(round(b3x,0)==red2x and round(b3y,0)==red2y):
                    b3y=b3y+distance
                    if(round(b3x,0)==red1x and b3y>red1y):
                        rem=abs(b3y-red1y)
                        (b3x,b3y)=(red1x,red1y)
                        move_blue(moving_key)
                else:
                    b3x=b3x-distance
                if(b3x<red2x and round(b3y,0)==red2y):
                    rem=abs(red2x-b3x)
                    (b3x,b3y)=(red2x,red2y)
                    move_blue(moving_key)


            elif(b3x<-20 and b3x>-60 and b3y>60):
                print("greenleft")
                print("b3y=",b3y,"b3x=",b3x)
                if(round(b3x,0)==green2x and round(b3y,0)==green2y):
                    b3x=b3x+distance
                    print("b3y=",b3y,"b3x=",b3x)
                    if(b3x>green1x and round(b3y,0)==green1y):
                        rem=abs(b3x-green1x)
                        (b3x,b3y)=(green1x,green1y)
                        move_blue(moving_key)
                else:    
                    b3y=b3y+distance   
                if(round(b3x,0)==green2x and b3y>green2y):            
                    rem=abs(b3y-green2y) #deleted 40
                    (b3x,b3y)=(green2x,green2y)
                    move_blue(moving_key)

            elif(b3x<20 and b3x>-20 and b3y>60):
                print("greenmid")
                #if(b3x==endgreenx and b3y==endgreeny):
                print("reached endgreen")
                b3x=b3x+distance
                if(b3x>green1x and round(b3y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(b3x-green1x)
                    (b3x,b3y)=(green1x,green1y)
                    move_blue(moving_key)
                    
            elif(b3x>20 and b3x<60 and b3y>60):
                print("greenright")
                b3y=b3y-distance
                print("b3y=",b3y,"b3x=",b3x)
                if(round(b3x,0)==sengreen1x and b3y<sengreen1y):
                    rem=abs(sengreen1y-b3y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (b3x,b3y)=(senyellow2x,senyellow2y)
                    move_blue(moving_key)

        
            elif(b3x>60 and b3y>20 and b3y<60):
                print("yellowup")
                if(round(b3x,0)==yellow2x and round(b3y,0)==yellow2y):
                    b3y=b3y-distance
                    if(round(b3x,0)==yellow1x and b3y<yellow1y):
                        rem=abs(yellow1y-b3y)
                        (b3x,b3y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                else:
                    b3x=b3x+distance

                if(b3x>yellow2x and round(b3y,0)==yellow2y):
                    rem=abs(b3x-yellow2x)
                    (b3x,b3y)=(yellow2x,yellow2y)
                    move_blue(moving_key)
    
            elif(b3x>60 and b3y>-20 and b3y<20):
                print("yellowmid")
                b3y=b3y-distance
                if(round(b3x,0)==yellow1x and b3y<yellow1y):
                        rem=abs(yellow1y-b3y)
                        (b3x,b3y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                        
                        
            elif(b3x>60 and b3y<-20 and b3y>-60):
                print("yellowdown")
                b3x=b3x-distance
                if(b3x<senyellow1x and round(b3y,0)==senyellow1y):
                    rem=abs(b3x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (b3x,b3y)=(senblue2x,senblue2y)
                    move_blue(moving_key)


            elif(b3x>20 and b3x<60 and b3y<-60):
                print("blueright")
                if(round(b3x,0)==blue2x and round(b3y,0)==blue2y):
                    b3x=b3x-distance
                    if(b3x<endbluex and round(b3y,0)==endbluey):
                        print("endblue")
                        rem=abs(b3x-endbluex)
                        (b3x,b3y)=(endbluex,endbluey)
                        move_blue(moving_key)
                    
                else:
                    b3y=b3y-distance

                if(round(b3x,0)==blue2x and b3y<blue2y):
                    rem=abs(blue2y-b3y)
                    (b3x,b3y)=(blue2x,blue2y)
                    move_blue(moving_key)

            elif(b3x>-20 and b3x<20 and b3y<-20):
                print("bluemid")                               
                b3y=b3y+distance
                print("b3y=",g1y,"b3x=",g1x)
                if(b3y>-60 and b3y<-20):
                    print("b3won")
                    time.sleep(1)
                    b3.clear()
                    b3.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Blue token reached home")
                    re_roll=True
 
                    check_blue_won()
                elif(b3y>-20):
                    b3y=b3y-distance
                    
                
            elif(b3x<-20 and b3x>-60 and b3y<-20):
                print("blueleft")
                b3y=b3y+distance
                if(round(b3x,0)==senblue1x and b3y>senblue1y):
                    rem=abs(b3y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (b3x,b3y)=(senred2x,senred2y)
                    move_blue(moving_key)                        #end of checking sensitive points
            b3.clear()
            b3.goto(b3x,b3y)

        elif(moving_key==4 and b4.isvisible()):
            if(b4x<-60 and b4y>20 and b4y<60):
                print("redup")
                b4x=b4x+distance
                print("b4y=",b4y,"b4x=",b4x)
                if(b4x>senred1x and round(b4y,0)==senred1y):
                    rem=abs(b4x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (b4x,b4y)=(sengreen2x,sengreen2y)
                    move_blue(moving_key)

            elif(b4x<-60 and b4y<20 and b4y>-20):
                print("redmid")
                b4y=b4y+distance
                if(round(b4x,0)==red1x and b4y>red1y):
                        rem=abs(red1y-b4y)
                        (b4x,b4y)=(red1x,red1y)
                        move_blue(moving_key)




            elif(b4x<-60 and b4y<-20 and b4y>-60):
                print("reddown")
                if(round(b4x,0)==red2x and round(b4y,0)==red2y):
                    b4y=b4y+distance
                    if(round(b4x,0)==red1x and b4y>red1y):
                        rem=abs(b4y-red1y)
                        (b4x,b4y)=(red1x,red1y)
                        move_blue(moving_key)
                else:
                    b4x=b4x-distance
                if(b4x<red2x and round(b4y,0)==red2y):
                    rem=abs(red2x-b4x)
                    (b4x,b4y)=(red2x,red2y)
                    move_blue(moving_key)


            elif(b4x<-20 and b4x>-60 and b4y>60):
                print("greenleft")
                print("b4y=",b4y,"b4x=",b4x)
                if(round(b4x,0)==green2x and round(b4y,0)==green2y):
                    b4x=b4x+distance
                    print("b4y=",b4y,"b4x=",b4x)
                    if(b4x>green1x and round(b4y,0)==green1y):
                        rem=abs(b4x-green1x)
                        (b4x,b4y)=(green1x,green1y)
                        move_blue(moving_key)
                else:    
                    b4y=b4y+distance   
                if(round(b4x,0)==green2x and b4y>green2y):            
                    rem=abs(b4y-green2y) #deleted 40
                    (b4x,b4y)=(green2x,green2y)
                    move_blue(moving_key)

            elif(b4x<20 and b4x>-20 and b4y>60):
                print("greenmid")
                #if(b4x==endgreenx and b4y==endgreeny):
                print("reached endgreen")
                b4x=b4x+distance
                if(b4x>green1x and round(b4y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(b4x-green1x)
                    (b4x,b4y)=(green1x,green1y)
                    move_blue(moving_key)
                    
            elif(b4x>20 and b4x<60 and b4y>60):
                print("greenright")
                b4y=b4y-distance
                print("b4y=",b4y,"b4x=",b4x)
                if(round(b4x,0)==sengreen1x and b4y<sengreen1y):
                    rem=abs(sengreen1y-b4y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (b4x,b4y)=(senyellow2x,senyellow2y)
                    move_blue(moving_key)

        
            elif(b4x>60 and b4y>20 and b4y<60):
                print("yellowup")
                if(round(b4x,0)==yellow2x and round(b4y,0)==yellow2y):
                    b4y=b4y-distance
                    if(round(b4x,0)==yellow1x and b4y<yellow1y):
                        rem=abs(yellow1y-b4y)
                        (b4x,b4y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                else:
                    b4x=b4x+distance

                if(b4x>yellow2x and round(b4y,0)==yellow2y):
                    rem=abs(b4x-yellow2x)
                    (b4x,b4y)=(yellow2x,yellow2y)
                    move_blue(moving_key)
    
            elif(b4x>60 and b4y>-20 and b4y<20):
                print("yellowmid")
                b4y=b4y-distance
                if(round(b4x,0)==yellow1x and b4y<yellow1y):
                        rem=abs(yellow1y-b4y)
                        (b4x,b4y)=(yellow1x,yellow1y)
                        move_blue(moving_key)
                        
                        
            elif(b4x>60 and b4y<-20 and b4y>-60):
                print("yellowdown")
                b4x=b4x-distance
                if(b4x<senyellow1x and round(b4y,0)==senyellow1y):
                    rem=abs(b4x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (b4x,b4y)=(senblue2x,senblue2y)
                    move_blue(moving_key)


            elif(b4x>20 and b4x<60 and b4y<-60):
                print("blueright")
                if(round(b4x,0)==blue2x and round(b4y,0)==blue2y):
                    b4x=b4x-distance
                    if(b4x<endbluex and round(b4y,0)==endbluey):
                        print("endblue")
                        rem=abs(b4x-endbluex)
                        (b4x,b4y)=(endbluex,endbluey)
                        move_blue(moving_key)
                    
                else:
                    b4y=b4y-distance

                if(round(b4x,0)==blue2x and b4y<blue2y):
                    rem=abs(blue2y-b4y)
                    (b4x,b4y)=(blue2x,blue2y)
                    move_blue(moving_key)

            elif(b4x>-20 and b4x<20 and b4y<-20):
                print("bluemid")                               
                b4y=b4y+distance
                print("b4y=",g1y,"b4x=",g1x)
                if(b4y>-60 and b4y<-20):
                    print("b4won")
                    time.sleep(1)
                    b4.clear()
                    b4.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Blue token reached home")
                    re_roll=True

                    check_blue_won()
                elif(b4y>-20):
                    b4y=b4y-distance
                    
                
            elif(b4x<-20 and b4x>-60 and b4y<-20):
                print("blueleft")
                b4y=b4y+distance
                if(round(b4x,0)==senblue1x and b4y>senblue1y):
                    rem=abs(b4y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (b4x,b4y)=(senred2x,senred2y)
                    move_blue(moving_key)                        #end of checking sensitive points
            b4.clear()
            b4.goto(b4x,b4y)


def play_blue():
    global moving_key,can_clash
    moving_key=0
    global  b1x,b1y,b2x,b2y,b3x,b3y,b4x,b4y
    global all_blue_start_pos,give_birth_blue,dice
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global re_roll

    b1.goto(b1x,b1y)
    b2.goto(b2x,b2y)
    b3.goto(b3x,b3y)
    b4.goto(b4x,b4y)



    show_blue_turn()


    #numinput("Rolling the dice","Press enter to roll the dice",1)
    dice=roll_dice()
    show_dice(dice)
    all_blue_start_pos=check_blue_start_pos()
    turn.write("       Blue's   Turn ",False,align='left',font=("Times new roman",22,"bold"))


    print(all_blue_start_pos)
    if(dice!=6 and all_blue_start_pos):
        time.sleep(1/3)
        d.clear()
        pass
    elif(dice==6):
        os.system("play Audio/positive.wav&")
        make_your_move()
        if(moving_key==1 and b1.isvisible() and (b1x==-245) and (b1y==-175)):
            give_birth_blue=True
        elif(moving_key==2 and b2.isvisible() and (b2x==-175) and (b2y==-175)):
            give_birth_blue=True
        elif(moving_key==3 and b3.isvisible() and (b3x==-245) and (b3y==-245)):
            give_birth_blue=True
        elif(moving_key==4 and b4.isvisible() and b4x==-175 and (b4y==-245)):
            give_birth_blue=True
        else:
            give_birth_blue=False
        move_blue(moving_key)
        re_roll=True
        d.clear()
    elif(not all_blue_start_pos):
        make_your_move()
        give_birth_blue=False
        move_blue(moving_key)
        d.clear()
    can_clash=can_clash_blue()
    if(can_clash):
        clash_blue(moving_key)
    turn.undo()    
    if(re_roll):
        re_roll=False
        d.clear()
        play_blue()





#yellow plays


def move_yellow(moving_key):
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global all_yellow_start_pos,give_birth_yellow
    global dice,rem
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global redrotcompleted,greenrotcompleted,yellowrotcompleted,bluerotcompleted
    global endredx,endredy,endgreenx,endgreeny,endyellowx,endyellowy,endbluex,endbluey
    global re_roll
    if(give_birth_yellow):
        os.system("play Audio/load.wav&")
        if(moving_key==1 and y1.isvisible()):
            (y1x,y1y)=(yellow1x-40,yellow1y)
            y1.clear()
            y1.goto(y1x,y1y)
        elif(moving_key==2 and y2.isvisible()):
            (y2x,y2y)=(yellow1x-40,yellow1y)
            y2.clear()
            y2.goto(y2x,y2y)
        elif(moving_key==3 and y3.isvisible()):
            (y3x,y3y)=(yellow1x-40,yellow1y)
            y3.clear()
            y3.goto(y3x,y3y)
        elif(moving_key==4 and y4.isvisible()):
            (y4x,y4y)=(yellow1x-40,yellow1y)
            y4.clear()
            y4.goto(y4x,y4y)

    else:
        if(rem==0):
            print("distance")
            distance=40*dice
        else:
            print("rem",rem)
            distance=rem
            rem=0
        if(moving_key==1 and y1.isvisible()):
            if(y1x<-60 and y1y>20 and y1y<60):
                print("redup")
                y1x=y1x+distance
                print("y1y=",y1y,"y1x=",y1x)
                if(y1x>senred1x and round(y1y,0)==senred1y):
                    rem=abs(y1x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (y1x,y1y)=(sengreen2x,sengreen2y)
                    move_yellow(moving_key)

            elif(y1x<-60 and y1y<20 and y1y>-20):
                print("redmid")
                y1y=y1y+distance
                if(round(y1x,0)==red1x and y1y>red1y):
                        rem=abs(red1y-y1y)
                        (y1x,y1y)=(red1x,red1y)
                        move_yellow(moving_key)




            elif(y1x<-60 and y1y<-20 and y1y>-60):
                print("reddown")
                if(round(y1x,0)==red2x and round(y1y,0)==red2y):
                    y1y=y1y+distance
                    if(round(y1x,0)==endredx and y1y>endredy):
                        rem=abs(y1y-endredy)
                        (y1x,y1y)=(endredx,endredy)
                        move_yellow(moving_key)
                else:
                    y1x=y1x-distance
                if(y1x<red2x and round(y1y,0)==red2y):
                    rem=abs(red2x-y1x)
                    (y1x,y1y)=(red2x,red2y)
                    move_yellow(moving_key)
            elif(y1x<-20 and y1x>-60 and y1y>60):
                print("greenleft")
                print("y1y=",y1y,"y1x=",y1x)
                if(round(y1x,0)==green2x and round(y1y,0)==green2y):
                    y1x=y1x+distance
                    print("y1y=",y1y,"y1x=",y1x)
                    if(y1x>green1x and round(y1y,0)==green1y):
                        rem=abs(y1x-green1x)
                        (y1x,y1y)=(green1x,green1y)
                        move_yellow(moving_key)
                else:    
                    y1y=y1y+distance   
                if(round(y1x,0)==green2x and y1y>green2y):            
                    rem=abs(y1y-green2y) #deleted 40
                    (y1x,y1y)=(green2x,green2y)
                    move_yellow(moving_key)

            elif(y1x<20 and y1x>-20 and y1y>60):
                print("greenmid")
                #if(y1x==endgreenx and y1y==endgreeny):
                print("reached endgreen")
                y1x=y1x+distance
                if(y1x>green1x and round(y1y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(y1x-green1x)
                    (y1x,y1y)=(green1x,green1y)
                    move_yellow(moving_key)
                    
            elif(y1x>20 and y1x<60 and y1y>60):
                print("greenright")
                y1y=y1y-distance
                print("y1y=",y1y,"y1x=",y1x)
                if(round(y1x,0)==sengreen1x and y1y<sengreen1y):
                    rem=abs(sengreen1y-y1y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (y1x,y1y)=(senyellow2x,senyellow2y)
                    move_yellow(moving_key)
        
            elif(y1x>60 and y1y>20 and y1y<60):
                print("yellowup")
                if(round(y1x,0)==yellow2x and round(y1y,0)==yellow2y):
                    y1y=y1y-distance
                    if(round(y1x,0)==endyellowx and y1y<endyellowy):
                        rem=abs(endyellowy-y1y)
                        print("rem in boom",rem)
                        (y1x,y1y)=(endyellowx,endyellowy)
                        move_yellow(moving_key)
                else:
                    y1x=y1x+distance

                if(y1x>yellow2x and round(y1y,0)==yellow2y):
                    rem=abs(y1x-yellow2x)
                    print("rem in choom",rem)
                    (y1x,y1y)=(yellow2x,yellow2y)
                    move_yellow(moving_key)
    
            elif(y1x>60 and y1y>-20 and y1y<20):
                print("yellowmid")
                y1x=y1x-distance
                print("y1y=",y1y,"y1x=",y1x)
                if(y1x<60 and y1x>20):
                    print("y1 won")
                    time.sleep(1)
                    y1.clear()
                    y1.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Yellow token reached home")
                    re_roll=True

                    check_yellow_won()
                elif(y1x<20):
                    y1x=y1x+distance
                        
                        
            elif(y1x>60 and y1y<-20 and y1y>-60):
                print("yellowdown")
                y1x=y1x-distance
                if(y1x<senyellow1x and round(y1y,0)==senyellow1y):
                    rem=abs(y1x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (y1x,y1y)=(senblue2x,senblue2y)
                    move_yellow(moving_key)


            elif(y1x>20 and y1x<60 and y1y<-60):
                print("blueright")
                if(round(y1x,0)==blue2x and round(y1y,0)==blue2y):
                    y1x=y1x-distance
                    if(y1x<blue1x and round(y1y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(y1x-blue1x)
                        (y1x,y1y)=(blue1x,blue1y)
                        move_yellow(moving_key)
                    
                else:
                    y1y=y1y-distance

                if(round(y1x,0)==blue2x and y1y<blue2y):
                    rem=abs(blue2y-y1y)
                    (y1x,y1y)=(blue2x,blue2y)
                    move_yellow(moving_key)

            elif(y1x>-20 and y1x<20 and y1y<-20):
                print("bluemid")                               
                y1x=y1x-distance
                if(y1x<blue1x and round(y1y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(y1x-blue1x)
                    (y1x,y1y)=(blue1x,blue1y)
                    move_yellow(moving_key)

                
            elif(y1x<-20 and y1x>-60 and y1y<-20):
                print("blueleft")
                y1y=y1y+distance
                if(round(y1x,0)==senblue1x and y1y>senblue1y):
                    rem=abs(y1y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (y1x,y1y)=(senred2x,senred2y)
                    move_yellow(moving_key)                        #end of checking sensitive points
            y1.clear()
            y1.goto(y1x,y1y)



        elif(moving_key==2 and y2.isvisible()):
            if(y2x<-60 and y2y>20 and y2y<60):
                print("redup")
                y2x=y2x+distance
                print("y2y=",y2y,"y2x=",y2x)
                if(y2x>senred1x and round(y2y,0)==senred1y):
                    rem=abs(y2x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (y2x,y2y)=(sengreen2x,sengreen2y)
                    move_yellow(moving_key)

            elif(y2x<-60 and y2y<20 and y2y>-20):
                print("redmid")
                y2y=y2y+distance
                if(round(y2x,0)==red1x and y2y>red1y):
                        rem=abs(red1y-y2y)
                        (y2x,y2y)=(red1x,red1y)
                        move_yellow(moving_key)




            elif(y2x<-60 and y2y<-20 and y2y>-60):
                print("reddown")
                if(round(y2x,0)==red2x and round(y2y,0)==red2y):
                    y2y=y2y+distance
                    if(round(y2x,0)==endredx and y2y>endredy):
                        rem=abs(y2y-endredy)
                        (y2x,y2y)=(endredx,endredy)
                        move_yellow(moving_key)
                else:
                    y2x=y2x-distance
                if(y2x<red2x and round(y2y,0)==red2y):
                    rem=abs(red2x-y2x)
                    (y2x,y2y)=(red2x,red2y)
                    move_yellow(moving_key)
            elif(y2x<-20 and y2x>-60 and y2y>60):
                print("greenleft")
                print("y2y=",y2y,"y2x=",y2x)
                if(round(y2x,0)==green2x and round(y2y,0)==green2y):
                    y2x=y2x+distance
                    print("y2y=",y2y,"y2x=",y2x)
                    if(y2x>green1x and round(y2y,0)==green1y):
                        rem=abs(y2x-green1x)
                        (y2x,y2y)=(green1x,green1y)
                        move_yellow(moving_key)
                else:    
                    y2y=y2y+distance   
                if(round(y2x,0)==green2x and y2y>green2y):            
                    rem=abs(y2y-green2y) #deleted 40
                    (y2x,y2y)=(green2x,green2y)
                    move_yellow(moving_key)

            elif(y2x<20 and y2x>-20 and y2y>60):
                print("greenmid")
                #if(y2x==endgreenx and y2y==endgreeny):
                print("reached endgreen")
                y2x=y2x+distance
                if(y2x>green1x and round(y2y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(y2x-green1x)
                    (y2x,y2y)=(green1x,green1y)
                    move_yellow(moving_key)
                    
            elif(y2x>20 and y2x<60 and y2y>60):
                print("greenright")
                y2y=y2y-distance
                print("y2y=",y2y,"y2x=",y2x)
                if(round(y2x,0)==sengreen1x and y2y<sengreen1y):
                    rem=abs(sengreen1y-y2y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (y2x,y2y)=(senyellow2x,senyellow2y)
                    move_yellow(moving_key)
        
            elif(y2x>60 and y2y>20 and y2y<60):
                print("yellowup")
                if(round(y2x,0)==yellow2x and round(y2y,0)==yellow2y):
                    y2y=y2y-distance
                    if(round(y2x,0)==endyellowx and y2y<endyellowy):
                        rem=abs(endyellowy-y2y)
                        print("rem in boom",rem)
                        (y2x,y2y)=(endyellowx,endyellowy)
                        move_yellow(moving_key)
                else:
                    y2x=y2x+distance

                if(y2x>yellow2x and round(y2y,0)==yellow2y):
                    rem=abs(y2x-yellow2x)
                    print("rem in choom",rem)
                    (y2x,y2y)=(yellow2x,yellow2y)
                    move_yellow(moving_key)
    
            elif(y2x>60 and y2y>-20 and y2y<20):
                print("yellowmid")
                y2x=y2x-distance
                print("y2y=",y2y,"y2x=",y2x)
                if(y2x<60 and y2x>20):
                    print("y2 won")
                    time.sleep(1)
                    y2.clear()
                    y2.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Yellow token reached home")
                    re_roll=True

                    check_yellow_won()
                elif(y2x<20):
                    y2x=y2x+distance
                        
                        
            elif(y2x>60 and y2y<-20 and y2y>-60):
                print("yellowdown")
                y2x=y2x-distance
                if(y2x<senyellow1x and round(y2y,0)==senyellow1y):
                    rem=abs(y2x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (y2x,y2y)=(senblue2x,senblue2y)
                    move_yellow(moving_key)


            elif(y2x>20 and y2x<60 and y2y<-60):
                print("blueright")
                if(round(y2x,0)==blue2x and round(y2y,0)==blue2y):
                    y2x=y2x-distance
                    if(y2x<blue1x and round(y2y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(y2x-blue1x)
                        (y2x,y2y)=(blue1x,blue1y)
                        move_yellow(moving_key)
                    
                else:
                    y2y=y2y-distance

                if(round(y2x,0)==blue2x and y2y<blue2y):
                    rem=abs(blue2y-y2y)
                    (y2x,y2y)=(blue2x,blue2y)
                    move_yellow(moving_key)

            elif(y2x>-20 and y2x<20 and y2y<-20):
                print("bluemid")                               
                y2x=y2x-distance
                if(y2x<blue1x and round(y2y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(y2x-blue1x)
                    (y2x,y2y)=(blue1x,blue1y)
                    move_yellow(moving_key)

                
            elif(y2x<-20 and y2x>-60 and y2y<-20):
                print("blueleft")
                y2y=y2y+distance
                if(round(y2x,0)==senblue1x and y2y>senblue1y):
                    rem=abs(y2y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (y2x,y2y)=(senred2x,senred2y)
                    move_yellow(moving_key)                        #end of checking sensitive points
            y2.clear()
            y2.goto(y2x,y2y)


        elif(moving_key==3 and y3.isvisible()):
            if(y3x<-60 and y3y>20 and y3y<60):
                print("redup")
                y3x=y3x+distance
                print("y3y=",y3y,"y3x=",y3x)
                if(y3x>senred1x and round(y3y,0)==senred1y):
                    rem=abs(y3x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (y3x,y3y)=(sengreen2x,sengreen2y)
                    move_yellow(moving_key)

            elif(y3x<-60 and y3y<20 and y3y>-20):
                print("redmid")
                y3y=y3y+distance
                if(round(y3x,0)==red1x and y3y>red1y):
                        rem=abs(red1y-y3y)
                        (y3x,y3y)=(red1x,red1y)
                        move_yellow(moving_key)




            elif(y3x<-60 and y3y<-20 and y3y>-60):
                print("reddown")
                if(round(y3x,0)==red2x and round(y3y,0)==red2y):
                    y3y=y3y+distance
                    if(round(y3x,0)==endredx and y3y>endredy):
                        rem=abs(y3y-endredy)
                        (y3x,y3y)=(endredx,endredy)
                        move_yellow(moving_key)
                else:
                    y3x=y3x-distance
                if(y3x<red2x and round(y3y,0)==red2y):
                    rem=abs(red2x-y3x)
                    (y3x,y3y)=(red2x,red2y)
                    move_yellow(moving_key)
            elif(y3x<-20 and y3x>-60 and y3y>60):
                print("greenleft")
                print("y3y=",y3y,"y3x=",y3x)
                if(round(y3x,0)==green2x and round(y3y,0)==green2y):
                    y3x=y3x+distance
                    print("y3y=",y3y,"y3x=",y3x)
                    if(y3x>green1x and round(y3y,0)==green1y):
                        rem=abs(y3x-green1x)
                        (y3x,y3y)=(green1x,green1y)
                        move_yellow(moving_key)
                else:    
                    y3y=y3y+distance   
                if(round(y3x,0)==green2x and y3y>green2y):            
                    rem=abs(y3y-green2y) #deleted 40
                    (y3x,y3y)=(green2x,green2y)
                    move_yellow(moving_key)

            elif(y3x<20 and y3x>-20 and y3y>60):
                print("greenmid")
                #if(y3x==endgreenx and y3y==endgreeny):
                print("reached endgreen")
                y3x=y3x+distance
                if(y3x>green1x and round(y3y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(y3x-green1x)
                    (y3x,y3y)=(green1x,green1y)
                    move_yellow(moving_key)
                    
            elif(y3x>20 and y3x<60 and y3y>60):
                print("greenright")
                y3y=y3y-distance
                print("y3y=",y3y,"y3x=",y3x)
                if(round(y3x,0)==sengreen1x and y3y<sengreen1y):
                    rem=abs(sengreen1y-y3y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (y3x,y3y)=(senyellow2x,senyellow2y)
                    move_yellow(moving_key)
        
            elif(y3x>60 and y3y>20 and y3y<60):
                print("yellowup")
                if(round(y3x,0)==yellow2x and round(y3y,0)==yellow2y):
                    y3y=y3y-distance
                    if(round(y3x,0)==endyellowx and y3y<endyellowy):
                        rem=abs(endyellowy-y3y)
                        print("rem in boom",rem)
                        (y3x,y3y)=(endyellowx,endyellowy)
                        move_yellow(moving_key)
                else:
                    y3x=y3x+distance

                if(y3x>yellow2x and round(y3y,0)==yellow2y):
                    rem=abs(y3x-yellow2x)
                    print("rem in choom",rem)
                    (y3x,y3y)=(yellow2x,yellow2y)
                    move_yellow(moving_key)
    
            elif(y3x>60 and y3y>-20 and y3y<20):
                print("yellowmid")
                y3x=y3x-distance
                print("y3y=",y3y,"y3x=",y3x)
                if(y3x<60 and y3x>20):
                    print("y3 won")
                    time.sleep(1)
                    y3.clear()
                    y3.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Yellow token reached home")
                    re_roll=True

                    check_yellow_won()
                elif(y3x<20):
                    y3x=y3x+distance
                        
                        
            elif(y3x>60 and y3y<-20 and y3y>-60):
                print("yellowdown")
                y3x=y3x-distance
                if(y3x<senyellow1x and round(y3y,0)==senyellow1y):
                    rem=abs(y3x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (y3x,y3y)=(senblue2x,senblue2y)
                    move_yellow(moving_key)


            elif(y3x>20 and y3x<60 and y3y<-60):
                print("blueright")
                if(round(y3x,0)==blue2x and round(y3y,0)==blue2y):
                    y3x=y3x-distance
                    if(y3x<blue1x and round(y3y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(y3x-blue1x)
                        (y3x,y3y)=(blue1x,blue1y)
                        move_yellow(moving_key)
                    
                else:
                    y3y=y3y-distance

                if(round(y3x,0)==blue2x and y3y<blue2y):
                    rem=abs(blue2y-y3y)
                    (y3x,y3y)=(blue2x,blue2y)
                    move_yellow(moving_key)

            elif(y3x>-20 and y3x<20 and y3y<-20):
                print("bluemid")                               
                y3x=y3x-distance
                if(y3x<blue1x and round(y3y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(y3x-blue1x)
                    (y3x,y3y)=(blue1x,blue1y)
                    move_yellow(moving_key)

                
            elif(y3x<-20 and y3x>-60 and y3y<-20):
                print("blueleft")
                y3y=y3y+distance
                if(round(y3x,0)==senblue1x and y3y>senblue1y):
                    rem=abs(y3y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (y3x,y3y)=(senred2x,senred2y)
                    move_yellow(moving_key)                        #end of checking sensitive points
            y3.clear()
            y3.goto(y3x,y3y)


        elif(moving_key==4 and y4.isvisible()):
            if(y4x<-60 and y4y>20 and y4y<60):
                print("redup")
                y4x=y4x+distance
                print("y4y=",y4y,"y4x=",y4x)
                if(y4x>senred1x and round(y4y,0)==senred1y):
                    rem=abs(y4x-senred1x)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senred1")
                    (y4x,y4y)=(sengreen2x,sengreen2y)
                    move_yellow(moving_key)

            elif(y4x<-60 and y4y<20 and y4y>-20):
                print("redmid")
                y4y=y4y+distance
                if(round(y4x,0)==red1x and y4y>red1y):
                        rem=abs(red1y-y4y)
                        (y4x,y4y)=(red1x,red1y)
                        move_yellow(moving_key)




            elif(y4x<-60 and y4y<-20 and y4y>-60):
                print("reddown")
                if(round(y4x,0)==red2x and round(y4y,0)==red2y):
                    y4y=y4y+distance
                    if(round(y4x,0)==endredx and y4y>endredy):
                        rem=abs(y4y-endredy)
                        (y4x,y4y)=(endredx,endredy)
                        move_yellow(moving_key)
                else:
                    y4x=y4x-distance
                if(y4x<red2x and round(y4y,0)==red2y):
                    rem=abs(red2x-y4x)
                    (y4x,y4y)=(red2x,red2y)
                    move_yellow(moving_key)
            elif(y4x<-20 and y4x>-60 and y4y>60):
                print("greenleft")
                print("y4y=",y4y,"y4x=",y4x)
                if(round(y4x,0)==green2x and round(y4y,0)==green2y):
                    y4x=y4x+distance
                    print("y4y=",y4y,"y4x=",y4x)
                    if(y4x>green1x and round(y4y,0)==green1y):
                        rem=abs(y4x-green1x)
                        (y4x,y4y)=(green1x,green1y)
                        move_yellow(moving_key)
                else:    
                    y4y=y4y+distance   
                if(round(y4x,0)==green2x and y4y>green2y):            
                    rem=abs(y4y-green2y) #deleted 40
                    (y4x,y4y)=(green2x,green2y)
                    move_yellow(moving_key)

            elif(y4x<20 and y4x>-20 and y4y>60):
                print("greenmid")
                #if(y4x==endgreenx and y4y==endgreeny):
                print("reached endgreen")
                y4x=y4x+distance
                if(y4x>green1x and round(y4y,0)==green1y):
                    print("enhanced green1")
                    rem=abs(y4x-green1x)
                    (y4x,y4y)=(green1x,green1y)
                    move_yellow(moving_key)
                    
            elif(y4x>20 and y4x<60 and y4y>60):
                print("greenright")
                y4y=y4y-distance
                print("y4y=",y4y,"y4x=",y4x)
                if(round(y4x,0)==sengreen1x and y4y<sengreen1y):
                    rem=abs(sengreen1y-y4y)-40
                    if(rem==0):
                        dice=0
                    print("enhanced senfreen1")
                    (y4x,y4y)=(senyellow2x,senyellow2y)
                    move_yellow(moving_key)
        
            elif(y4x>60 and y4y>20 and y4y<60):
                print("yellowup")
                if(round(y4x,0)==yellow2x and round(y4y,0)==yellow2y):
                    y4y=y4y-distance
                    if(round(y4x,0)==endyellowx and y4y<endyellowy):
                        rem=abs(endyellowy-y4y)
                        print("rem in boom",rem)
                        (y4x,y4y)=(endyellowx,endyellowy)
                        move_yellow(moving_key)
                else:
                    y4x=y4x+distance

                if(y4x>yellow2x and round(y4y,0)==yellow2y):
                    rem=abs(y4x-yellow2x)
                    print("rem in choom",rem)
                    (y4x,y4y)=(yellow2x,yellow2y)
                    move_yellow(moving_key)
    
            elif(y4x>60 and y4y>-20 and y4y<20):
                print("yellowmid")
                y4x=y4x-distance
                print("y4y=",y4y,"y4x=",y4x)
                if(y4x<60 and y4x>20):
                    print("y4 won")
                    time.sleep(1)
                    y4.clear()
                    y4.hideturtle()
                    os.system("play Audio/win.wav&")
                    messagebox.showinfo("Reached home","A Yellow token reached home")
                    re_roll=True
                    check_yellow_won()
                elif(y4x<20):
                    y4x=y4x+distance
                        
                        
            elif(y4x>60 and y4y<-20 and y4y>-60):
                print("yellowdown")
                y4x=y4x-distance
                if(y4x<senyellow1x and round(y4y,0)==senyellow1y):
                    rem=abs(y4x-senyellow1x)-40
                    if(rem==0):
                        dice=0                    
                    print("enhanced senyellow1")
                    (y4x,y4y)=(senblue2x,senblue2y)
                    move_yellow(moving_key)


            elif(y4x>20 and y4x<60 and y4y<-60):
                print("blueright")
                if(round(y4x,0)==blue2x and round(y4y,0)==blue2y):
                    y4x=y4x-distance
                    if(y4x<blue1x and round(y4y,0)==blue1y):
                        print("enhanced blue1")
                        rem=abs(y4x-blue1x)
                        (y4x,y4y)=(blue1x,blue1y)
                        move_yellow(moving_key)
                    
                else:
                    y4y=y4y-distance

                if(round(y4x,0)==blue2x and y4y<blue2y):
                    rem=abs(blue2y-y4y)
                    (y4x,y4y)=(blue2x,blue2y)
                    move_yellow(moving_key)

            elif(y4x>-20 and y4x<20 and y4y<-20):
                print("bluemid")                               
                y4x=y4x-distance
                if(y4x<blue1x and round(y4y,0)==blue1y):
                    print("enhanced blue1")
                    rem=abs(y4x-blue1x)
                    (y4x,y4y)=(blue1x,blue1y)
                    move_yellow(moving_key)

                
            elif(y4x<-20 and y4x>-60 and y4y<-20):
                print("blueleft")
                y4y=y4y+distance
                if(round(y4x,0)==senblue1x and y4y>senblue1y):
                    rem=abs(y4y-senblue1y)-40 
                    if(rem==0):
                        dice=0
                    print("enhanced senblue1")
                    (y4x,y4y)=(senred2x,senred2y)
                    move_yellow(moving_key)                        #end of checking sensitive points
            y4.clear()
            y4.goto(y4x,y4y)






re_roll=False
def play_yellow():
    global moving_key,can_clash
    moving_key=0
    global  y1x,y1y,y2x,y2y,y3x,y3y,y4x,y4y
    global all_yellow_start_pos,give_birth_yellow,dice
    global red1x,red2x,red1y,red2y,green1x,green2x,green1y,green2y,blue1x,blue2x,blue1y,blue2y,yellow1x,yellow2x,yellow1y,yellow2y
    global senred1x,senred1y,senred2x,senred2y,sengreen1x,sengreen1y,sengreen2x,sengreen2y
    global senblue1x,senblue1y,senblue2x,senblue2y,senyellow1x,senyellow1y,senyellow2x,senyellow2y
    global re_roll
    y1.goto(y1x,y1y)
    y2.goto(y2x,y2y)
    y3.goto(y3x,y3y)
    y4.goto(y4x,y4y)

    
    show_yellow_turn()

    #numinput("Rolling the dice","Press enter to roll the dice",1)
    dice=roll_dice()
    show_dice(dice)
    all_yellow_start_pos=check_yellow_start_pos()

    turn.write("       Yellow's   Turn ",False,align='left',font=("Times new roman",22,"bold"))

    #print(all_yellow_start_pos)
    if(dice!=6 and all_yellow_start_pos):
        time.sleep(3/9)
        d.clear()
    elif(dice==6):
        os.system("play Audio/positive.wav&")
        make_your_move()
        if(moving_key==1 and y1.isvisible() and (y1x,y1y)==(140+35,-280+105)):
            give_birth_yellow=True
        elif(moving_key==2 and y2.isvisible() and (y2x,y2y)==(140+105,-280+105)):
            give_birth_yellow=True
        elif(moving_key==3 and y3.isvisible() and (y3x,y3y)==(140+35,-280+35)):
            give_birth_yellow=True
        elif(moving_key==4 and y4.isvisible() and (y4x,y4y)==(140+105,-280+35) ):
            give_birth_yellow=True
        else:
            give_birth_yellow=False
        
        move_yellow(moving_key)
        re_roll=True
        d.clear()
    elif(not all_yellow_start_pos):
        make_your_move()
        give_birth_yellow=False
        move_yellow(moving_key)
        re_roll=False
        d.clear()
    can_clash=can_clash_yellow()
    if(can_clash):
        clash_yellow(moving_key)
    turn.undo()
    if(re_roll):
        d.clear()
        play_yellow()
    












st()

'''r1.ht()
r2.ht()
r4.ht()
r3.ht()

y1.ht()
y2.ht()
y3.ht()
y4.ht()

b1.ht()
b2.ht()
b3.ht()
b4.ht()

g1.ht()
g2.ht()
g3.ht()
g4.ht()
'''
#(r1x,r1y)=(endredx,endredy)
'''(r1x,r1y)=(endredx+40,endredy)
(r2x,r2y)=(endredx,endredy)
(r3x,r3y)=(endredx,endredy)
(r4x,r4y)=(endredx,endredy)

'''
'''    if(not yellow_won):    
        play_yellow()
    if(not blue_won):    
        play_blue()
(r1x,r1y)=(safegreen1x,safegreen1y)
(g1x,g1y)=(r1x,r1y)
r1.goto(r1x,r1y)
time.sleep(1)
g1.goto(g1x,g1y)
'''


print("maxplaxce",maxplace)
while (True):

    #check_green_won()
    #check_blue_won()
    #check_yellow_won()
    #check_red_won()


    if(not red_won):
        play_red()
    if(not green_won):
        play_green()
    if(not yellow_won):    
       play_yellow()
    if(not blue_won):    
       play_blue()
    if(place==maxplace):
        pickle.dump(redplace,open("Places/redplace.dat","wb"))
        pickle.dump(blueplace,open("Places/blueplace.dat","wb"))
        pickle.dump(yellowplace,open("Places/yellowplace.dat","wb"))
        pickle.dump(greenplace,open("Places/greenplace.dat","wb"))
        bye()
        os.system("python3 gameover.py")
        break
    time.sleep(3/2-1)

done()   
mainloop()

'''
    if(r1.isvisible()):
        r1.write("1",False,align="center",font=("Times new roman",18,"bold"))
    if(r2.isvisible()):
        r2.write("2",False,align="center",font=("Times new roman",18,"bold"))
    if(r3.isvisible()):
        r3.write("3",False,align="center",font=("Times new roman",18,"bold"))
    if(r4.isvisible()):
        r4.write("4",False,align="center",font=("Times new roman",18,"bold"))

    if(g1.isvisible()):
        g1.write("1",False,align="center",font=("Times new roman",18,"bold"))
    if(g2.isvisible()):
        g2.write("2",False,align="center",font=("Times new roman",18,"bold"))
    if(g3.isvisible()):
        g3.write("3",False,align="center",font=("Times new roman",18,"bold"))
    if(g4.isvisible()):
        g4.write("4",False,align="center",font=("Times new roman",18,"bold"))

    if(b1.isvisible()):
        b1.write("1",False,align="center",font=("Times new roman",18,"bold"))
    if(b2.isvisible()):
        b2.write("2",False,align="center",font=("Times new roman",18,"bold"))
    if(b3.isvisible()):
        b3.write("3",False,align="center",font=("Times new roman",18,"bold"))
    if(b4.isvisible()):
        b4.write("4",False,align="center",font=("Times new roman",18,"bold"))

    if(y1.isvisible()):
        y1.write("1",False,align="center",font=("Times new roman",18,"bold"))
    if(y2.isvisible()):
        y2.write("2",False,align="center",font=("Times new roman",18,"bold"))
    if(y3.isvisible()):
        y3.write("3",False,align="center",font=("Times new roman",18,"bold"))
    if(y4.isvisible()):
        y4.write("4",False,align="center",font=("Times new roman",18,"bold"))

'''
