# Author: Nicolas Legrand <nicolas.legrand@cfin.au.dk>

import os
import pandas as pd
import numpy as np
from psychopy import visual, core, event


def instructions(parameters, win, show_intructions=False):
    """Wait for space bar and show the instruction.

    Parameters
    ----------
    parameters : dict
        Dictionnary containing task parameters.
    win : psychopy window
        Where to display the task.
    show_intructions : boolean, default is `True`
        Show the instruction at the beggining of the task.
    """
    if show_intructions is True:
        # Show the first instruction
        messageStart = visual.TextStim(win, text=parameters['instruction1'],
                                       height=0.03, pos=(0.0, 0.3),
                                       units='height')
        messageStart.autoDraw = True
        # Show the second instruction
        messageStart2 = visual.TextStim(win, text=parameters['instruction2'],
                                        height=0.03, pos=(0.0, 0.0),
                                        units='height')
        messageStart2.autoDraw = True
        # Show the second instruction
        messageStart3 = visual.TextStim(win, text=parameters['instruction3'],
                                        height=0.03, pos=(0.0, -0.3),
                                        units='height')
        messageStart3.autoDraw = True
        win.flip()

        # Wait for space bar and flip screen
        event.waitKeys(keyList='space')
        messageStart.autoDraw = False
        messageStart2.autoDraw = False
        messageStart3.autoDraw = False

    # Ask the participant to press 'Space' (default) to start the task
    messageStart = visual.TextStim(win, text=parameters['wait'], height=0.03)
    messageStart.autoDraw = True
    win.flip()
    event.waitKeys(keyList='space')
    messageStart.autoDraw = False
    win.flip()


def learning(listStudied, timeLearning, win=None, oxi=None):
    """Learning phases.

    Parameters
    ----------
    listStudied : list
        List of 50 strings.
    timeLearning : int
        Number of seconds the list is displayed.
    win : psychopy Window. Default is None
        The window in which displaying.
    oxi : oximeter instance
        If provided, record using Oximeter.

    Returns
    -------
    oxi : instance of Oximeter
        The recording device storing recording.
    """
    # Security check
    if len(listStudied) != 50:
        raise ValueError('Incorrect length of study list')

    # Create ranges to present 5 * 10 words
    x = 0.5 * (win.size[0] / win.size[1])
    x_margin = 1.5*x/5
    y_margin = 0.5/5
    x_range = np.linspace(-x+x_margin, x-x_margin, 5)
    y_range = np.linspace(-0.5+y_margin, 0.5-y_margin, 10)

    # Show the list in the screen
    i = 0
    for x in x_range:
        for y in y_range:
            word = visual.TextStim(win, text=listStudied[i], units='height',
                                   height=0.05, pos=(x, y))
            word.draw()
            i += 1

    # Security check
    if i != 50:
        raise ValueError("""Error in list presentation,
                            should show exactly 50 words""")
    # Update window
    win.update()
    if oxi is not None:
        oxi.readInWaiting()
        oxi.triggers[-1] = 4

        # Wait for an amount of time depending on the condition
        oxi.read(nSeconds=timeLearning)
    else:
        core.wait(timeLearning)

    # Remove words from screen
    win.flip()
    if oxi is not None:
        oxi.triggers[-1] = 4

    return oxi


def training(parameters, path, win, oxi, training_df, subID, nTrials=10,
             learningTime=60):
    """Training sequence
    Parameters
    ----------
    training_df : pandas DataFrame
        The practice DataFrame.
    nTrials : int, default is `10`
        The number of practice trials.
    """
    # calling the parameters and instructions for the practice trials
    instructions(parameters, win, show_intructions=True)

    learning(list(training_df['Study']), learningTime, win, oxi=None)

    trainingPosition = np.hstack((np.zeros(int(nTrials/2)),
                                  np.ones(int(nTrials/2))))
    np.random.seed(38)
    np.random.shuffle(trainingPosition)

    trainResult_df = pd.DataFrame([])

    for i in range(nTrials):
        StudyPracticeWord = training_df['Study'].iloc[i]
        DistractorPracticeWord = training_df['Distractor'].iloc[i]

        expectedCorrect, accuracy, keyPressed, rt, confidence, \
            confidence_rt, oxi, markerStart, word1, word2 = \
            trial(parameters, StudyPracticeWord, DistractorPracticeWord,
                  trainingPosition[i], win, oxi=None, confidence=True)

        # Update the result Dataframe
        trainResult_df = trainResult_df.append({
                'RT': rt,
                'Expected': expectedCorrect,
                'Accuracy': accuracy,
                'LearningTime': learningTime,
                'nBlock': 'TrainingBlock',
                'Confidence': confidence,
                'Confidence_RT': confidence_rt,
                'TrialNumber': i,
                'MarkerStart': markerStart,
                'KeyPressed': keyPressed,
                'LeftWord': word1,
                'RightWord': word2}, ignore_index=True)

    trainResult_df.to_csv(
        path + '/Results/Traing_Subject_' + str(subID) + '.txt')


