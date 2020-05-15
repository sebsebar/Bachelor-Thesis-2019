#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on Mon Oct 21 15:33:41 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'SurveyExpMetaMem'  # from the Builder filename that created this script
expInfo = {'ParticipantID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['ParticipantID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/FlowersnIce-cream/Google Drev/EmotionalMetaMemory/code/tasks/survey_pavlovia/SurveyExpMetaMem_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intro_To_Click"
Intro_To_ClickClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome To The Emotional Meta-Memory Survey\n\nClick On the Screen To Continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
introText = visual.TextStim(win=win, name='introText',
    text='Welcome To The Word-Rating Survey \nI appreciate you for participating in this part of the study. The survey being conducted today is investigating emotion, and concerns how people respond to different types of words. On the next screens you will see some figures.\nWe call these figures SAM, and you will be using these figures to rate how different words seem to you. \nSAM shows two different kinds of feelings:\n\nHappy vs. Unhappy \nand \nExcited vs. Calm.\n \nYou will use both of these ratings for each word that is presented to you. Please notice that both feelings are arrayed along a 9-point scale. \n\nOn the happy vs. unhappy scale, which ranges from a frown to a smile, 9 means happy, pleased, satisfied, contented or hopeful. 1 on the other hand means unhappy, annoyed, unsatisfied, melancholic, despaired, or bored. If the word feels neutral to you, neither happy nor sad, you can select 5 on the ratingscale. \n\nOn the excited vs. calm scale, which ranges from a SAM to an exploding SAM, 9 means stimulated, excited, frenzied, jittered, or aroused. 1 on the other hand means relaxed, calm, sluggish, dull, sleepy, or unaroused. If the word feels neutral to you, neither exciting nor calm, you can select 5 on the ratingscale. \n\nThere will be a total of 1200 words that you will need to rated and you will be compensated 100kr for helping us with this survey part ofthe study.\n\nPlease work at a rapid place and don’t spend too much time thinking about each word. Rather, make your ratings based on your first\nand immediate reaction as you read each word. \n\nClick the screen to continue.',
    font='Arial',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "valence_instruction"
valence_instructionClock = core.Clock()
InstructValenceText = visual.TextStim(win=win, name='InstructValenceText',
    text='This Is The Scale For Valence Ratings\n\nA 1 On The Scale Equals To Very Low Valence (Unhappy)\n\nA 5 On The Scale Equals To Neutral\n\nA 9 On The Scale Equals To Very High Valence (Happy)\n\nYou select a number on the scale using your keyboards keys: 1-9\n\nClick On The Screen To Continue',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Valence = visual.ImageStim(
    win=win,
    name='Valence', 
    image='Valence.png', mask=None,
    ori=0, pos=(0, 0.3), size=(0.50, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "arousal_instruction"
arousal_instructionClock = core.Clock()
InstructArousalText = visual.TextStim(win=win, name='InstructArousalText',
    text='This Is The Scale For Arousal Ratings\n\nA 1 On The Scale Equals To Very Low Arousal (Calm)\n\nA 5 On The Scale Equals To Neutral\n\nA 9 On The Scale Equals To Very High Arousal (Excited)\n\nYou select a number on the scale using your keyboards keys: 1-9\n\nClick On The Screen To Continue',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Arousal = visual.ImageStim(
    win=win,
    name='Arousal', 
    image='Arousal.png', mask=None,
    ori=0, pos=(0, 0.3), size=(0.50, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "Arousal_2"
Arousal_2Clock = core.Clock()
WordPresentation = visual.TextStim(win=win, name='WordPresentation',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ArousalGuide = visual.ImageStim(
    win=win,
    name='ArousalGuide', 
    image='Arousal.png', mask=None,
    ori=0, pos=(0, .25), size=(0.80, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Arousal\n1 = Calm, 9 = Excited',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
A_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Valence_2"
Valence_2Clock = core.Clock()
WordPresentation2 = visual.TextStim(win=win, name='WordPresentation2',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.09, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ValenceImage = visual.ImageStim(
    win=win,
    name='ValenceImage', 
    image='Valence.png', mask=None,
    ori=0, pos=(0, .25), size=(0.8, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Valence\n1 = Unhappy, 9 = Happy',
    font='Arial',
    pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
GoodbyeText = visual.TextStim(win=win, name='GoodbyeText',
    text='Thank You For Participating \nIn This Survey Part Of The Experiment!\n\nIt Has Been A PleasureTo Have You On Board!\n\nTake Care!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro_To_Click"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
gotValidClick = False  # until a click is received
# keep track of which components have finished
Intro_To_ClickComponents = [text, mouse_4]
for thisComponent in Intro_To_ClickComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro_To_ClickClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Intro_To_Click"-------
while continueRoutine:
    # get current time
    t = Intro_To_ClickClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro_To_ClickClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro_To_ClickComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro_To_Click"-------
for thisComponent in Intro_To_ClickComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
# the Routine "Intro_To_Click" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
introductionComponents = [introText, mouse]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introText* updates
    if introText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introText.frameNStart = frameN  # exact frame index
        introText.tStart = t  # local t and not account for scr refresh
        introText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introText, 'tStartRefresh')  # time at next scr refresh
        introText.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introText.started', introText.tStartRefresh)
thisExp.addData('introText.stopped', introText.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "valence_instruction"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
gotValidClick = False  # until a click is received
# keep track of which components have finished
valence_instructionComponents = [InstructValenceText, Valence, mouse_2]
for thisComponent in valence_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
valence_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "valence_instruction"-------
while continueRoutine:
    # get current time
    t = valence_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=valence_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructValenceText* updates
    if InstructValenceText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructValenceText.frameNStart = frameN  # exact frame index
        InstructValenceText.tStart = t  # local t and not account for scr refresh
        InstructValenceText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructValenceText, 'tStartRefresh')  # time at next scr refresh
        InstructValenceText.setAutoDraw(True)
    
    # *Valence* updates
    if Valence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Valence.frameNStart = frameN  # exact frame index
        Valence.tStart = t  # local t and not account for scr refresh
        Valence.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Valence, 'tStartRefresh')  # time at next scr refresh
        Valence.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in valence_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "valence_instruction"-------
for thisComponent in valence_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructValenceText.started', InstructValenceText.tStartRefresh)
thisExp.addData('InstructValenceText.stopped', InstructValenceText.tStopRefresh)
thisExp.addData('Valence.started', Valence.tStartRefresh)
thisExp.addData('Valence.stopped', Valence.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
# the Routine "valence_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "arousal_instruction"-------
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
arousal_instructionComponents = [InstructArousalText, Arousal, mouse_3]
for thisComponent in arousal_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
arousal_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "arousal_instruction"-------
while continueRoutine:
    # get current time
    t = arousal_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=arousal_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructArousalText* updates
    if InstructArousalText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructArousalText.frameNStart = frameN  # exact frame index
        InstructArousalText.tStart = t  # local t and not account for scr refresh
        InstructArousalText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructArousalText, 'tStartRefresh')  # time at next scr refresh
        InstructArousalText.setAutoDraw(True)
    
    # *Arousal* updates
    if Arousal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Arousal.frameNStart = frameN  # exact frame index
        Arousal.tStart = t  # local t and not account for scr refresh
        Arousal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Arousal, 'tStartRefresh')  # time at next scr refresh
        Arousal.setAutoDraw(True)
    # *mouse_3* updates
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in arousal_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "arousal_instruction"-------
for thisComponent in arousal_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructArousalText.started', InstructArousalText.tStartRefresh)
thisExp.addData('InstructArousalText.stopped', InstructArousalText.tStopRefresh)
thisExp.addData('Arousal.started', Arousal.tStartRefresh)
thisExp.addData('Arousal.stopped', Arousal.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
# the Routine "arousal_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Workbook2.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Arousal_2"-------
    # update component parameters for each repeat
    WordPresentation.setText(word)
    A_key_resp.keys = []
    A_key_resp.rt = []
    # keep track of which components have finished
    Arousal_2Components = [WordPresentation, ArousalGuide, text_3, A_key_resp]
    for thisComponent in Arousal_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Arousal_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Arousal_2"-------
    while continueRoutine:
        # get current time
        t = Arousal_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Arousal_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WordPresentation* updates
        if WordPresentation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WordPresentation.frameNStart = frameN  # exact frame index
            WordPresentation.tStart = t  # local t and not account for scr refresh
            WordPresentation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WordPresentation, 'tStartRefresh')  # time at next scr refresh
            WordPresentation.setAutoDraw(True)
        
        # *ArousalGuide* updates
        if ArousalGuide.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ArousalGuide.frameNStart = frameN  # exact frame index
            ArousalGuide.tStart = t  # local t and not account for scr refresh
            ArousalGuide.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ArousalGuide, 'tStartRefresh')  # time at next scr refresh
            ArousalGuide.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *A_key_resp* updates
        if A_key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A_key_resp.frameNStart = frameN  # exact frame index
            A_key_resp.tStart = t  # local t and not account for scr refresh
            A_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_key_resp, 'tStartRefresh')  # time at next scr refresh
            A_key_resp.status = STARTED
            # keyboard checking is just starting
            A_key_resp.clock.reset()  # now t=0
            A_key_resp.clearEvents(eventType='keyboard')
        if A_key_resp.status == STARTED:
            theseKeys = A_key_resp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                A_key_resp.keys = theseKeys.name  # just the last key pressed
                A_key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Arousal_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Arousal_2"-------
    for thisComponent in Arousal_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('WordPresentation.started', WordPresentation.tStartRefresh)
    trials.addData('WordPresentation.stopped', WordPresentation.tStopRefresh)
    trials.addData('ArousalGuide.started', ArousalGuide.tStartRefresh)
    trials.addData('ArousalGuide.stopped', ArousalGuide.tStopRefresh)
    trials.addData('text_3.started', text_3.tStartRefresh)
    trials.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if A_key_resp.keys in ['', [], None]:  # No response was made
        A_key_resp.keys = None
    trials.addData('A_key_resp.keys',A_key_resp.keys)
    if A_key_resp.keys != None:  # we had a response
        trials.addData('A_key_resp.rt', A_key_resp.rt)
    trials.addData('A_key_resp.started', A_key_resp.tStart)
    trials.addData('A_key_resp.stopped', A_key_resp.tStop)
    # the Routine "Arousal_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Valence_2"-------
    # update component parameters for each repeat
    WordPresentation2.setText(word)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    Valence_2Components = [WordPresentation2, ValenceImage, text_2, key_resp]
    for thisComponent in Valence_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Valence_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Valence_2"-------
    while continueRoutine:
        # get current time
        t = Valence_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Valence_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WordPresentation2* updates
        if WordPresentation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            WordPresentation2.frameNStart = frameN  # exact frame index
            WordPresentation2.tStart = t  # local t and not account for scr refresh
            WordPresentation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(WordPresentation2, 'tStartRefresh')  # time at next scr refresh
            WordPresentation2.setAutoDraw(True)
        
        # *ValenceImage* updates
        if ValenceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ValenceImage.frameNStart = frameN  # exact frame index
            ValenceImage.tStart = t  # local t and not account for scr refresh
            ValenceImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ValenceImage, 'tStartRefresh')  # time at next scr refresh
            ValenceImage.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Valence_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Valence_2"-------
    for thisComponent in Valence_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('WordPresentation2.started', WordPresentation2.tStartRefresh)
    trials.addData('WordPresentation2.stopped', WordPresentation2.tStopRefresh)
    trials.addData('ValenceImage.started', ValenceImage.tStartRefresh)
    trials.addData('ValenceImage.stopped', ValenceImage.tStopRefresh)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStart)
    trials.addData('key_resp.stopped', key_resp.tStop)
    # the Routine "Valence_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "goodbye"-------
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [GoodbyeText]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GoodbyeText* updates
    if GoodbyeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GoodbyeText.frameNStart = frameN  # exact frame index
        GoodbyeText.tStart = t  # local t and not account for scr refresh
        GoodbyeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GoodbyeText, 'tStartRefresh')  # time at next scr refresh
        GoodbyeText.setAutoDraw(True)
    if GoodbyeText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GoodbyeText.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            GoodbyeText.tStop = t  # not accounting for scr refresh
            GoodbyeText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(GoodbyeText, 'tStopRefresh')  # time at next scr refresh
            GoodbyeText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('GoodbyeText.started', GoodbyeText.tStartRefresh)
thisExp.addData('GoodbyeText.stopped', GoodbyeText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
