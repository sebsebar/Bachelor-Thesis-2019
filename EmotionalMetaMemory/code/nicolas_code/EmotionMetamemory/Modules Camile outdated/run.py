#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:54:46 2019

@author: au632191
"""

#Run task
#importing the functions that are saved separately 

from learningParameters import learning
from getParameters import getParameters
from trialFunction import trial

# from task import * (Nicolas)
parameters = getParameters()
words_df = pd.read.excel('wordLists.xls', header=None)


task_df = words_df [[0,1]]

#Create task_df that we are going to feed later

a=np.hstack((np.zeros(25), np.ones(25)))
np.random.shuffle(a)
task_df['Position']= a #adding a column of zeros and ones randomizing
task_df.columns = ['Studied', 'Distractor', 'Position']



np.random.choice(a=[True, False], size=50).sum() # ************************************

listStudied = words_df[0]
# listDistractor = words_df[1]
learning(parameters, listStudied)
trial(parameters, 'x', 'y')
                     