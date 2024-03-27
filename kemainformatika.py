from turtle import *
import random

speed(-1)
r = 20

pu()
goto(-200,450)
write("prikaz izotopov bakra:", True,"left", ("Arial", 30, "normal")) 
goto(-400,400)
for i in range(20):
    for k in range(20):
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





