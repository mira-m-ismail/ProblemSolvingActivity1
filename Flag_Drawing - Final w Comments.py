'''This program uses turtle graphics to draw a colored flag step-by-step, returning the x- and y- coordinates
of the center of the flag in the process. Then, a second identical flag is drawn to the chosen scale factor.'''

import turtle as t

def draw_side(width, height):
    t.forward(width)    # draws one side, considered width
    t.right(90)
    t.forward(height)   # draws one side, considered height
    t.right(90)

def draw_rectangle(x,y,width,height,color): # (step 2) this function draws a rectangle, the flag part
    t.penup()
    t.goto(x,y)
    t.fillcolor(color)   # argument passed to "color" parameter from inside the draw_flag() function
    t.pensize(1)
    t.begin_fill()
    t.setheading(360)
    t.pendown()
    draw_side(width,height)  # draws two sides
    draw_side(width,height)  # draws two more sides, closing the rectangle
    t.end_fill()
    t.penup()
    t.forward(width/2)
    t.right(90)
    t.forward(height/2)     # turtle moves to the center of the rectangle
    center_x=(t.xcor())     # this stores x-coordinate of the center in center_x
    center_y=(t.ycor())     # this stores y-coordinate of the center in center_y
    print(center_x)         # this prints x-coordinate of the center onto the terminal
    print(center_y)         # this prints y-coordinate of the center onto the terminal
    t.right(-90)            # resets where the turtle is facing

def draw_circle(x,y,radius,color):  # (step 3) this function draws a circle in the center of the flag
    t.penup()
    t.goto(x,y-radius)  # turtle moves to center of the flag, minus radius, in order to center the circle
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)    # creates the circle
    t.end_fill()

def draw_flagpole(x,y,height,color):    # (step 1) this function draws the flagpole
    t.penup()
    t.setheading(90)
    t.goto(x,y)     # turtle goes to chosen starting point
    t.pencolor(color)
    t.pensize(4)
    t.pendown()
    t.forward(height)
    t.penup()

def draw_flag(x,y,scale_factor):    # this function combines all the steps to draw a flag in chosen scale factor
    width=scale_factor*150
    height=scale_factor*100
    color="black"
    x=x*scale_factor    # this ensures x-values are to-scale
    y=y*scale_factor    # this ensures y-values are to-scale
    draw_flagpole(x,-y,height*2,color)  # flagpole is twice the height of flag, drawn bottom-to-top, making flag reach half the pole's height
    draw_rectangle(x+5,y,width,height,"red")    # draws red rectangle slightly to the right of the pole (5 units away)
    radius=scale_factor*25
    draw_circle(x+(width/2)+5,y-(height/2),radius,"white")  # circle is centered using given x & y coordinates and width & height values

def main():
    t.bgcolor("lightblue")  # background color
    draw_flag(-100,100,1)   # calls the draw_flag() function & draws a flag in full scale
    draw_flag(200,100,0.75) # draws a flag in 3/4 of the scale, next to the first flag
    t.done()

main()