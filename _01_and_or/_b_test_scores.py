"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk

# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    test1 = simpledialog.askstring(None, "What did you get on your first test?")
    test2 = simpledialog.askstring(None, "What did you get on your second test?")
    int_test1 = float(test1)
    int_test2 = float(test2)

    both_tests = (int_test1+int_test2)/2
    both_tests
    if both_tests >= 89.5:
        messagebox.showinfo(None, 'You got a ' + str(both_tests) + ' Thats an A, you must have studied hard!')
    elif both_tests >= 79.5 and both_tests < 89.5:
        messagebox.showinfo(None, 'You got a ' + str(both_tests) + ' Thats a B, not bad!')
    elif both_tests >= 69.5 and both_tests < 79.5:
        messagebox.showinfo(None, 'You got a ' + str(both_tests) + ' Thats a C, you need to study more!')
    elif both_tests >= 59.5 and both_tests < 69.5:
        messagebox.showinfo(None, 'You got a ' + str(both_tests) + ' Thats a D, you need to work harder and sleep more!')
    elif both_tests >= 49.5 and both_tests < 59.5:
        messagebox.showinfo(None, 'You got a ' + str(both_tests) + ' Thats an F, EEK!')
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable

    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable

    # TODO) Take the average score of both tests (total score / 2)

    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    pass
