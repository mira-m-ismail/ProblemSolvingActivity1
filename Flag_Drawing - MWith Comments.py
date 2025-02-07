import turtle as t

def draw_side(width, height):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

def draw_rectangle(x,y,width,height,color):
    t.pensize(1)
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)
    t.pencolor("black")
    t.pensize(1)
    t.begin_fill()
    t.setheading(360)
    t.pendown()
    draw_side(width,height)
    draw_side(width,height)
    t.end_fill()
    t.penup()
    t.goto(x/2,y/2)
    print(t.xcor())    # prints coords on terminal
    print(t.ycor())    # prints coords on terminal

def draw_circle(x,y,radius,color):
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_flagpole(x,y,height,color):
    t.penup()
    t.setheading(90)
    t.goto(x,y)
    t.pencolor(color)
    t.pensize(4)
    t.pendown()
    t.forward(height)
    t.penup()

def draw_flag(x,y,scale_factor):
    width=scale_factor*150
    height=scale_factor*100      # passed values for width & height
    color="black"
    x=x*scale_factor
    y=y*scale_factor
    draw_flagpole(x,-y,height*2,color) # flagpole height is 2 times flag height
    draw_rectangle(x+5,y,width,height,"red")
    radius=scale_factor*25
    draw_circle(x+(width/2)+5,y-(height/2),radius,"white")   # gave x & y parameters that center the circle

def main():
    t.speed(1)
    t.bgcolor("lightblue")
    draw_flag(-100,100,1)   # 1st flag
    draw_flag(200,100,0.75) # 2nd flag, x-cor and scale factor changed
    t.done()

main()

    



