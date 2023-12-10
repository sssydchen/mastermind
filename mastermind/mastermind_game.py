'''
    CS 5001, Fall 2023
    Final Project -- Mastermind
    Yifan Chen
'''
import turtle
from GameSettings import GameSettings

def main():
    # create an instance of GameSettings
    G = GameSettings()
    G.draw_board()
    turtle.onscreenclick(G.on_click)
    turtle.mainloop()

if __name__ == "__main__":
    main()
