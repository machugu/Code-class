# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:16:05 2019

@author: Mgeni
"""
import tkinter
import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()