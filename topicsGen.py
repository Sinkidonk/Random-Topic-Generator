# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:01:25 2021

@author: apary
"""

import tkinter as tk

newtopic = "h"

def newTopic():
    greeting.config(text="hello")
    pass

topic = str("Topic")

window = tk.Tk()
greeting = tk.Label(
    text="Hi",
    textvariable=topic,
    fg="white",
    bg="black",
    width=30,
    height=10
)
button = tk.Button(
    text="New Topic!",
    command=newTopic,
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    )
greeting.pack()
button.pack()
window.mainloop() # Need to be at the end of the program or my GUI won't be displayed