def trial(parameters, word1, word2, shift, win, oxi=None, confidence=True):
    """Trial function.

    Parameters
    ----------
    parameters : dictionnary
        Contain the task parameters.
    word1, word2 : str
        If position is not shifted, word1 is target and word2 is distractor.
    shift : boolean or int
        Shift the position of words horizontally.
    win : psychopy window
        Where to draw the task.
    oxi : Instance of Oximeter
        Where recording devise.
    confidence : boolean, default is `True`
        Measure the confidence a the end of the trial.

    Returns
    -------
    expectedCorrect : str
        The expected position of the targeted word.
    accuracy : boolean or string, default will be `Nan`
        Is the answer provided `True` or `False`.
    keyPressed : str
        The key pressend by the participant, among `parameters['allowedKeys']`
    rt : float or str, default will be `Nan`
        The response time for the decision.
    confidence : int or str, default will be `Nan`
        The level of confidence, between range specified in
        `parameters['confScale']`
    confidence_rt : float or str, default will be `Nan`
        The response time for the rating scale.
    oxi : instance of Oximeter
        The recording device storing recording.
    markerStart : int
        Where in the rating scale did the marker start.
    word1, word2 : str
        Testing words.

    Notes
    -----
    If no answer is provided for the decision after the time limit, the rating
    scale will not be presented.
    """
    # Set default output values
    confidence, confidence_rt, accuracy, markerStart = \
        'Nan', 'Nan', 'NaN', 'NaN'

    fixation = visual.GratingStim(win=win, mask='cross', size=0.1,
                                  pos=[0, 0], sf=0, rgb=-1)

    # Fixation cross
    fixation.draw()
    win.update()
    if oxi is not None:
        oxi.readInWaiting()
        oxi.triggers[-1] = 2
    core.wait(parameters['fixTime'])

    # Shift if requsted
    if shift == 0:
        expectedCorrect = 'left'
    elif shift == 1:
        word1, word2 = word2, word1
        expectedCorrect = 'right'
    else:
        raise ValueError('Invalid position')

    # Draw two words
    word1Text = visual.TextStim(win, text=word1, pos=(-0.5, 0), units='norm',
                                height=0.2)
    word2Text = visual.TextStim(win, text=word2, pos=(0.5, 0), units='norm',
                                height=0.2)
    word1Text.autoDraw = False
    word2Text.autoDraw = False

    # Show words for min 1.5s and max 3s
    clock, responseKey = core.Clock(), []
    while clock.getTime() < parameters['decisionTimeMax']:

        # Get subject answer
        if not responseKey:
            responseKey = event.getKeys(timeStamped=clock,
                                        keyList=parameters['allowedKeys'])
        if responseKey:
            # Change word color if response is provided
            if responseKey[0][0] == 'left':
                word1Text.color = (0, 0, 1)
            elif responseKey[0][0] == 'right':
                word2Text.color = (0, 0, 1)
            if clock.getTime() > parameters['decisionTimeMin']:
                break

        word1Text.draw()
        word2Text.draw()
        win.flip()

    # Reset screen
    win.flip()

    # Store available ox recording
    if oxi is not None:
        oxi.readInWaiting()
        oxi.triggers[-1] = 3

    # Check if response was provided
    if not responseKey:
        warning = visual.TextStim(win, text='Too late', units='norm',
                                  height=0.2)
        warning.draw()
        win.flip()
        core.wait(0.5)
        rt, keyPressed = 'Nan', 'NaN'
    else:
        keyPressed = responseKey[0][0]
        rt = responseKey[0][1]

        # Accuracy of the subject's answer
        if keyPressed == expectedCorrect:
            accuracy = True
        else:
            accuracy = False

        if confidence:
            # Record participant confidence
            markerStart = np.random.choice(
                            np.arange(parameters['confScale'][0],
                                      parameters['confScale'][1]))
            ratingScale = visual.RatingScale(
                                     win,
                                     low=parameters['confScale'][0],
                                     high=parameters['confScale'][1],
                                     noMouse=True,
                                     labels=parameters['labelsRating'],
                                     acceptKeys='down',
                                     markerStart=markerStart)
            clock2 = core.Clock()
            while clock2.getTime() < parameters['maxRatingTime']:

                if not ratingScale.noResponse:
                    ratingScale.markerColor = (0, 0, 1)
                    if clock2.getTime() > parameters['minRatingTime']:
                        break
                ratingScale.draw()
                win.flip()

            if ratingScale.noResponse:
                print(clock2.getTime())
                warning = visual.TextStim(win, text='Too late')
                warning.draw()
                win.flip()
                core.wait(0.5)
            else:
                confidence = ratingScale.getRating()
                confidence_rt = ratingScale.getRT()

            if oxi is not None:
                oxi.readInWaiting()
                oxi.triggers[-1] = 4

    # Fixation cross
    fixation.draw()
    win.update()
    core.wait(parameters['iti'](low=1.75, high=2.25))

    return expectedCorrect, accuracy, keyPressed, rt, confidence, \
        confidence_rt, oxi, markerStart, word1, word2


