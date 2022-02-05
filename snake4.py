import turtle
import time
import random

def godown():
    if head.direction != "up":
        head.direction = "down"
def goup():
    if head.direction != "down":
        head.direction = "up"
def goright():
    if head.direction != "left":
        head.direction = "right"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def automove():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    

delay = 0.1
score=0
high_score=0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
colors = random.choice(["red","lime","magenta"])
shapes = random.choice(["square","triangle","circle"])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

segments = []

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("candara",24,"bold"))

        
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

timer=1


while True:

    wn.update()
    time.sleep(delay)
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        pen.goto(0,0)
        pen.write("Game Over", align="center",font=("candara",40,"bold"))
        time.sleep(2)
        pen.goto(0,250)      
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("candara",24,"bold"))
    
    if head.distance(food) <20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        colors = random.choice(["red","lime","magenta"])
        shapes = random.choice(["square","triangle","circle"])
        food.shape(shapes)
        food.color(colors)
        food.goto(x,y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.001
        score += 10
      
    
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("candara",24,"bold"))

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    automove()
    
    for segment in segments:
        if segment.distance(head)<20:
            pen.goto(0,0)
            pen.write("Game Over", align="center",font=("candara",40,"bold"))            
            time.sleep(2)
            pen.goto(0,250)
            head.goto(0,0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
        

            
            pen.clear()
            pen.write("Score: {} High score: {}".format(score,high_score),align="center",font=("candara",24,"bold"))


        
wn.mainloop()
turtle.done()