#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:35:04 2019

@author: au632191
"""


def getParameters():
    '''Define the parameters
    
    Parameters
    __________
    winSize:list
        
    monitor: str
        
    allowedKeys:list of str
        
    learningTime_: list
        The different exposition times of the word list (sec).
    ConfScale: int
    How many points you want your rating scale
    confLimit :int
    time limit for confidence responding(sec). Default is `4`
  choiceLimit:int
    time limit for choice responding(sec). Default is `4`
    
    
    
    
    
    
    '''
    
    parameters = {'winSize': [1000,1000],
                  'monitor': 'testMonitor',
                  'allowedKeys': ['left', 'right'],
                  'learningTime' [30l, 60, 90],
                  'confScale':4
                  'confLimit': 4,
                  'choiceLimit': 4}
                  
                  
                  
                  
                  
                  }
    
    return parameters






