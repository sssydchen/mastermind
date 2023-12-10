'''
    CS 5001, Fall 2023
    Final Project -- mastermind
    Yifan Chen

    This is the GameSettings class.
'''
import turtle
import json
import time
import random
from Point import Point
from Marble import Marble
from CheckButton import CheckButton
from Message import Message
from MovingPointer import MovingPointer
from datetime import datetime
from GameLogic import GameLogic

class GameSettings:
    '''
    The GameSettings class is responsible for managing the game settings for
    the mastermind game. It contains methods to capture errors, load files, 
    record and renew player records, create and draw marbles, and process the 
    drawing after clicking check buttons.
    '''
    def __init__(self):
        '''
        Constructor -- create a new GameSettings class instance
        Parameter:
            self -- the current object
        Returns None
        '''
        # initializing the attributes
        self.player_name = None
        self.pen = self.new_pen()
        self.pen.hideturtle()
        self.answers = []
        self.row_index = 0
        self.column_index = 0
        self.count = 0
        self.buttons = []
        self.pegs = []
        self.marbles = []
        self.scoring_pegs = []
        self.player_found = False
        self.player_records = {}
        
        # initializing message objects
        self.bound_msg = Message(0, 0, "bound_msg.gif")
        self.winner_msg = Message(0, 0, "winner.gif")
        self.quit_msg = Message(0, 0, "quitmsg.gif")
        self.duplicate_msg = Message(0, 0, "duplicate_msg.gif")
        self.lose_msg = Message(0, 0, "Lose.gif")
        self.unfill_msg = Message(0, 0, "unfill_msg.gif")
        self.leaderboard_msg = Message(0, 0, "leaderboard_error.gif")
        self.config_msg = Message(0, 0, "file_error.gif")

        # initializing checkbutton objects
        self.checkbutton = CheckButton(20, -280, "checkbutton.gif", 30)
        self.xbutton = CheckButton(100, -280, "xbutton.gif", 30)
        self.quitbutton = CheckButton(220, -280, "resized_quit.gif", 30)

        # initializing pointer object
        self.pointer = MovingPointer(2, 2, 2, "red", "black")
        
        # initializing colors and secret code
        self.colors = self.create_colors()
        self.secret_code = self.create_secrete_code()

    def error_capture(self, err):
        '''
        Method: error_capture
            Captures the error and the date/time of the error
        Parameters:
            self -- the current object
            err -- the error to be captured
        Returns None
        '''
        with open("mastermind_errors.err", mode="a") as errors:
            now = datetime.now().strftime("%m/%d/%Y %H:%M:%S:")
            errors.write(f"Time: {now} {str(err)}\n")
    
    def load_config(self):
        '''
        Method: load_config
            Load the configurations
        Parameters:
            self -- the current object
        Returns None
        '''        
        try:
            with open("config.json", mode='r') as config:
                return json.load(config)
        except Exception as error:
            self.config_msg.display()
            self.error_capture(error)
            return self.default_config()
    
    def default_config(self):
        '''
        Method: default_config
            Returns the defaut values
        Parameters:
            self -- the current object
        Returns the default values of username and colors
        '''
        return {"username": "unknown_user",
                "colors": ["red", "blue", "green", "yellow", "purple", "black"]}

    def new_pen(self):
        '''
        Method: new_pen
            Create a new turtle object
        Parameters:
            self -- the current object
        Returns a turtle object
        '''
        pen = turtle.Turtle()
        pen.speed(0)
        return pen
    
    def create_guess_buttons(self):
        '''
        Method: create_guess_buttons
            Create six guess buttons
        Parameters:
            self -- the current object
        Returns None
        '''
        start_x = -240
        start_y = -300

        for color in self.colors:
            self.buttons.append(Marble(Point(start_x, start_y), color, size=15))
            start_x += 40 
    
    def create_marbles(self):
        '''
        Method: create_marbles
            Create 40 marble objects
        Parameters:
            self -- the current object
        Returns None
        '''
        rows = 10
        cols = 4
        start_x = -250
        start_y = 250
        x_spacing = 40
        y_spacing = 50
        size = 15
        
        for i in range(rows):
            row = []
            for j in range(cols):
                x = start_x + j * x_spacing
                y = start_y - i * y_spacing
                row.append(Marble(Point(x, y), '', size=size))
            self.marbles.append(row)

    def create_colors(self):
        '''
        Method: create_colors
            Create the six colors
        Parameters:
            self -- the current object
        Returns a list containing six colors
        '''
        colors = self.load_config()["colors"]
        return colors

    def create_secrete_code(self):
        '''
        Method: create_secrete_code
            Create a secrete code list
        Parameters:
            self -- the current object
        Returns a secrete code list
        '''
        return random.sample(self.colors, 4)

    def draw_rectangle(self, x, y, width, height, pen_color):
        '''
        Method: draw_rectangle
            Draw a rectangle
        Parameters:
            self -- the current object
            x1 -- the start x position
            y1 -- the start y position
            width -- the width of the rectangle
            height -- the height of the rectangle
            pen_color -- the color of the pen
        Returns None
        '''
        self.pen.pensize(4)
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        
        self.pen.pencolor(pen_color)
        self.pen.forward(width)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.right(90)
        self.pen.forward(width)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.right(90)
    
    def draw_marbles(self):
        '''
        Method: draw_marbles
            Draw the 40 marbles
        Parameters:
            self -- the current object
        Returns None
        '''
        for row in self.marbles:
            for marble in row:
                marble.draw_empty()

    def draw_pegs(self):
        '''
        Method: draw_pegs
            Draw 40 pegs
        Parameters:
            self -- the current object
        Returns None
        '''
        rows = 10
        start_x = -50
        start_y = 270
        block_y_spacing = 50
        peg_x_spacing = 15
        peg_y_spacing = 20
        size = 5
        for i in range(rows):
            current_start_y = start_y - i * block_y_spacing
            peg_block = []
            for j in range(2):  
                peg_row = []
                for k in range(2): 
                    x = start_x + k * peg_x_spacing
                    y = current_start_y - j * peg_y_spacing
                    peg = Marble(Point(x, y), '', size=size)
                    peg.draw_empty()
                    peg_row.append(peg)
                peg_block.append(peg_row)
            self.pegs.append(peg_block)
    
    def draw_guess_buttons(self):
        '''
        Method: draw_guess_buttons
            Captures the error and the date/time of the error
        Parameters:
            self -- the current object
            err -- the error to be captured
        Returns None
        '''
        for button in self.buttons:
            button.draw()

    def write_text(self, x, y, text):
        '''
        Method: write_text
            Write text on the screen
        Parameters:
            self -- the current object
            x -- the start x position
            y -- the start y position
            text -- the text to be written
        Returns None
        '''  
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.write(text, True, align="left", font=("Arial", 16, "bold"))  
    
    def create_player_records(self):
        '''
        Method: create_player_records
            Create a dictionary to record player score
        Parameters:
            self -- the current object
        Returns None
        '''
        try:
            with open("leaderboard.txt", mode="r") as leaderboard:
                for line in leaderboard:
                    record_line = line.strip()
                    record = record_line.split(": ")
                    count = int(record[0])
                    name = record[1]
                    self.player_records[name] = count
        # if unable to find the leaderboard file
        # capture the error and create a new file
        except Exception as error:
            self.leaderboard_msg.display()
            self.error_capture(error)
            with open("leaderboard.txt", mode="w") as leaderboard:
                pass             

    def renew_player_records(self):
        '''
        Method: renew_player_records
            Renew the records when the same player gains a higher score
        Parameters:
            self -- the current object
        Returns None
        '''
        if self.player_name in self.player_records:
            if self.count < self.player_records[self.player_name]:
                self.player_records[self.player_name] = self.count 
        else:
            self.player_records[self.player_name] = self.count

        # sort the dictionary by score
        sorted_records = sorted(self.player_records.items(), key=lambda x: x[1])

        # write the records to a file
        with open("leaderboard.txt", "w") as file:
            for name, score in sorted_records:
                file.write(f"{score}: {name}\n")

    def clear_all_messages(self):
        '''
        Method: clear_all_messages
            Clear all the visual message popups
        Parameters:
            self -- the current object
        Returns None
        '''
        self.bound_msg.clear()
        self.duplicate_msg.clear()
        self.unfill_msg.clear()
        self.winner_msg.clear()
        self.lose_msg.clear()
        self.quit_msg.clear()

    def display_players(self, x, y):
        '''
        Method: display_players
            Display the player names on the leaderboard
        Parameters:
            self -- the current object
            x -- the start x position
            y -- the start y position
        Returns None
        '''
        self.pen.pensize(1)
        self.pen.penup()
        self.write_text(x, y, "Leaders: ")
        y -= 60
        # set the maximum lines to display as 10
        MAX_LINE = 10
        try:
            with open("leaderboard.txt", mode='r') as players:
                i = 0
                for line in players:
                    if i < MAX_LINE: 
                        self.write_text(x, y, line)
                        i += 1
                        y -= 20
                    else:
                        break
        except Exception as error:
            self.error_capture(error)

    def on_click_xbutton(self):
        '''
        Method: on_click_xbutton
            When click the xbutton, clear answers and reset guess buttons
        Parameters:
            self -- the current object
        Returns None
        '''
        for i in range(len(self.marbles[self.row_index])):
            self.marbles[self.row_index][i].draw_empty()
        self.answers = []
        self.column_index = 0
        self.draw_guess_buttons()
    
    def on_click_quitbutton(self):
        '''
        Method: on_click_quitbutton
            Display the quit message and exit the game
        Parameters:
            self -- the current object
        Returns None
        '''
        self.quit_msg.display()
        time.sleep(2)
        turtle.bye()
    
    def on_click_guess_button(self, button):
        '''
        Method: on_click_guess_button
            When click a guess button,
            color the marbles and make the current guess button empty
        Parameters:
            self -- the current object
            button -- the guess button to be clicked
        Returns None
        '''
        self.marbles[self.row_index][self.column_index].set_color(button.get_color())
        self.marbles[self.row_index][self.column_index].draw()
        self.answers.append(button.get_color())
        button.draw_empty()             
        self.column_index += 1 # move to the next marble in this row

    def on_click(self, x, y):
        '''
        Method: on_click
            Handle user clicks
        Parameters:
            self -- the current object
            x -- the x-coordinate of the click
            y -- the y-coordinate of the click
        Returns None
        '''
        self.clear_all_messages()
        button_clicked = False

        if self.xbutton.clicked_in_region(x, y):
            self.on_click_xbutton()
        elif self.quitbutton.clicked_in_region(x, y):
            self.on_click_quitbutton()
        elif self.checkbutton.clicked_in_region(x, y):
            if len(self.answers) == 4:
                self.on_click_checkbutton()
            elif len(self.answers) < 4:
                self.unfill_msg.display()
        else:
            for button in self.buttons:
                if button.clicked_in_region(x, y):
                    if len(self.answers) < 4:
                        if button.is_empty:
                            # when click an empty button,
                            # display the duplicate message
                            self.duplicate_msg.display()
                            break
                        elif self.column_index < 4:
                            self.on_click_guess_button(button)
                            if self.column_index == 4:
                                self.column_index = 0
                            break  # exit the loop after having processed one row
                    elif len(self.answers) == 4:
                        button_clicked = True
            # if there are already four answers and the player still 
            # clicks the guess button, display the bound message
            if button_clicked:
                self.bound_msg.display()

    def on_click_checkbutton(self):
        '''
        Method: on_click_checkbutton
            When click the checkbutton, check and show the different results
        Parameters:
            self -- the current object
        Returns None
        '''
        if self.row_index < len(self.marbles) and self.column_index == 0:
            code = self.secret_code
            new_game = GameLogic()
            new_game.answers = self.answers
            self.scoring_pegs = new_game.check_result(code)
            
            # reset answers for the next attempt
            self.answers = []
            self.paint_pegs()
            self.count += 1
            self.row_index += 1
            
            # if all pegs are black, the player wins 
            if self.scoring_pegs == ["black"] * 4:
                self.winner_msg.display()
                self.renew_player_records()
                time.sleep(2)
                turtle.bye()
                return
            
            # if row_index becomes 10, the player loses
            elif self.row_index == len(self.marbles):
                self.lose_msg.display()
                secret_code_text = "  ".join(self.secret_code)
                turtle.textinput("Secret code was:", secret_code_text)
                turtle.bye()

            # else, move to the next round
            else:
                self.pointer.move(
                    -280, self.marbles[self.row_index][self.column_index].position.y + 15)
                self.draw_guess_buttons()      

    def paint_pegs(self):
        '''
        Method: paint_pegs
            Paint the peg marbles according to the scoring pegs list
        Parameters:
            self -- the current object
        Returns None
        '''
        pegs_row_index = 0
        pegs_column_index = self.column_index
        for color in self.scoring_pegs:
            if pegs_column_index < len(self.pegs[pegs_row_index]):
                self.pegs[self.row_index][pegs_row_index][pegs_column_index].set_color(color)
                self.pegs[self.row_index][pegs_row_index][pegs_column_index].draw()
                pegs_column_index += 1
            
                if pegs_column_index == len(self.pegs[pegs_row_index]):
                    pegs_column_index = 0
                    pegs_row_index += 1

    def draw_board(self):
        '''
        Method: draw_board
            Draw the game board
        Parameters:
            self -- the current object
        Returns None
        '''
        turtle.setup(700, 700)
        time.sleep(1)
        self.player_name = turtle.textinput("CS5001 mastermind", "Your name:")
        # if the user click "OK" or "Cancel" without entering their name,
        # the player name will be set to the default name in the config file
        if not self.player_name:
            self.player_name = self.load_config()["username"]
        
        # turn off the animation
        self.pen._tracer(False)

        # draw the three display boards
        self.draw_rectangle(-320, 320, 400, 550, "black")
        self.draw_rectangle(120, 320, 200, 550, "blue")
        self.draw_rectangle(-320, -240, 640, 90, "black")

        # draw three check buttons
        self.checkbutton.draw()
        self.xbutton.draw()
        self.quitbutton.draw()

        # draw marbles and pegs
        self.create_marbles()
        self.draw_marbles()
        self.draw_pegs()

        # create and draw guess buttons
        self.create_guess_buttons()
        self.draw_guess_buttons()
        
        # create and display player records
        self.create_player_records()
        self.display_players(150, 280)

        self.pointer.move(-280, 270)

        # update the turtle screen and turn on the animation
        turtle.update()
        self.pen._tracer(True)
