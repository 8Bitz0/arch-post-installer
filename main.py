#!/usr/env python3

import os

def ask_yn(text, recommended):
    if recommended == True:
        possible_answers = " [Y/n]: "

    elif recommended == False:
        possible_answers = " [y/N]: "

    while True:
        answer = input(text + possible_answers)
        if answer == "y" or answer == "Y":
            return True

        elif answer == "n" or answer == "N":
            return False

        elif answer == "":
            if recommended == True:
                return True

            elif recommended == False:
                return False

        else:
            print("Invalid input!")

def pacman(package):
    os.system("sudo pacman -S " + package)

def yay(package):
    os.system("yay -S " + package)