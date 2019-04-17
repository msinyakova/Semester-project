#!/usr/bin/env python3

from tkinter import *

CONST_PROJECT_NAME_WIDTH = 50
CONST_TEXT_WIDTH = 50
CONST_TEXT_HEIGHT = 25
CONST_LOG_HEIGHT = 5
CONST_LOG_WIDTH = 100

CONST_PADX = 10
CONST_PADY = 10
CONST_WORD_WIDTH = 15
CONST_INPUT_WIDTH = 20

def startMarkov(*args) :
    print("startMarkov")

def stepMarkov(*args) :
    print("stepMarkov")

def stopMarkov(*args) :
    print("stopMarkov")

def inputWord(*args) :
    print("inputWord")

def mainRules(*args) :
    print("mainRules")

root = Tk()
root.title = "Марков"
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

result = StringVar()
result.set("abcd")

#------------------------LABELS--------------------
label_project_name = Label(root, text = "Нормальные алгоритмы Маркова", width = CONST_PROJECT_NAME_WIDTH)
label_project_name.configure(fg = "deep pink")
label_project_name.grid(row = 0, column = 2, columnspan = 4, pady = CONST_PADY)

label_input_word = Label(root, text = "Входное слово:", width = CONST_WORD_WIDTH)
label_input_word.configure(fg = "midnight blue")
label_input_word.grid(row = 1, column = 0, columnspan = 2 , sticky = N)

label_output_word = Label(root, text = "Выходное слово:", width = CONST_WORD_WIDTH)
label_output_word.configure(fg = "midnight blue")
label_output_word.grid(row = 1, column = 6 , columnspan = 2 , sticky = N)

label_alphabet = Label(root, text = "Алфавит:",width = 10)
label_alphabet.configure(fg = "midnight blue")
label_alphabet.grid(row = 3, column = 2, columnspan = 1, pady = CONST_PADY, sticky = E)

label_rule = Label(root, text = "Правила:", width = CONST_WORD_WIDTH)
label_rule.configure(fg = "midnight blue")
label_rule.grid(row = 4, column = 0, columnspan = 2 , sticky = S+W)#, padx = CONST_PADX)

label_exec = Label(root, text = "Ход выполнения:", width = CONST_WORD_WIDTH)
label_exec.configure(fg = "midnight blue")
label_exec.grid(row = 4, column = 4 , columnspan = 2 , sticky = S+W, padx = 20)

#------------------------TEXT-----------------
textbox_input_word = Entry(root, width = CONST_INPUT_WIDTH)
textbox_input_word.grid(row = 2, column = 0, columnspan = 2, padx = CONST_PADX, sticky = S)
textbox_input_word.bind("<Key>", inputWord)

textbox_output_word = Entry(root, width = CONST_INPUT_WIDTH, textvariable = result)
textbox_output_word.config(state = DISABLED)
textbox_output_word.grid(row = 2, column = 6, columnspan = 2, padx = CONST_PADX, sticky = S)

textbox_alphabet = Text(root, width = 20, height = 1)
textbox_alphabet.insert(1.0, "abc*")
textbox_alphabet.config(state = DISABLED)
textbox_alphabet.grid(row = 3, column = 3, columnspan = 2, pady = CONST_PADY, sticky = W)

text_algorithm = Text(root, width = CONST_TEXT_WIDTH, height = CONST_TEXT_HEIGHT, wrap = WORD)
text_algorithm.grid(row = 5, column = 0, columnspan = 4, sticky = W, pady = CONST_PADY, padx = CONST_PADX)
text_algorithm.bind("<Key>", mainRules)

text_logs = Text(width = CONST_LOG_WIDTH, height = CONST_LOG_HEIGHT)
text_logs.config(state = DISABLED)
text_logs.grid(row = 7,column = 0, columnspan = 8, padx = CONST_PADX, pady = CONST_PADY)

#------------------------LISTBOX------------------
listbox_algorithm = Listbox(root, width = CONST_TEXT_WIDTH-2, height = CONST_TEXT_HEIGHT-1)
listbox_algorithm.config(state = DISABLED)
listbox_algorithm.grid(row = 5, column = 4, columnspan = 4, sticky = E, padx = CONST_PADX)

#----------------------BUTTONS-----------------------
button_start = Button(root, text = "Start", width = 15)
button_start.configure(bg = "green", fg =  "yellow")
button_start.grid(row = 6, column = 0, columnspan = 2, padx = CONST_PADX, pady = CONST_PADY)
button_start.bind("<Button-1>", startMarkov)

button_stop = Button(root, text = "Stop", width = 15)
button_stop.configure(bg = "red", fg = "white")
button_stop.grid(row = 6, column = 2, columnspan = 2, padx = CONST_PADX, pady = CONST_PADY)
button_stop.bind("<Button-1>", stopMarkov)

button_step = Button(root, text = "Step", width = 15)
button_step.configure(bg = "MediumPurple2", fg = "antique white")
button_step.grid(row = 6, column = 4, columnspan = 2, padx = CONST_PADX, pady = CONST_PADY)
button_step.bind("<Button-1>", stepMarkov)

button_exit = Button(root, text = "Exit",width = 15,command = root.quit)
button_exit.configure(bg = "antique white", fg = "red")
button_exit.grid(row = 6, column = 6, columnspan = 2, padx = CONST_PADX, pady = CONST_PADY)

root.mainloop()
