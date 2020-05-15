#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:15:56 2019

@author: au632191
"""

def sequence (parameters, studyList, distractorListr):
    '''
    parameters
    __________
    parameters: dictionary
    studyList: list of pandas sequence
    distractorList: list of pandas sequence
    
    Notes
    ____
    * 50 trials
    '''
    
    #Create task_df that we are going to feed later
    
    #security chack
    if len(studylist) != len(distractorList):
        raise ValueError ('''Study list and distractor should have the same length''')
        
    
    if len(studyList)%2)!=0:
        raise ValueError ('''Study list should have an even number''')
        
    sequence _df = pd.DataFrame({'Studied': studyList, 'Distractor': distractorList})
    
    #Create a randomized position column
    
   positionLength = int(len(studyList)/2)

a=np.hstack((np.zeros(positionLength), np.ones(positionLength)))
np.random.shuffle(a)
sequence_df['Position']=a


for index, row in sequence_df.iterrows():
    if row['Position'] ==0:
    trial(parameters, word1=row['Studied'], word2=row['Distractor'])
elif:row['Position'] ==1:
    trial(parameters, word1=row['Distractor'], word2=row['Studied])
else:
    raise valueError ('incorrecr value in Position column)
    
    





parameters = getParameters()
studyList = words_sdf[0]
distractorList = words_sdf[1]