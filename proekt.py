#!/usr/bin/env python3

from tkinter import *
import re

CONST_ALPHABET = ['a','b','c','*']

CONST_PROJECT_NAME_WIDTH = 50
CONST_TEXT_WIDTH = 50
CONST_TEXT_HEIGHT = 25
CONST_LOG_HEIGHT = 5
CONST_LOG_WIDTH = 100

CONST_PADX = 10
CONST_PADY = 10
CONST_PADY_FIRST = 50
CONST_WORD_WIDTH = 15
CONST_INPUT_WIDTH = 20

CONST_ITERATION = 1000

root = Tk()

Errors = {
    "empty" : "Пустое входное слово\n",
    "done" : "Алгоритм выполнен\n",
    "cycle" : "Алгорит зациклился\n"}

# return list | bool
def parseRules(rules) :
    i = 1
    lst = []
    template = '(['+''.join(CONST_ALPHABET)+']*)(\\|?)->'+'(['+''.join(CONST_ALPHABET)+']*)$'
    for rule in rules :
      if (rule.rstrip() == '') :
        continue
      res = re.match(template,rule.rstrip(),re.MULTILINE)
      if (type(res) == type(None)):
        text_logs.insert(1.0,rule + "\n")
        text_logs.insert(1.0,"Ошибка в алгоритме, строчка номер: " + str(i) + "\n")
        return False
      i += 1
      lst.append([res.group(1),res.group(3), not (res.group(2) == '')])
    return lst

# return lst
def doIteration(rules,sinput) :
    flag = True
    i = 0
    for rule in rules :
      stmp = sinput.replace(rule[0],rule[1],1)
      if (stmp != sinput) :
        sinput = stmp
        if (rule[2]) :
          break
        flag = False
        break
      i += 1
    return [sinput,flag,i]

def startMarkov(event) :
    if (save_rules != False) :
      return
    if (input_.get() == '') : 
      text_logs.insert(1.0, Errors["empty"])
      return
    rules = parseRules(text_algorithm.get(1.0,END).split("\n"))
    if (rules == False) :
      return
    uploadRules(rules) 
    sinput = input_.get()
    i = 0
    while(True) :
      if (i >= CONST_ITERATION) :
        text_logs.insert(1.0, Errors["cycle"])
        return
      iter_res = doIteration(rules,sinput)
      sinput = iter_res[0]
      if (iter_res[1]) :
        break
      i += 1
    result.set(sinput)
    text_logs.insert(1.0, Errors["done"])

save_rules = False
#return bool 
def initSteps() :
    if (input_.get() == '') : 
      text_logs.insert(1.0, Errors["empty"])
      return False
    global save_rules
    save_rules = parseRules(text_algorithm.get(1.0,END).split("\n"))
    if (save_rules == False) :
      return False
    uploadRules(save_rules)
    button_start.config(state = DISABLED)
    textbox_input_word.config(state = DISABLED)
    text_algorithm.config(state = DISABLED)
    result.set(input_.get())
    return True

#void
def uploadRules(rules) :
    listbox.delete(0,END)
    for index in range(len(rules)) :
      if (rules[index][2]) :
        arrow = "  \u21A6  "
      else :
        arrow = "  \u2192  "
      rule_number = '   (' + str(index) + ')   '
      listbox.insert(END,rule_number + rules[index][0] + arrow + rules[index][1])

def endStep() :
    global save_rules
    save_rules = False
    button_start.config(state = NORMAL)
    textbox_input_word.config(state = NORMAL)
    text_algorithm.config(state = NORMAL)

def stepMarkov(event) :
    if (save_rules == False) :
      if (initSteps() == False) :
        return
    iter_res = doIteration(save_rules,result.get())
    result.set(iter_res[0])
    if (iter_res[2] < listbox.size()):
      for i in range(0,listbox.size()) :
        listbox.itemconfig(i,bg = "white", fg = "dark slate gray")
      listbox.itemconfig(iter_res[2],bg = "SlateBlue4", fg = "snow")
    if (iter_res[1]) :
      endStep()
      text_logs.insert(1.0, Errors["done"])
      return

def stopMarkov(*args) :
    endStep()
    result.set('')

