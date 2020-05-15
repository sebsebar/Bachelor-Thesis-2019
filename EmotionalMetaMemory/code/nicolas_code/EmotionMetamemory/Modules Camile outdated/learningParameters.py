#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:28:46 2019

@author: au632191
"""

# Learning parameters
import pandas as pd
import numpy as np
from psychopy import visual, core, gui, event


def learning(parameters,listStudied):


    
    if len(listStudied) !=50:
        raise ValueError ('Incorrectlength of study list')
    
#creating window

    myWin = visual.Window (parameters['winSize'], monitor = parameters ['monitor'])


    x_range = np.arange(-0.5, 0.5, 0.2) # 0.8
    y_range = np.arange(-0.5, 0.5, 0.1)

# Show the list on the screen

    i = 0
    for x in x_range:
        for y in y_range:
            word = visual.TextStim(myWin, text=listStudied[i], pos=(x,y),height=0.05, units ='norm')
            word.draw()
            i +=1  #i=i+1
        
        
        # Security check
    if i != 50:
        raise ValueError('Error in list presentation')
        
    myWin.update()
    core.wait(2)
    myWin.close()


          

        
