#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:35:04 2019

@author: au632191
"""

import pandas as pd
import numpy as np
from psychopy import visual, core, gui, event

def getParameters():
    '''Define the parameters
    '''
    
    parameters = {'winSize': [1000,1000],
                  'monitor': 'testMonitor',
                  'allowedKeys': ['left', 'right']}
    
    return parameters







# Load parameters
    
parameters = getParameters()
words_df = pd.read_excel('wordLists.xls', header=none)
listStudied = words_df['0']
listDistractor = words_df['1']




result_df= pd.DataFrame([])


#Open window
myWin = visual.Window (parameters['winSize'], monitor = parameters ['monitor'])


#Create fixation
fixation = visual.GratingStim(win=myWin, size=0.1,mask='cross', pos=[0,0], sf=0, rgb=-1)
fixation.draw()
myWin.update()

#pause, so you get a chance to see it!
core.wait(1.0)


#Draw two words. This is different from Nicolas' script
word1 = visual.TextStim(myWin, text= 'Word1', pos = (0.5, 0), units='norm') 
word2 = visual.TextStim(myWin, text= 'Word2', pos = (1, 0), units='norm')

word1.draw()
word2.draw()

clock =core.Clock()
myWin.update()


#Get subject answer
responseKey = event.waitKeys(timeStamped=clock,maxWait = 2.0, keyList = parameters['allowedKeys'])

if responseKey is None:
    warning = visual.TextStim(myWin, text= 'Too late!') 
    warning.draw()
    myWin.update()
    core.wait(0.5)
    rt, keyPressed= 'Nan', 'Nan'
else:
    keyPressed = responseKey[0][0]
    rt =responseKey[0][1]

#Update the result dataFrame
    
    result_df = result_df.append({'RT':rt, 'keyPressed': keyPressed}, ignore_index=True)
    
    #it will create result in the current folder as results.txt
    result_df.to_csv('results.txt')

myWin.close()




