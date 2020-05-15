#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:01:34 2019

@author: au632191
"""
# Importing

import random
import numpy
from constants import *
from psychopy.visual import Window, TextStim
from psychopy.event import waitKeys
from psychpy.core import wait
import pandas

# d = [1]

# Trial function

# Starting with fixation
disp = Window(size=DISPSIZE, units= 'pix', fullscr=False)
fixmark = Circle(disp, radius=3, edges=64, lineColor = FGC, fillColor=FGC)
fixmark.draw()
disp.flip()
wait(2))
disp.close()

# Randomly choosing a word from the constants list
WordToDisplay = random.choice(NASTYWORDS)

# Presenting it on the monitor
WordStim = TextStim(disp, text=WordToDisplay, height = 64)
WordStim.draw()

# Updating the monitor
disp.flip()

# Waiting for a response
resplist = waitkeys(maxWait = float('inf'), keylist = ALLOWEDRESPKEYS, timeStamped = True)
# selecting the first response from the list
key, presstime = resplist[0]


if key == SEENLIST:
    correct=1
else:
    correct=0

# giving feedback
if correct:
    feedback = 'Well done!'
    fbcolour = (-1,1,-1)
else:
    feedback = '!Ooops!'
    fbcolour = (1, -1, -1)

#creating a stimulus for the feedback text
    fbstim = TextStim(disp, text=feedback, color=fbcolour, height = 24)
    fbstim.draw()
    disp.flip()


#Closing the display

disp.close()

#Micah's snip
#word1 = TextStim(disp, text = text1)
#word1.pos = (1, 0)
#word2 = TextStim(disp, text = text2)
#word2.pos = (-1, 0)
#
#word1.draw()
#word2.draw()
#disp.flip()
#wait(2)
#
#disp.close()
