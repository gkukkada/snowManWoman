from turtle import *
import math

class shape():

    def __init__(self,pencolor,pensize):
        self.pencolor = pencolor
        self.pensize = pensize

class Circle(shape):

    def __init__(self,x,y,r,pencolor,pensize):
        self.x = x
        self.y = y
        self.r = r
        shape.__init__(self, pencolor, pensize)
    def __str__(self, params):
        return ""

    def draw(self,turtle):
        turtle.penup()
        turtle.goto (self.x, self.y)
        turtle.pendown()
        turtle.pencolor (self.pencolor)
        turtle.pensize(self.pensize)
        turtle.circle (self.r)
        turtle.penup()

class Triangle(shape):
    
    def __init__(self,x, y, side_len,pencolor,pensize):
        self.x = x
        self.y = y
        self.side_len = side_len
        shape.__init__(self, pencolor, pensize)
    
    def __str__(self, params):
        return ""
    
    def draw(self,turtle): 
        angle = 360 / 3
        turtle.penup()
        turtle.goto (self.x, self.y)
        turtle.begin_fill()
        turtle.color ('pink')
        turtle.pendown()
        turtle.pencolor (self.pencolor)
        turtle.pensize(self.pensize)
        turtle.forward(self.side_len) 
        turtle.left(120)
        turtle.forward(self.side_len)
        turtle.left(120)
        turtle.forward(self.side_len)
        turtle.end_fill()

class Rectangle(shape):

    def __init__(self,x, y, length,width,pencolor,pensize):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        shape.__init__(self, pencolor, pensize)

    def __str__(self, params):
        return ""

    def draw(self,turtle):
        turtle.penup()
        turtle.goto (self.x, self.y)
        turtle.begin_fill()
        turtle.color("brown")
        turtle.pendown()
        turtle.pencolor (self.pencolor)
        turtle.pensize(self.pensize)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.length)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.length)
        turtle.left(90)
        turtle.end_fill()

class Line(shape):

    def __init__(self, x, y, length,angle,pencolor,pensize):
 
        self.x = x
        self.y = y
        self.length = length
        self.pencolor = pencolor
        self.pensize = pensize
        self.angle = angle
        shape.__init__(self, pencolor, pensize)
    
    def __str__(self, params):
        return ""
    
    def draw(self,turtle):       
        turtle.penup()
        turtle.goto (self.x, self.y)
        turtle.pendown()
        turtle.pencolor (self.pencolor)
        turtle.pensize(self.pensize)
        turtle.goto (self.x+(math.cos(self.angle)*self.length), self.y+(math.sin(self.angle)*self.length))
        turtle.penup()

class Snow_person():

    def circles(self, turtle,x,y,bodysize,pencolor,eye):
        color = pencolor
        size = 3
        eyecolor = eye
        c1 = Circle(x,y,bodysize,color,size)
        c1.draw(turtle)
        c2 = Circle(x,y+(2*bodysize),bodysize*0.75,color,size)
        c2.draw(turtle)        
        c3 = Circle(x,y+(3.5*bodysize),bodysize*0.5,color,size)
        c3.draw(turtle)
        c4 = Circle(x,y+(0.5*bodysize),5,color,size)
        c4.draw(turtle)
        c5 = Circle(x,y+(1.25*bodysize),5,color,size)
        c5.draw(turtle)
        c6 = Circle(x,y+(2.3*bodysize),5,color,size)
        c6.draw(turtle)
        c7 = Circle(x,y+(3*bodysize),5,color,size)
        c7.draw(turtle)
        
        c8 = Circle(x-(0.25*bodysize),y+(4*bodysize),3,eyecolor,size)
        c8.draw(turtle)
        c9 = Circle(x+(0.25*bodysize),y+(4*bodysize),3,eyecolor,size)
        c9.draw(turtle)
        l = Line(x-(0.2*bodysize),y+(3.8*bodysize),0.4*bodysize,0,pencolor,3)
        l.draw(turtle)
        
class Snow_man(Snow_person):
    
    def __str__(self, params):
        return ""
    
    def draw(self,turtle):
        x = -100
        y = -100
        color = "black"
        eye = "blue"
        bodysize = 60
        Snow_person.circles(self,turtle, x, y,bodysize,color,eye)
        s = Rectangle(x-(0.4*bodysize),y+(4.4*bodysize),bodysize,0.75*bodysize,"brown",3)
        s.draw(turtle)
        l1 = Line(x-(0.6*bodysize),y+(4.4*bodysize),1.25*bodysize,0,"brown",3)    
        l1.draw(turtle)
        l2 = Line(x-(0.7*bodysize),y+(3*bodysize),-1.25*bodysize,290,color,3)    
        l2.draw(turtle)
        l2 = Line(x+(0.7*bodysize),y+(3*bodysize),1.25*bodysize,-290,color,3)    
        l2.draw(turtle)
        turtle.goto (x-(1.0*bodysize), y-(1.0*bodysize))
        turtle.write("Snow man", move=False, align="left", font=("Arial", 20, "normal"))
        
class Snow_woman(Snow_person):
    
    def __str__(self, params):
        return ""
    
    def draw(self,turtle):
        x = 150
        y = -100
        color = "orange"  
        eye = "green"  
        bodysize = 50               
        Snow_person.circles(self, turtle, x, y,bodysize,color,eye) 
        t = Triangle(x-(0.6*bodysize),y+(4.4*bodysize),1.25*bodysize,"pink",3)    
        t.draw(turtle)
        turtle.begin_fill()
        turtle.color ('red')
        c9 = Circle(x-(0.05*bodysize),y+(3.85*bodysize),3,"red",4)    
        c9.draw(turtle)
        turtle.end_fill()
        l = Line(x-(0.7*bodysize),y+(3*bodysize),-1.25*bodysize,290,color,3)    
        l.draw(turtle)
        l = Line(x+(0.7*bodysize),y+(3*bodysize),1.25*bodysize,270,color,3)    
        l.draw(turtle)
        l = Line(x+(0.7*bodysize)+(math.cos(270)*1.25*bodysize),y+(3*bodysize)+(math.sin(270)*1.25*bodysize),1.50*bodysize,60,color,3)    
        l.draw(turtle)
        l = Line(x-(0.4*bodysize),y+(4.35*bodysize),bodysize,230,"brown",3)    
        l.draw(turtle)
        l = Line(x-(0.4*bodysize),y+(4.35*bodysize),0.5*bodysize,350,"brown",3)    
        l.draw(turtle)
        l = Line(x+(0.4*bodysize),y+(4.35*bodysize),-bodysize,-230,"brown",3)    
        l.draw(turtle)
        l = Line(x+(0.4*bodysize),y+(4.35*bodysize),-0.5*bodysize,-350,"brown",3)    
        l.draw(turtle)
        turtle.goto (x-(1.0*bodysize), y-(1.0*bodysize))
        turtle.write("Snow woman", move=False, align="left", font=("Arial", 20, "normal"))
       
if __name__ == '__main__':

    turtle = Turtle()

    # Control the speed here
    set_speed = 10
    turtle.speed(set_speed)
    #turtle.fillcolor ('white')
    s1 = Snow_man()
    s1.draw(turtle)
    s2 = Snow_woman()
    s2.draw(turtle)
    turtle.getscreen()._root.mainloop()