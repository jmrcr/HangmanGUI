#!/usr/local/bin/python3
"""
-------------------------------------------------------
| Written by Joseph Mercer; released to public domain |
-------------------------------------------------------
"""

import sys
from random import randint, choice
import tkinter


class Hangman:

    def __init__(self, master):
        self.master = master
        topFrame = tkinter.Frame(self.master)
        master.geometry("500x500")
        master.resizable(False, False)
        self.mainmenu()

    def buttonMake(self, imgName, x, y, func):
        buttonImage = tkinter.PhotoImage(file=imgName)
        button = tkinter.Button(self.master, image=buttonImage, borderwidth=0, highlightthickness=0)
        buttonImage.image = buttonImage
        button.place(x=x, y=y)
        button.config(command=func)
        return button

    def labelMake(self, imgName, x, y):
        labelImage = tkinter.PhotoImage(file=imgName)
        label = tkinter.Label(self.master, image=labelImage, borderwidth=0, highlightthickness=0)
        labelImage.image = labelImage
        label.place(x=x, y=y)

    def backgroundMake(self):
        backgroundImage = tkinter.PhotoImage(file="background.png")

        background = tkinter.Label(tk, image=backgroundImage)
        backgroundImage.image = backgroundImage
        background.place(x=0, y=0, relwidth=1, relheight=1)

    def mainmenu(self):
        background = self.backgroundMake()

        buttonQuit = self.buttonMake("buttonQuit.png", 320, 325, sys.exit)
        buttonPlay = self.buttonMake("buttonPlay.png", 74, 325, self.play)
        buttonHelp = self.buttonMake("buttonHelp.png", 197, 325, self.instructions)
        labelTitle = self.labelMake("title.png", 105, 79)
        labelCredit = self.labelMake("credit.png", 344, 422)
        labelHanger = self.labelMake("hanger.png", 177, 140)

    def instructions(self):
        background = self.backgroundMake()

        buttonBack = self.buttonMake("buttonBack.png", 197, 325, self.mainmenu)

    def play(self):
        background = self.backgroundMake()

        buttonHard = self.buttonMake("buttonHard.png", 74, 325, lambda: self.wordList(4))
        buttonNormal = self.buttonMake("buttonNormal.png", 186, 325, lambda: self.wordList(2))
        buttonEasy = self.buttonMake("buttonEasy.png", 320, 325, lambda: self.wordList(0))

    def wordList(self, x):
        randWord = choice(open("wordList.txt").read().split(',')[6])
        self.lines = open("wordList.txt").readlines()
        self.line = self.lines[x]
        self.words = self.line.split(', ')
        self.randWord = choice(self.words)
        print(self.line)

tk = tkinter.Tk()
h = Hangman(tk)
tk.mainloop()