def inputWord(act,inp) :
    if (act == '0'):
      return True
    if (inp in CONST_ALPHABET):
      return True
    return False

inputWord_reg = (root.register(inputWord),"%d","%S")

root.title = "Markov"
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

result = StringVar()

input_ = StringVar()
input_.set("aaaaa");

#------------------------LABELS--------------------
label_project_name = Label(root, text = "Нормальные алгоритмы Маркова", width = CONST_PROJECT_NAME_WIDTH)
label_project_name.configure(fg = "deep pink")
label_project_name.grid(row = 0, column = 2, columnspan = 4, pady = CONST_PADY_FIRST)

label_input_word = Label(root, text = "Входное слово:", width = CONST_WORD_WIDTH)
label_input_word.configure(fg = "midnight blue")
label_input_word.grid(row = 1, column = 0, columnspan = 2 , sticky = N + S)

label_output_word = Label(root, text = "Выходное слово:", width = CONST_WORD_WIDTH)
label_output_word.configure(fg = "midnight blue")
label_output_word.grid(row = 1, column = 6 , columnspan = 2 , sticky = N + S)

label_simbols = Label(root, text = "Обозначения стрелок:")
label_simbols.configure(fg = "midnight blue")
label_simbols.grid(row = 1, column = 2, columnspan = 4, sticky = S)

label_arrow = Label(root, text = " \u21A6 : |->   \u2192 : -> ")
label_arrow.configure(fg = "midnight blue")
label_arrow.grid(row = 2, column = 2, columnspan = 4, sticky = N)

label_alphabet = Label(root, text = "Алфавит:",width = 10)
label_alphabet.configure(fg = "midnight blue")
label_alphabet.grid(row = 3, column = 2, columnspan = 1, pady = CONST_PADY_FIRST, sticky = E)

label_rule = Label(root, text = "Правила:", width = CONST_WORD_WIDTH)
label_rule.configure(fg = "midnight blue")
label_rule.grid(row = 4, column = 0, columnspan = 2 , sticky = S+W)#, padx = CONST_PADX)

label_exec = Label(root, text = "Ход выполнения:", width = CONST_WORD_WIDTH)
label_exec.configure(fg = "midnight blue")
label_exec.grid(row = 4, column = 4 , columnspan = 2 , sticky = S+W, padx = 20)

#------------------------TEXT-----------------
textbox_input_word = Entry(root, width = CONST_INPUT_WIDTH, textvariable = input_)
textbox_input_word.grid(row = 2, column = 0, columnspan = 2, padx = CONST_PADX, sticky = S)
textbox_input_word.config(validate = "key", validatecommand=inputWord_reg)

textbox_output_word = Entry(root, width = CONST_INPUT_WIDTH, textvariable = result)
textbox_output_word.config(state = DISABLED)
textbox_output_word.grid(row = 2, column = 6, columnspan = 2, padx = CONST_PADX, sticky = S)

textbox_alphabet = Text(root, width = 20, height = 1)
textbox_alphabet.insert(1.0, "abc*")
textbox_alphabet.config(state = DISABLED)
textbox_alphabet.grid(row = 3, column = 3, columnspan = 2, pady = CONST_PADY, sticky = W)

text_algorithm = Text(root, width = CONST_TEXT_WIDTH, height = CONST_TEXT_HEIGHT, wrap = WORD)
text_algorithm.grid(row = 5, column = 0, columnspan = 4, sticky = W, pady = CONST_PADY, padx = CONST_PADX)
file = open("test.txt", "r")
algorithm_rules = file.read()
text_algorithm.insert(0.0, algorithm_rules)

text_logs = Text(width = CONST_LOG_WIDTH, height = CONST_LOG_HEIGHT)
text_logs.grid(row = 7,column = 0, columnspan = 8, padx = CONST_PADX, pady = CONST_PADY)

#------------------------LISTBOX------------------
listbox = Listbox(root, width = CONST_TEXT_WIDTH-2, height = CONST_TEXT_HEIGHT-1)
listbox.grid(row = 5, column = 4, columnspan = 4, sticky = E, padx = CONST_PADX)

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
