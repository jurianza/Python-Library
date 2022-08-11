# Simple Snake Game
# By Joshua Urianza

# Library Imports
import os
import turtle
import time #Help control time within Python
import random

# Set up Screen

delay = 0.1

#Score
score = 0
high_score = 0

wn =turtle.Screen()
wn.title("Snake Game by Joshua Urianza")
wn.bgcolor("Blue")
wn.setup(width =600, height=600)
wn.tracer(0) #Turns off the screen updates


#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0,100)


#Snake Body

segments = [ ]


#Pen
pen=turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))




#Head direction
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction="down"

def go_left():
    if head.direction!="right":
        head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"

#Snake move ability
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)  
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)  
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20) 
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
        

        
#Keyboard bindings/Controls
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")




# Main game loop - How the game functions outside of make food and body. 
while True:
    wn.update( ) # Updates everything at the end
    
    #Check for a collision with the border/ Kill snake head at border
    if head.xcor( )> 290 or head.xcor( ) <-290 or head.ycor( ) > 290 or head.ycor( ) < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
    
    #Reset the the score
        score = 0
    
    # Reset the delay
        delay = 0.1
    
        pen.clear()
        pen.write("Score: {}  High Scorre: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))    
    
    #Check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        #Add a segment
        new_segment = turtle.Turtle( )
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup ( )
        segments.append(new_segment)
        
        
        #Shorten the delay
        delay -= 0.001
        
        
        #Increase the score
        score +=10
        
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Scorre: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    #Move the end segment first in reverse order
    for index in range(len(segments)-1, 0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
        #Move segment 0 to where the where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
            
            
    move()
    
    #Check for head Collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Kill Snake body on collison/ Segments
            for segment in segments:
                segment.goto(1000, 1000)
                
            # Clear the segments list
            segments.clear()            
            
            score = 0
            
            pen.clear()
            pen.write("Score: {}  High Scorre: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))               

    
    time.sleep(delay) #Stop program from the top 1/10 of a second

wn.mainloop()

