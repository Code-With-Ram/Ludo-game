from turtle import *
import os
import time
import pickle
setup(width=1500,height=1500,startx=0,starty=0)
bgcolor('pink')
up()
goto(-150,0)
write("LOADING ",True,align='left',font=("Domestic Manners",42,"bold"))
write(". ",True,align='left',font=("Domestic Manners",42,"bold"))
time.sleep(1/3)
for i in range(6):
    goto(150,0)
    write(" . ",True,align='left',font=("Domestic Manners",42,"bold"))
    time.sleep(1/3)
    write(". ",True,align='left',font=("Domestic Manners",42,"bold"))
    time.sleep(1/3)
    undo()
    undo()
    undo()



mainloop()
done()
