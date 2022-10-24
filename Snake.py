import turtle
import time 
import random

delay = 0.1

#Score
score = 0
high_score = 0



#Screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor('#82C7B1')
wn.setup(width=600, height=600)
wn.tracer(0)


# head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('#FDB08E')
head.penup()
head.goto(0,0)
head.direction = "stop"
head.destination = (0,)

#apple
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('#C784FC')
food.penup()
food.goto(0,100)
food.direction = "stop"

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('#C784FC')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 26, "bold"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

paused = False

def pause_on():
    global paused
    if paused == True:
        paused = False
    else:
        paused = True

#keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(pause_on, "Escape")

#Pause


#Main game loop
while True:
    if not paused:
        wn.update()

    #border collision
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

         #hide segments
            for segment in segments:
                segment.goto(1000, 1000)

        #clear the segments
            segments.clear()

        #reset delay
            delay = 0.1

        #score reset
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 26, "normal"))


    #collision
        if head.distance(food) < 20:
           #location randomizer 
            x = random.randrange (-280, 280, 20)
            y = random.randrange (-280, 240, 20)
            food.goto (x, y)

        #add a body
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color('#FDDFAA')
            new_segment.penup()
            segments.append(new_segment)

        #shorten the delay
            delay -= 0.001

        #score
            score += 1

            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 26, "normal"))

    #move the segments in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

    #move segment 0
        if len(segments) > 0:
             x = head.xcor()
             y = head.ycor()
             segments[0].goto(x,y)
    

        move()

        for segment in segments:
            if segment.distance(head) < 20:
               time.sleep(0.5)
               head.goto(0, 0)
               head.direction = "stop"
  
          #hide segments
               for segment in segments:
                   segment.goto(1000, 1000)

                #clear the segments
               segments.clear()

                #reset delay
               delay = 0.1
 
           #score reset
               score = 0
               pen.clear()
               pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 26, "normal"))
            

        time.sleep(delay)
    
    else:
        wn.update()

wn.mainloop()
