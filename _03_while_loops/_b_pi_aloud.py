"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math

i=0
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    str_pi = "3.1415926535897932384"
    print(str_pi[0], str_pi[1], str_pi[2])

    while True:
        i+=1
        next_digit = simpledialog.askstring(None, prompt="What is the next digit of pi?")
        if next_digit != str_pi[3+i]:
            next_digit = simpledialog.askstring(None, prompt="What is the next digit of pi?")
        else:
            break
    for l in range(i+3):
        messagebox.showinfo(None, str_pi[l])
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
