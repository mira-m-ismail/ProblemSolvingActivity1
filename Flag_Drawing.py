import turtle as t

def draw_side(width, height):
    t.forward(width)
    t.right(90)
    t.forward(height)

def draw_rectangle(x,y,width,height,color):
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.begin_fill()
    draw_side(width,height)
    draw_side(width,height)
    t.penup()
    t.end_fill()
    t.goto(x/2,y/2)
    print(t.xcor())    # prints coords on terminal
    print(t.ycor())    # prints coords on terminal

def draw_circle(x,y,radius,color):
    t.goto(x,y-radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_flagpole(x,y,height,color):
    t.penup()
    t.goto(x,y)
    t.pencolor(color)
    t.forward(height)

'''def draw_flag(x,y,scale_factor):
    draw_flagpole(x,y,height,color)
    draw_rectangle(x,y,width,height,color)
    draw_circle(x,y,radius,color)

def main():
    t.bgcolor("lightblue")
    draw_flag(-50,50,1)
    draw_flag(50,50,0.5)'''

    



