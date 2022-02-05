import turtle
import time
import random

class SnakeApp:

    def __init__(self) -> None:
        self.delay = 0.1
        self.score=0
        self.high_score=0

        self.init_screen()

        self.init_head()        
       
        self.init_food()

        self.segments = []

        self.init_pen()
        
        self.timer=1

    def init_screen(self):
        self.wn = turtle.Screen()
        self.wn.title("Snake Game")
        self.wn.bgcolor("blue")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)

        self.wn.listen()
        self.wn.onkeypress(self.goup, "w")
        self.wn.onkeypress(self.godown, "s")
        self.wn.onkeypress(self.goleft, "a")
        self.wn.onkeypress(self.goright, "d")

    def init_head(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

    def init_food(self):
        self.food = turtle.Turtle()
        self.colors = random.choice(["red","lime","magenta"])
        self.shapes = random.choice(["square","triangle","circle"])
        self.food.speed(0)
        self.food.shape(self.shapes)
        self.food.color(self.colors)
        self.food.penup()
        self.food.goto(0,100)

    def init_pen(self):
        self.pen=turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,250)
        self.pen.write("Score: {} High score: {}".format(self.score,self.high_score),align="center",font=("candara",24,"bold"))

    def game_over(self):
        self.pen.goto(0,0)
        self.pen.write("Game Over", align="center",font=("candara",40,"bold"))
        time.sleep(2)
        self.pen.goto(0,250)      
        self.head.goto(0,0)
        self.head.direction = "stop"

        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.score = 0
        self.delay = 0.1
        self.pen.clear()
        self.pen.write("Score: {} High score: {}".format(self.score,self.high_score),align="center",font=("candara",24,"bold"))

    def godown(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    def goup(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    def goright(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    def goleft(self):
        if self.head.direction != "right":
            self.head.direction = "left"
    def automove(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y+20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y-20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x+20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x-20)
        
    def run(self):
        while True:

            self.wn.update()
            time.sleep(self.delay)
            
            if self.head.xcor()>290 or self.head.xcor()<-290 or self.head.ycor()>290 or self.head.ycor()<-290:
                self.game_over()
            
            if self.head.distance(self.food) <20:
                x = random.randint(-270,270)
                y = random.randint(-270,270)
                self.colors = random.choice(["red","lime","magenta"])
                self.shapes = random.choice(["square","triangle","circle"])
                self.food.shape(self.shapes)
                self.food.color(self.colors)
                self.food.goto(x,y)
                
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("orange")
                new_segment.penup()
                self.segments.append(new_segment)
                
                self.delay -= 0.001
                self.score += 10
            
            
                if self.score > self.high_score:
                    self.high_score = self.score
                self.pen.clear()
                self.pen.write("Score: {} High score: {}".format(self.score,self.high_score),align="center",font=("candara",24,"bold"))

            for index in range(len(self.segments)-1,0,-1):
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                self.segments[index].goto(x,y)
            
            if len(self.segments)>0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x,y)
                
            self.automove()
            
            for segment in self.segments:
                if segment.distance(self.head)<20:
                    self.game_over()
                    
        self.wn.mainloop()
        turtle.done()

if __name__ == "__main__":
        
    app = SnakeApp()

    app.run()
