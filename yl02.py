#toomas
#10.10.22
#yl2
import turtle

#akna seaded
window = turtle.Screen()
window.setup(400,400)

#kujundi loomine
t = turtle.Turtle()
for x in range(5):
    t.fd(150)
    t.rt(144)
    

for x in range(3):
    t.color("red")
    t.backward(100)
    t.rt(120)
    
turtle.exitonclick()