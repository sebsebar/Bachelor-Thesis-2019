# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import numpy as np

def getParameters():
    """Define the parameters for the Emotion & Metamemory task.

    Attributes
    ----------
    allowedKeys : list of str
        Response keys, 'left', 'right'.
    learningTime: list
        The different exposition time of the list (seconds).
    confScale : list of int
        How many points on the rating scale. Define low and high numeric
        ratings [1, 6].
    decisionTimeMin:  int or float, default is `1.5`
        The maximum limit for choice responding (seconds).
    decisionTimeMax : int or float, default is `3`
        The minimum limit for choice responding (seconds).
    fixTime : float
        Length of the first fixation cross (seconds).
    iti : numpy random distribution
        The distribution used to generage the inter trial interval.
    ratingTimeMin : int or float, default is `1.5`
        The minimum limit for the rating scale.
    ratingTimeMax : int or float, default is `3`
        The maximum limit for the rating scale.
    wait : str
        Instruction text to present before each experimental block.
    Condition : dict
        Condition labels.
    instructions : str
        Text instruction presented at the beggining of the task.
    """
    parameters = {'allowedKeys': ['right', 'left'],
                  'learningTime': [30, 60, 90],
                  'confScale': [1, 7],
                  'labelsRating': ['Guess', 'Certain'],
                  'decisionTimeMin': 1.5,
                  'decisionTimeMax': 3,
                  'minRatingTime': 1.5,
                  'maxRatingTime': 3,
                  'fixTime': 0.25,
                  'iti': np.random.uniform,
                  'Conditions': {'1': ['High', 'High'], '2': ['High', 'Low'],
                                 '3': ['Low', 'High'], '4': ['Low', 'Low']}}

    parameters['instruction1'] = """You will be presented with 50 words on the screen. You will be given a variable time to memorize as many of them as you can. After the time is up, you will be tested on which words were on this list. Do your best to remember as many of them as you can."""
    parameters['instruction2'] = """The word list will now disappear from the screen and your time will start the moment you press any key you'll start getting presented with words from the list you've studied aswell as new ones. You should press the LEFT or RIGHT arrow key to indicate which of the two words YOU HAVE SEEN BEFORE on the studied list."""
    parameters['instruction3'] = """After this choice you will be presented with a confidence scale ranging from 1 (totally guessing) until 7 (totally certain). You select your confidence with the arrow keys (LEFT and RIGHT) and confirm it by pressing the DOWN arrow key. Press the space bar when you are ready start."""
    parameters['wait'] = """Please press the space bar when you are ready to learn the new list"""

    return parameters
