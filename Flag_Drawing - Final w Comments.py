'''This program uses turtle graphics to draw a colored flag step-by-step, returning the x- and y- coordinates
of the center of the flag in the process. Then, a second identical flag is drawn to the chosen scale factor.'''

import turtle as t

def draw_side(width, height):
    t.forward(width)    # draws one side (width)
    t.right(90)
    t.forward(height)   # draws one side (height)
    t.right(90)

def draw_rectangle(x,y,width,height,color): # (step 2) this function draws a rectangle, the flag part
    t.penup()
    t.goto(x,y)     # moves turtle to (x,y), top left corner
    t.fillcolor(color)   # argument passed to "color" parameter from inside draw_flag()
    t.pensize(1)
    t.setheading(360)
    t.begin_fill()
    t.pendown()
    draw_side(width,height)  # draws two sides
    draw_side(width,height)  # draws two more sides, closing the rectangle
    t.end_fill()
    t.penup()
    t.forward(width/2)
    t.right(90)
    t.forward(height/2)     # turtle moves to the center of the rectangle
    center_x=(t.xcor())     # this stores x-coordinate of the turtle at center in center_x
    center_y=(t.ycor())     # this stores y-coordinate of the turtle at center in center_y
    print(center_x,",",center_y)    # returns & prints coordinates of the center onto the terminal
    t.right(-90)            # resets where the turtle is facing

def draw_circle(x,y,radius,color):  # (step 3) this function draws a circle in the center of the flag
    t.penup()
    t.goto(x,y-radius)  # turtle moves to center of the flag, minus radius, in order to center the circle
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)    # draws the filled circle
    t.end_fill()

def draw_flagpole(x,y,height,color):    # (step 1) this function draws the flagpole
    t.penup()
    t.setheading(90)
    t.goto(x,y)     # turtle goes to chosen point (x,y)
    t.pencolor(color)
    t.pensize(4)
    t.pendown()
    t.forward(height)   # draws vertically upwards toward the top-left of the flag
    t.penup()

def draw_flag(x,y,scale_factor):    # this function combines all the steps to draw a flag with an emblem in chosen scale factor
    width=scale_factor*150
    height=scale_factor*100
    color="black"
    x=x*scale_factor    # this ensures x-values are to-scale
    y=y*scale_factor    # this ensures y-values are to-scale
    draw_flagpole(x,-y,height*2,color)  # flagpole is twice the height of flag, making flag reach half the pole's height
    draw_rectangle(x+5,y,width,height,"red")    # draws red rectangle slightly to the right of the pole (5 units away)
    radius=scale_factor*25
    draw_circle(x+(width/2)+5,y-(height/2),radius,"white")  # circle is centered using given x & y coordinates and width & height values

def main(): # this is a reusable function, allowing change of x-values and scale factors to result in different-sized flags
    t.bgcolor("lightblue")  # background color
    draw_flag(-200,100,1)   # calls draw_flag() & draws flag in full scale
    draw_flag(50,100,0.75) # draws a flag in 3/4 of the scale, near the first flag
    t.done()

main()