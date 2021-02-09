# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:01:25 2021

@author: apary
"""

import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text="Hello,Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
button = tk.Button(
    text="New Topic!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    )
greeting.pack()
button.pack()
window.mainloop() # Need to be at the end of the program or my GUI won't be displayed

