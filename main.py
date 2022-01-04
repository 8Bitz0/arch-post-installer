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


user = input("What username should be used? ")

print("-- Core")
if ask_yn("Install git?", True):
    pacman("git")
if ask_yn("Install yay (AUR helper)?", True):
    os.system("cd /opt; sudo git clone https://aur.archlinux.org/yay-git.git; sudo chown -R " + user + ":" + user + " ./yay-git; cd yay-git; makepkg -si")
if ask_yn("Swap pacman.conf (enable multilib included)?", True):
    os.system("sudo echo ./pacman.conf > /etc/pacman.conf")

print("-- Utilities")
if ask_yn("Install Chromium?", True):
    pacman("chromium")

print("-- Chat")
if ask_yn("Install Discord with dvm (Discord Version Manager)? ", True):
    os.system("wget https://github.com/diced/dvm/releases/download/1.1.7/dvm-x86_64-unknown-linux-gnu")
    os.system("sudo mv dvm-x86_64-unknown-linux-gnu /bin/dvm")
    os.system("dvm install stable")