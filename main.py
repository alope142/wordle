#wordle clone
import random as ran
import sys
from termcolor import cprint
import os
global poly
global wordlist
wordlist=[]
low = open('words.txt').read().split('\n')

answer = low[ran.randint(0, 5750)]
poly = low


def keyboard(key, color):
    for i in range(len(key)):
        for j in range(len(key[i])):
            cprint(key[i][j], color[i][j], end="  ")
        print("")


def keyboardcolor(keyboard, keyboardcolor, maincolor, word, count, answer):
    wordlist.append(word)
    for i in range(len(keyboard)):
      for j in range(len(keyboard[i])):
        keyboardcolor[i][j]="white"
    
    for i in range(0,5):
      for h in range(0,3):
        if word[i] in keyboard[h]:
          place=keyboard[h].index(word[i])
          keyboardcolor[h][place]=maincolor[count-1][i]


def clearConsole():
    os.system('clear')


answer = answer.upper()


def note(word, answer):
    x = []
    for i in range(0, 5):
        for j in range(0, 5):
            if word[i] != answer[j] and x.count(word[i]) < 1:
                x.append(word[i])
    return x


def guess(num):
    tester = 0
    word = input("Guess: ")
    wordlength = len(word)
    word = word.lower()
    if word in poly:
        tester = 1
    while wordlength != 5 or tester != 1:
        print("Invalid word")
        word = input("Guess: ")
        wordlength = len(word)
        if word in poly:
            tester = 1
    word = word.upper()
    wordGuessList = [s.strip() for s in word]

    return wordGuessList


def answersplit(answer):
    answer = answer.upper()
    wordAnswerList = [s.strip() for s in answer]
    return wordAnswerList


def checker(word, answer):
    color = ["white", "white", "white", "white", "white"]
    for i in range(0, 5):
        if word[i] == answer[i]:
            color[i] = "green"
        for j in range(0, 5):
            if word[i] == answer[j] and word[i] != answer[i]:
                if word[i] != word[j]:
                    color[i] = "yellow"
    return color


def linecprint(a, color):
    for i in range(len(a)):
        for j in range(len(a[i])):
            cprint(a[i][j], color[i][j], end="  ")
        print()


linearray = [["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"],
             ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"],
             ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]
win = 0
countvar = 0
answer = answersplit(answer)
guessnum = 0
word = ["_", "_", "_", "_", "_"]
color = [["white", "white", "white", "white", "white"],
         ["white", "white", "white", "white", "white"],
         ["white", "white", "white", "white", "white"],
         ["white", "white", "white", "white", "white"],
         ["white", "white", "white", "white", "white"],
         ["white", "white", "white", "white", "white"]]

keys = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
keyscolor = [[
    "white", "white", "white", "white", "white", "white", "white", "white",
    "white", "white"
],
             [
                 "white", "white", "white", "white", "white", "white", "white",
                 "white", "white"
             ],
             ["white", "white", "white", "white", "white", "white", "white"]]

linecprint(linearray, color)
print()
usedlist = []
while win == 0:
    keyboardcolor(keys, keyscolor, color, word, countvar, answer)
    keyboard(keys, keyscolor)
    print("\n")
    word = guess(guessnum)
    
    clearConsole()
    linearray[guessnum] = word
    color[guessnum] = checker(word, answer)

    linecprint(linearray, color)
    guessnum += 1
    print('')
    if word == answer:
        win = 1
    countvar += 1
    if countvar == 6:
        win = 2
if win == 1:
    print("Word found \n\nCongrats")
else:
    print("")
    print("Word was: ", end=" ")
    for i in range(0, 5):
        print(answer[i], end=" ")
