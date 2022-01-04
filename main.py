#!/usr/env python3

def ask_yn(text, recommended):
    if recommended == True:
        possible_answers = " [Y/n]"

    elif recommended == False:
        possible_answers = " [y/N]"

    while True:
        answer = input(text + possible_answers)
        if answer == "y" or "Y":
            return True

        elif answer == "n" or "N":
            return False

        elif answer == "":
            if recommended == True:
                return True

            elif recommended == False:
                return False

        else:
            print("Invalid input!")