from turtle import *
import random
from pygame import mixer

r = 5
ime_elementa = "x"
list_of_percentages = [ 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250,]

speed(0)
screen = Screen()
screen.delay(0)
wn = Screen()
addshape("car-removebg-preview.png")



mixer.init()
mixer.music.load("GasGasGas.mp3")
mixer.music.set_volume(0)
mixer.music.play()
mixer.music.set_pos(50)



colors = ["yellow", "pink", "red", "purple", "green", "light blue", "silver", "blue"]

def alg(isotopes):
    random_num = random.randint(1,10000)
    for i in range(len(isotopes)):
        if sum(isotopes[:i+1]) >= random_num:
            return colors[i]
        
pu()
goto(-225,450)
write(f"prikaz izotopov elementa {ime_elementa}:", True,"left", ("Arial", 30, "normal")) 
goto(-800,350)
for i in range(round(400/r)):
    for k in range(round(800/r)):
        fillcolor(alg(list_of_percentages))
        begin_fill()
        pd()
        circle(r)
        pu() 
        fd(2*r) 
        end_fill()
    goto(-800, 350-(i+1)*2*r) 



done()

