import turtle
import time 
import random

delay = 0.1

#Score
score = 0
high_score = 0
score2 = 0 
high_score2 = 0

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
head.goto(-100, 0)
head.direction = "stop"

# head number 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color('#FDDFAA')
head2.penup()
head2.goto(100, 0)
head2.direction = "stop"

#apples
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('#C784FC')
food.penup()
food.goto(0,100)
food.direction = "stop"

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color('#C784FC')
food2.penup()
food2.goto(100,100)
food2.direction = "stop"

food3 = turtle.Turtle()
food3.speed(0)
food3.shape("circle")
food3.color('#C784FC')
food3.penup()
food3.goto(-100,100)
food3.direction = "stop"



segments = []
segments2 = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('#FDB08E')
pen.penup()
pen.hideturtle()
pen.goto(-140, 270)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "bold"))

#Pen
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color('#FDDFAA')
pen2.penup()
pen2.hideturtle()
pen2.goto(-140, 250)
pen2.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "bold"))

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

#Functions2
def go_up2():
    if head2.direction != "down":
        head2.direction = "up"

def go_down2():
    if head2.direction != "up":
        head2.direction = "down"

def go_left2():
    if head2.direction != "right":
        head2.direction = "left"

def go_right2():
    if head2.direction != "left":
        head2.direction = "right"


def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)

    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)

#keybinds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")

#Main game loop
while True:
    wn.update()

    #border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(-100, 0)
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
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))
    
    #snakes collision
    if head.distance(head2) < 20:
        time.sleep(0.5)
        head.goto(-100, 0)
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
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))

    if head2.distance(head) < 20:
        time.sleep(0.5)
        head2.goto(100, 0)
        head2.direction = "stop"

         #hide segments
        for segment in segments2:
            segment.goto(1000, 1000)

        #clear the segments
        segments2.clear()

        #reset delay
        delay = 0.1

        #score reset
        score2 = 0
        pen2.clear()
        pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

    for segment in segments2:
        if segment.distance(head) < 20:
           time.sleep(0.5)
           head.goto(-100, 0)
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
           pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))

    for segment in segments:
        if segment.distance(head2) < 20:
           time.sleep(0.5)
           head2.goto(100, 0)
           head2.direction = "stop"
  
          #hide segments
           for segment in segments2:
               segment.goto(-1000, -1000)

           #clear the segments
           segments.clear()

           #reset delay
           delay = 0.1

           #score reset
           score2 = 0
           pen2.clear()
           pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

    #border collision2
    if head2.xcor() > 290 or head2.xcor() < -290 or head2.ycor() > 290 or head2.ycor() < -290:
        time.sleep(0.5)
        head2.goto(100, 0)
        head2.direction = "stop"

         #hide segments2
        for segment in segments2:
            segment.goto(-1000, -1000)

        #clear the segments2
        segments2.clear()
        delay = 0.1

        #score reset2
        score2 = 0
        pen2.clear()
        pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

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
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))

    if head.distance(food2) < 20:
        #location randomizer 
        x = random.randrange (-280, 280, 20)
        y = random.randrange (-280, 240, 20)
        food2.goto (x, y)

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
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))
        
    if head.distance(food3) < 20:
        #location randomizer 
        x = random.randrange (-280, 280, 20)
        y = random.randrange (-280, 240, 20)
        food3.goto (x, y)

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
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))
        
    #collision2
    if head2.distance(food) < 20:
        #location randomizer 
        x = random.randrange (-280, 280, 20)
        y = random.randrange (-280, 240, 20)
        food.goto (x, y)

        #add a body2
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color('#FDB08E')
        new_segment2.penup()
        segments2.append(new_segment2)

        #shorten the delay
        delay -= 0.001

        #score
        score2 += 1

        if score2 > high_score2:
            high_score2 = score2
        pen2.clear()
        pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

    if head2.distance(food2) < 20:
        #location randomizer 
        x = random.randrange (-280, 280, 20)
        y = random.randrange (-280, 240, 20)
        food2.goto (x, y)

        #add a body2
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color('#FDB08E')
        new_segment2.penup()
        segments2.append(new_segment2)

        #shorten the delay
        delay -= 0.001

        #score
        score2 += 1

        if score2 > high_score2:
            high_score2 = score2
        pen2.clear()
        pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

    if head2.distance(food3) < 20:
        #location randomizer 
        x = random.randrange (-280, 280, 20)
        y = random.randrange (-280, 240, 20)
        food3.goto (x, y)

        #add a body2
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("square")
        new_segment2.color('#FDB08E')
        new_segment2.penup()
        segments2.append(new_segment2)

        #shorten the delay
        delay -= 0.001

        #score
        score2 += 1

        if score2 > high_score2:
            high_score2 = score2
        pen2.clear()
        pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))

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

    #move the segments in reverse order
    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x, y)

    #move segment 0
    if len(segments2) > 0:
         x = head2.xcor()
         y = head2.ycor()
         segments2[0].goto(x,y)
    

    move()
    move2()

    for segment in segments:
        if segment.distance(head) < 20:
           time.sleep(0.5)
           head.goto(-100, 0)
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
           pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))

    for segment in segments2:
        if segment.distance(head2) < 20:
           time.sleep(0.5)
           head2.goto(100, 0)
           head2.direction = "stop"
  
          #hide segments
           for segment in segments2:
               segment.goto(-1000, -1000)

           #clear the segments
           segments2.clear()

           #reset delay
           delay = 0.1

           #score reset
           score2 = 0
           pen2.clear()
           pen2.write("Score: {}  High Score: {}".format(score2, high_score2), align="center", font=("Courier", 16, "bold"))
            

    time.sleep(delay)

wn.mainloop()
