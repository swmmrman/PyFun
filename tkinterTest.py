#!/usr/bin/env python3

import tkinter

window = tkinter.Tk();
frame = tkinter.Frame(window)
frame.grid(column=0, row=0)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.pack(padx=100, pady=100)

tkvar = tkinter.StringVar(window)

choices = {'Test', 'Test2', 'Test3'}
tkvar.set('Test')

popMenu = tkinter.OptionMenu(frame, tkvar, *choices)
target = tkinter.Label(frame, text='Pick a Test')
target.grid(row=1, column=1)
popMenu.grid(row=2, column=1)

def changeTarget(*args):
    target.config( text=tkvar.get() )

tkvar.trace('w', changeTarget)

window.mainloop()
