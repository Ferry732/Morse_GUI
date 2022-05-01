import RPi.GPIO as GPIO
import time
from guizero import App, Text, PushButton, TextBox
import tkinter as tk
from tkinter import *

window = Tk()

def enterr():
    inputt = entry.get()
    
    if len(inputt) > 12:
        print('input has exceeded 12 characters try again')
    
    else:
        for letter in inputt:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.5)
            time.sleep(0.5)

#enter_button = tk.Button(entry,
 #                        text = "send",
  #                       command = enterr)
#enter_button.pack()

enter_button = Button(window, text="send", command=enterr)
enter_button.pack()

entry = Entry()
entry.config(font=('comic sans', 30))
entry.config(bg= 'orange')
entry.config(fg= 'dark blue')
entry.config(width = 100)

entry.pack()

#win.title("Morse your input")
#win.geometry('250x250')




          

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
ledPin=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


def dot():
    GPIO.output(ledPin,1)
    time.sleep(0.25)
    GPIO.output(ledPin,0)
    time.sleep(0.25)

def dash():
    GPIO.output(ledPin,1)
    time.sleep(0.5)
    GPIO.output(ledPin,0)
    time.sleep(0.25)
    
#inputt = input('What would you like to send? ')
#while len(inputt) > 12:
 
 #   print('input has exceeded 12 characters try again')
  #  inputt = input('What would you like to send? ')
    

    

    
#lbl = tk.Label(win, text = "What would you like to send")
#lbl.pack()
    
entry.mainloop()
    
    