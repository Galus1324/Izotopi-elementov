import turtle
import random
from pygame import mixer

r = 5
ime_elementa = "x"
list_of_percentages = [ 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250,]

auto = turtle.Turtle()
auto.speed(0)
screen = turtle.Screen()
screen.addshape("screenshot_3.png")
screen.delay(0)
auto.shape("screenshot_3.png")


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
        
auto.pu()
auto.goto(-225,450)
auto.write(f"prikaz izotopov elementa {ime_elementa}:", True,"left", ("Arial", 30, "normal")) 
auto.goto(-800,350)
for i in range(round(400/r)):
    for k in range(round(800/r)):
        auto.fillcolor(alg(list_of_percentages))
        auto.begin_fill()
        auto.pd()
        auto.circle(r)
        auto.pu() 
        auto.fd(2*r) 
        auto.end_fill()
    auto.goto(-800, 350-(i+1)*2*r) 



auto.done()

