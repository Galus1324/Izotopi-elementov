from turtle import *
import random
from pygame import mixer

speed(0)
r = 20
screen = Screen()
screen.delay(0)

mixer.init()
mixer.music.load("GasGasGas.mp3")
mixer.music.play()
mixer.music.set_pos(50)

list_of_percentages = [492, 277, 40, 185, 6]

colors = ["yellow", "pink", "red", "purple", "green", "gold", "silver", "blue"]

def alg(isotopes):
    random_num = random.randint(1,1000)
    for i in range(len(isotopes)):
        if sum(isotopes[:i+1]) >= random_num:
            return (colors[i])
        
pu()
goto(-200,450)
write("prikaz izotopov bakra:", True,"left", ("Arial", 30, "normal")) 
goto(-400,400)
for i in range(round(400/r)):
    for k in range(round(400/r)):
        fillcolor(alg(list_of_percentages))
        begin_fill()
        pd()
        circle(r)
        pu() 
        fd(2*r) 
        end_fill()
    goto(-400, 400-(i+1)*2*r) 



done()

