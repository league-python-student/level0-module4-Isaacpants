"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math

i=0
points = 0
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    str_pi = "3.1415926535897932384"
    true = True

    while true:
        next_digit = ''
        next_digit = simpledialog.askstring(None, prompt="What is the next digit of pi?")
        if next_digit == str_pi[i]:
            points+=1
        elif next_digit != str_pi[i]:
            true = False
        i += 1
    messagebox.showinfo(None, 'Good job, you got '+str(points) +' digits of pi')
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
