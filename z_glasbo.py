from turtle import *
import random
from pygame import mixer

speed(0)
r = 3
screen = Screen()
screen.delay(0)

mixer.init()
mixer.music.load("GasGasGas.mp3")
mixer.music.play()
mixer.music.set_pos(50)


pu()
goto(-200,450)
write("prikaz izotopov bakra:", True,"left", ("Arial", 30, "normal")) 
goto(-400,400)
for i in range(round(400/r)):
    for k in range(round(400/r)):
        if random.randint(1,1000)<692:
            fillcolor("gold")
        else:
            fillcolor("silver")
        begin_fill()
        pd()
        circle(r)
        pu() 
        fd(2*r) 
        end_fill()
    goto(-400, 400-(i+1)*2*r)  

done()

