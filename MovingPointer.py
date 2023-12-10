'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen

    This is the MovingPointer class
'''
import turtle

class MovingPointer:
    '''
    This class creates a moving pointer instance and has a move
    method to move it vertically.

    Attributes:
        pen -- a turtle object
        visible -- a boolean flag indicating the 
                    visibility of the MovingPointer object
    '''
    def __init__(self, wid, len, outline, fillcolor, pencolor):
        '''
        Constructor -- create a moving pointer instance
        Parameters:
            self -- the current object
            wid (float) -- the width of the pointer
            len (float) -- the length of the pointer
            outline (float) -- the outline of the pointer
            fillcolor (str) -- the fillcolor of the pointer
            pencolor (str) -- the pencolor of the pointer    
        '''
        self.pen = self.new_pen(wid, len, outline, fillcolor, pencolor)
        self.visible = False
    
    def new_pen(self, wid, len, outline, fillcolor, pencolor):
        '''
        Method: new_pen
            create a new object
        Parameters:
            self -- the current object
            wid (float) -- the width of the pen
            len (float) -- the length of the pen
            outline (float) -- the outline of the pen
            fillcolor (str) -- the fillcolor of the pen
            pencolor (str) -- the pencolor of the pen
        Returns the turtle object 
        '''
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shapesize(stretch_wid=wid, stretch_len=len, outline=outline)
        pen.pen(fillcolor=fillcolor, pencolor=pencolor)
        pen.hideturtle()
        return pen

    def move(self, x, y):
        '''
        Method: move
            move the pointer vertically to the target position
        Parameters:
            self -- the current object
            x -- the x-coordinate of the target position
            y -- the y-coordinate of the target position
        Returns None
        '''       
        self.visible = True
        self.pen.showturtle()
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
