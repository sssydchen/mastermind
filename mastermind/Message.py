'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen

    This is the Message class
'''
import turtle

class Message:
    '''
    This class can display and clear a message picture.

    Attributes:
        x (float) -- the x-coordinate of the message gif
        y (float) -- the y-coordinate of the message gif
        filename (str) -- the name of the message gif
        pen -- a turtle object
    '''
    def __init__(self, x, y, filename):
        '''
        Constructor -- create a new Message instance
        Parameters:
            self -- the current object
            x (float) -- the x-coordinate of the message gif
            y (float) -- the y-coordinate of the message gif
            filename (str) -- the name of the message gif       
        '''
        self.x = x
        self.y = y
        self.pen = self.new_pen()
        self.pen.hideturtle()
        self.filename = filename
        turtle.register_shape(filename)

    def new_pen(self):
        '''
        Method: new_pen
            Create a new turtle object
        Parameter:
            self -- the current object
        Returns a turtle object
        '''
        return turtle.Turtle()
 
    def display(self):
        '''
        Method: display
            Display the message gif
        Parameter:
            self -- the current object
        Returns None
        '''       
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.shape(self.filename)
        self.pen.showturtle()
        turtle.ontimer(self.clear, t=1000) 
    
    def clear(self):
        '''
        Method: clear
            Clear all the messages displayed on the screen
        Parameter:
            self -- the current object
        Returns None
        '''
        self.pen.clear()
        self.pen.hideturtle()