def sequence(parameters, subNumber, subID=None, simulate=False, nMax=None,
             win=None, path=None, oxi=None):
    """Run the entire task sequence.

    Parameters
    ----------
    parameters : dictionnary
        Dictionnary containing task parameters.
    subNumber : int
        Subject number.
    subID : str or None, default is `None`
        Subject ID.
    simulate : boolean, default is `False`
        Simulate data based on random sampling.
    nMax : int or None, default is `None`
        If provided, limit the number or trials to nMax. To do used for testing
        purpose.
    win : psychopy Window. Default is None
        The window in which displaying.
    path : str or None, default is `None`
        Folder containing the task files and Result folder.
    oxi : Instance of Oximeter
        Where recording devise.

    Notes
    -----
    If recording, will store data at the end o0f each block. The final dataframe
    is saved as `result_df`.
    """
    if path is None:
        path = os.get_cwd()
    if oxi:
        oxi.setup()
    result_df = pd.DataFrame([])

    # Generate blocks orders
    arousing = np.array([1, 3, 1, 3, 1, 3])
    nonarounsing = np.array([2, 4, 2, 4, 2, 4])
    np.random.shuffle(arousing)
    np.random.shuffle(nonarounsing)

    if (subNumber % 2) == 0:

        blockOrder = []
        for i in range(6):
            blockOrder.append(arousing[i])
            blockOrder.append(nonarounsing[i])

    elif (subNumber % 2) != 0:

        blockOrder = []
        for i in range(6):
            blockOrder.append(nonarounsing[i])
            blockOrder.append(arousing[i])
    else:
        raise ValueError('Invalid subject number.')

    # Generate learning times
    timeList = [[30, 60, 90], [30, 90, 60], [60, 30, 90],
                [60, 90, 30], [90, 30, 60], [90, 60, 30]]
    nTime = timeList[(subNumber % 6)]

    # Generate Learning/Distractors lists
    if (subNumber % 2) == 0:
        learningList, distractorList = [1, 3, 5], [2, 4, 6]
    else:
        learningList, distractorList = [2, 4, 6], [1, 3, 5]

    # Read dataframes
    df_1 = pd.read_csv(path + '/Material/1_WordList_ValHighAroHigh.csv',
                       dtype={'List': 'int'})
    df_2 = pd.read_csv(path + '/Material/2_WordList_ValHighAroLow.csv',
                       dtype={'List': 'int'})
    df_3 = pd.read_csv(path + '/Material/3_WordList_ValLowAroHigh.csv',
                       dtype={'List': 'int'})
    df_4 = pd.read_csv(path + '/Material/4_WordList_ValLowAroLow.csv',
                       dtype={'List': 'int'})
    words_df = {'1': df_1, '2': df_2, '3': df_3, '4': df_4}

    # Run the sequence
    end = False
    for nBlock, block in enumerate(blockOrder):

        if end:
            break

        # Show instructions, break and wait for space press
        if nBlock == 0:
            instructions(parameters=parameters,
                         show_intructions=True, win=win)
        else:
            instructions(parameters=parameters, win=win)

        if oxi:
            oxi.setup()
            oxi.read(nSeconds=1)

        df = words_df[str(block)]

        # Security check
        if (len(df[df.List == learningList[0]]) !=
           len(df[df.List == distractorList[0]])):
            raise ValueError("""Inconsistent list size Learning/Distractor
                                    per condition""")

        # Find the index for learning and distractor
        # Check if both values are present in the List column
        if ((learningList[0] in df.List.unique()) &
                (distractorList[0] in df.List.unique())):
            indexLearning, indexDistractor = learningList[0], distractorList[0]
            timeLearning = nTime[0]

        # Check if both values are present in the List column
        elif ((learningList[1] in df.List.unique()) &
                (distractorList[1] in df.List.unique())):
            indexLearning, indexDistractor = learningList[1], distractorList[1]
            timeLearning = nTime[1]

        # Check if both values are present in the List column
        elif ((learningList[2] in df.List.unique()) &
                (distractorList[2] in df.List.unique())):
            indexLearning, indexDistractor = learningList[2], distractorList[2]
            timeLearning = nTime[2]
        else:
            raise ValueError('Invalid lists')

        # Use the index to select the learning and distractors words
        learning_df = df[df.List == indexLearning].reset_index()
        distractor_df = df[df.List == indexDistractor].reset_index()

        # Drop the row corresponding to learning list AND distractor list
        df = df[df.List != indexLearning]
        df = df[df.List != indexDistractor]
        words_df[str(block)] = df

        # Run the learning phase
        if not simulate:
            oxi = learning(listStudied=list(learning_df.Word),
                           timeLearning=timeLearning, win=win, oxi=oxi)

        # Run trials
        positionLength = int(len(learning_df)/2)
        wordPosition = np.hstack((np.zeros(positionLength),
                                  np.ones(positionLength)))
        np.random.shuffle(wordPosition)

        for i in range(len(learning_df)):

            word1 = learning_df.iloc[i].Word
            word2 = distractor_df.iloc[i].Word

            if simulate:
                mean = np.random.normal(2, 0.5, 1)[0]
                std = np.random.normal(2, 0.2, 1)[0]
                rt = np.random.normal(mean, std, 1)[0]
                accuracy = np.random.choice([True, False])
                keyPressed = np.random.choice(['left', 'right'])
                confidence = np.random.choice([1, 2, 3, 4, 5, 6])
                confidence_rt = np.random.normal(mean, std, 1)[0]
            else:
                expectedCorrect, accuracy, keyPressed, rt, confidence, \
                    confidence_rt, oxi, markerStart, word1, word2 = \
                    trial(parameters, word1, word2,
                          shift=wordPosition[i], win=win, oxi=oxi)

            # Update the result Dataframe
            result_df = result_df.append({
                      'RT': rt,
                      'Expected': expectedCorrect,
                      'Accuracy': accuracy,
                      'LearningTime': timeLearning,
                      'nBlock': nBlock,
                      'Confidence': confidence,
                      'Confidence_RT': confidence_rt,
                      'TrialNumber': i,
                      'MarkerStart': markerStart,
                      'Valence': parameters['Conditions'][str(block)][0],
                      'Arousal': parameters['Conditions'][str(block)][1],
                      'KeyPressed': keyPressed,
                      'LeftWord': word1,
                      'RightWord': word2}, ignore_index=True)

            # If nMax elapsed end the task here
            if nMax:
                if i >= nMax:
                    end = True
                    break

        # Save the result_df after each block
        result_df.to_csv(path + '/Results/Subject_' + str(subID) + '.txt')

        if oxi:
            np.save(path + '/Results/Subject_' + str(subID) + str(subNumber)
                    + str(nBlock) + '.npy',
                    [oxi.recording, oxi.triggers])

    return result_df
