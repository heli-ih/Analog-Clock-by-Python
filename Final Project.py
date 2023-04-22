from turtle import Screen, Turtle
from time import *

#Tarif screen baraye turtle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)

#Emtiyazi(Function taghyire ax)
screen.bgpic("07.gif")
counter=0
def change_bg():
    global counter
    bg_list=["01.gif","02.gif","03.gif","04.gif","05.gif","06.gif","07.gif"]
    screen.bgpic(bg_list[counter])
    counter+=1
    if counter>=len(bg_list):
        counter=0

#Tarif turtle va function rasme safheye saat
clock_pen = Turtle()
def clockFace():
    # Rasme dayere
    clock_pen.pen(shown=False, pencolor="#FFF2CC", pensize=5)
    clock_pen.penup()
    clock_pen.setheading(0)
    clock_pen.setposition(0, 250)
    clock_pen.pendown()
    clock_pen.circle(-250)
    clock_pen.penup()
    clock_pen.setheading(60)

    # Rasme adad ha
    roman_numbers = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
    for i in range(12):
        clock_pen.setposition(0,-19)
        clock_pen.fd(185)
        clock_pen.write(roman_numbers[i], align='center', font=('Bahnschrift Condensed', 25, 'bold'))
        clock_pen.rt(30)
    clock_pen.setheading(90)

    # Rasme khotoote saat
    for j in range(0, 60):
        clock_pen.setposition(0,0)
        if j % 5 == 0:
            length = 210
        else:
            length = 225
        clock_pen.fd(length)
        clock_pen.pendown()
        clock_pen.fd(235 - length)
        clock_pen.penup()
        clock_pen.rt(6)

#Tarif turtle baraye shekle aghrabeha va function baraye tanzime jahat
hour_hand=Turtle()
hour_hand.shape("arrow")
hour_hand.color("#FFF2CC")
hour_hand.shapesize(0.5,13)

minute_hand=Turtle()
minute_hand.shape("arrow")
minute_hand.color("#FFF2CC")
minute_hand.shapesize(0.5,19)

second_hand=Turtle()
second_hand.shape("arrow")
second_hand.color("red")
second_hand.shapesize(0.4,23)

def clockHands(h,m,s):
    hour_hand.setheading(90)
    hour_hand.rt(h*30 + m*0.5)

    minute_hand.setheading(90)
    minute_hand.rt(m*6 + s*0.1)

    second_hand.setheading(90)
    second_hand.rt(s*6)

#Dayere vasate saat
inside_dot=Turtle()
inside_dot.shape('circle')
inside_dot.pen(pencolor="#FFF2CC",fillcolor="#FFF2CC",pensize=20)

# Function baraye negah dashtane saat
stopVal = False
def stop():
    global stopVal
    if stopVal == False:
        stopVal = True
    else:
        stopVal = False

# Fuction haye tagheire saat
added_h, added_m, added_s = 0, 0, 0
def hour_changer():
    global added_h
    if stopVal == True:
        added_h = 1

def minute_changer():
    global added_m
    if stopVal == True:
        added_m = 1

def second_changer():
    global added_s
    if stopVal == True:
        added_s = 1

#Tarif turtle va function baraye rasm saat digital
digital_drawer=Turtle()
digital_drawer.ht()
digital_drawer.pencolor("#FFF2CC")
digital_drawer.setheading(90)
digital_drawer.pu()
digital_drawer.fd(270)

def digital(h,m,s):
    digital_drawer.write(str(h).zfill(2) + ":" + str(m).zfill(2) +
     ":" + str(s).zfill(2),align='center',font=('DS-Digital', 40, 'normal'))

#Function asliye harekate saat
def main_func():
    current_time = strftime("%H:%M:%S").split(":")
    h = int(current_time[0])
    m = int(current_time[1])
    s = int(current_time[2])
    clockHands(h,m,s)
    screen.update()

    global added_h, added_m, added_s
    while True:

        if stopVal == False:
            s += 1
            sleep(1)

        if s == 60:
            m += 1
            s = 0
        
        if m == 60:
            h += 1
            m = 0
        
        if h == 24:
            h = 0
        s = s + added_s
        m = m + added_m
        h = h + added_h
        added_s, added_m, added_h = 0, 0, 0

        clockHands(h,m,s)
        digital(h,m,s)
        screen.update()
        digital_drawer.clear()

clockFace()

#Emtiyazi(Freeze kardane va tanzime saat, Taghyire ax)
screen.onkeypress(stop, "t")
screen.onkeypress(change_bg, "f")
screen.onkeypress(hour_changer, "h")
screen.onkeypress(minute_changer, "m")
screen.onkeypress(second_changer, "s")
screen.listen()

main_func()

screen.mainloop()