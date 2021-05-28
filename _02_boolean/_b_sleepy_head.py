"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle
from tkinter import messagebox, Tk

from turtle import Turtle

if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    isaac = turtle.Turtle()

    weekend_var1 = True
    test_passed = True
    game_over = True

    is_red = True
    is_square = True

    if weekend_var1:
        messagebox.showinfo(None, 'it is the weekend!')
    else:
        messagebox.showinfo(None, 'So close! It is a weekday :(')

    if test_passed:
        messagebox.showinfo(None, 'You passed!')
    else:
        messagebox.showinfo(None, 'You failed:(')

    if game_over:
        messagebox.showinfo(None, 'You died, Game Over!')
    else:
        messagebox.showinfo(None, 'You are still alive')

    if is_red:
        if is_square:
            isaac.pencolor('red')
            isaac.pendown()
            isaac.forward(5)
            isaac.right(90)
            isaac.forward(5)
            isaac.right(90)
            isaac.forward(5)
            isaac.right(90)
            isaac.forward(5)
            isaac.right(90)
        else:
            messagebox.showinfo(None, 'It is red but not a square')
    else:
        messagebox.showinfo(None, 'It is neither')

    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    pass
