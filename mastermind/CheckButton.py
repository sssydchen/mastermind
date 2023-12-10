'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen

    This is the CheckButton class
'''
import turtle

class CheckButton:
    '''
    A class to represent all three checkbuttons

    Attributes:
        pen -- the turtle object
        x (float) -- the x-coordinate of the message gif
        y (float) -- the y-coordinate of the message gif
        image (str) -- the name of the ceheckbutton image
        size (float) -- the size of the image
    '''
    def __init__(self, x, y, image, size):
        '''
        Constructor -- create a new CheckButton instance
        Parameters:
            self -- the current object
            x (float) -- the x-coordinate of the CheckButton
            y (float) -- the y-coordinate of the CheckButton
            image (str) -- the name of the ceheckbutton image
            size (float) -- the size of the image             
        '''
        self.pen = self.new_pen()
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        
        turtle.register_shape(self.image)

    def new_pen(self):
        '''
        Method: new_pen
            Create a new turtle object
        Parameter:
            self -- the current object
        Returns a turtle object
        '''
        return turtle.Turtle()
    
    def draw(self):
        '''
        Method: draw
            Draw the CheckButtons
        Parameter:
            self -- the current object
        Returns None
        '''
        self.pen.speed('fastest')
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.shape(self.image)

    def clicked_in_region(self, x, y):
        '''
        Method: clicked_in_region
            Return a boolean indicating if the click 
            is inside the checkbutton
        Parameter:
            self -- the current object
            x -- the x-coordinate of the click
            y -- the y-coordinate of the click
        Returns True or False
        '''
        if abs(x - self.x) <= self.size  and \
            abs(y - self.y) <= self.size * 2:
            return True
        else:
            return False
 