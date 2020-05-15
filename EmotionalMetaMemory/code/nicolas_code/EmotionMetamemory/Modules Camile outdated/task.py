import pandas as pd
import numpy as np
from psychopy import visual, core, event


def getParameters():
    """Define the parameters

    Attributes
    ----------
    winSize : list

    monitor : str

    allowedKeys : list of str

    learningTime: list
        The different exposition time of the list (seconds).
    confScale : int
        How many points on the rating scale.
    confLimit: int
        Time limit for confidence responding (seconds). Default is `4`.
    choiceLimit: int
        Time limit for choice responding (seconds). Default is `4`.

    """
    parameters = {'winSize': [800, 800],
                  'monitor': 'testMonitor',
                  'allowedKeys': ['right', 'left'],
                  'learningTime': [30, 60, 90],
                  'confScale': 4,
                  'confLimit': 4,
                  'choiceLimit': 4}

    parameters['Instructions'] = """You will be presented with 50 words on the screen.
    You will be given a variable time to memorize as many of them as you can.
    After the time is up, you will be tested on which words were on this list.
    Do your best to remember as many of them as you can. Good luck!
    Please press any key to continue. The word list will be shown on the screen
    and your time will start the moment you press any key. Press the space bar
    when you are ready"""

    parameters['Wait'] = """Please press the space bar
                        when you are ready to learn the new list"""

    parameters['Conditions'] = {'1': ['High', 'High'], '2': ['High', 'Low'],
                                '3': ['Low', 'High'], '4': ['Low', 'Low']}

    parameters['Confidence'] = """How sure are you?"""

    return parameters


def instructions(parameters, win):
    """Wait for space bar and show the instruction.

    """
    # Ask the participant to press 'Space' (default) to start the task
    messageStart = visual.TextStim(win, text=parameters['Wait'])
    messageStart.autoDraw = True  # Show instructions
    win.flip()
    event.waitKeys(keyList='space')
    messageStart.autoDraw = False  # Hide instructions
    win.update()

    # Show the instructions
    messageStart = visual.TextStim(win, text=parameters['Instructions'])
    messageStart.autoDraw = True  # Show instructions
    win.flip()
    event.waitKeys(keyList='space')
    messageStart.autoDraw = False  # Hide instructions
    win.update()


def learning(listStudied, timeLearning, win=None):
    """Learning phases.

    listStudied: list
        List of 50 strings.

    timeLearning: int
        Number of seconds the list is displayed.

    win: psychopy Window. Default is None
        The window in which displaying.
    """
    # Security check
    if len(listStudied) != 50:
        raise ValueError('Incorrect length of study list')

    # Create ranges to present 5 * 10 words
    x_range = np.arange(-0.5, 0.5, 0.2)
    y_range = np.arange(-0.5, 0.5, 0.1)

    # Show the list in the screen
    i = 0
    for x in x_range:
        for y in y_range:
            word = visual.TextStim(win, text=listStudied[i],
                                   height=0.05, pos=(x, y))
            word.draw()
            i += 1

    # Security check
    if i != 50:
        raise ValueError("""Error in list presentation,
                            should show exactly 50 words""")
    # Update window
    win.update()

    # Wait for an amount of time depending on the condition
    core.wait(timeLearning)

    # Remove words from screen
    win.flip()


def trial(parameters, word1, word2, shift, win):
    """Trial function.

    Parameters
    ----------
    parameters : dictionnary
        Contain the task parameters.
    word1, word2 : str
        Testing words.
    shift : boolean or int

    Notes
    -----

    References
    ----------

    Examples
    --------


    """
    fixation = visual.GratingStim(win=win, mask='cross', size=0.1,
                                  pos=[0, 0], sf=0, rgb=-1)

    # Fixation cross
    fixation.draw()
    win.update()
    core.wait(1.0)

    # Draw two words
    if shift:
        word1 = visual.TextStim(win, text=word1, pos=(-0.5, 0), units='norm')
        word2 = visual.TextStim(win, text=word2, pos=(0.5, 0), units='norm')
        expectedCorrect = 'left'
    else:
        word1 = visual.TextStim(win, text=word2, pos=(0.5, 0), units='norm')
        word2 = visual.TextStim(win, text=word1, pos=(-0.5, 0), units='norm')
        expectedCorrect = 'right'

    word1.draw()
    word2.draw()

    win.update()
    clock = core.Clock()

    # Get subject answer
    responseKey = event.waitKeys(timeStamped=clock, maxWait=2,
                                 keyList=parameters['allowedKeys'])

    if responseKey is None:
        warning = visual.TextStim(win, text='Too late')
        warning.draw()
        win.update()
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

    # Record participant confidence (+/-)
    ratingScale = visual.RatingScale(win)
    ratingScale.draw()
    win.flip()
    confidence = ratingScale.getRating()
    confidence_rt = ratingScale.getRT()

    return accuracy, keyPressed, rt, confidence, confidence_rt


def sequence(parameters, simulate=False, nMax=None, nSub=None, win=None):
    """Run the entire task sequence.

    Parameters
    ----------
    parameters: dictionnary

    studyList : list or Pandas sequence

    distractorList : list or Pandas sequence

    Notes
    -----
        """
    result_df = pd.DataFrame([])

    # Get subject number
    subjectNumber = 6

    # Generate blocks orders
    arousing = np.array([1, 3, 1, 3, 1, 3])
    nonarounsing = np.array([2, 4, 2, 4, 2, 4])
    np.random.shuffle(arousing)
    np.random.shuffle(nonarounsing)

    if (subjectNumber % 2) == 0:

        blockOrder = []
        for i in range(6):
            blockOrder.append(arousing[i])
            blockOrder.append(nonarounsing[i])

    elif (subjectNumber % 2) == 0:

        blockOrder = []
        for i in range(6):
            blockOrder.append(nonarounsing[i])
            blockOrder.append(arousing[i])

    # Generate learning times
    timeList = [[30, 60, 90], [30, 90, 60], [60, 30, 90],
                [60, 90, 30], [90, 30, 60], [90, 60, 30]]
    nTime = timeList[(subjectNumber % 6)]

    # Generate Learning/Distractors lists
    if (subjectNumber % 2) == 0:
        learningList, distractorList = [1, 3, 5], [2, 4, 6]
    else:
        learningList, distractorList = [2, 4, 6], [1, 3, 5]

    # Read dataframes
    df_1 = pd.read_csv('1_WordList_ValHighAroHigh.csv', dtype={'List': 'int'})
    df_2 = pd.read_csv('2_WordList_ValHighAroLow.csv', dtype={'List': 'int'})
    df_3 = pd.read_csv('3_WordList_ValLowAroHigh.csv', dtype={'List': 'int'})
    df_4 = pd.read_csv('4_WordList_ValLowAroLow.csv', dtype={'List': 'int'})
    words_df = {'1': df_1, '2': df_2, '3': df_3, '4': df_4}

    # Run the sequence
    for nBlock, block in enumerate(blockOrder):

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
            learning(listStudied=list(learning_df.Word),
                     timeLearning=timeLearning, win=win)

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
                accuracy, keyPressed, rt, confidence, confidence_rt = \
                    trial(parameters, word1, word2,
                          shift=wordPosition[i], win=win)

            # Update the result Dataframe
            result_df = result_df.append({
                      'RT': rt,
                      'Accuracy': accuracy,
                      'LearningTime': timeLearning,
                      'nBlock': nBlock,
                      'Confidence': confidence,
                      'Confidence_RT': confidence_rt,
                      'TrialNumber': i,
                      'Valence': parameters['Conditions'][str(block)][0],
                      'Arousal': parameters['Conditions'][str(block)][1],
                      'KeyPressed': keyPressed}, ignore_index=True)
            if nMax:
                if i < nMax:
                    break

        result_df.to_csv('Results/Subject_' + str(nSub) + '.txt')


# Run
#####

# Get parameters
parameters = getParameters()

# Open window
win = visual.Window(parameters['winSize'],  monitor=parameters['monitor'])

# Show instruction
instructions(parameters, win)

sequence(parameters, simulate=False, nMax=5, nSub=1, win=win)

##########
# Analyzes
##########

final_df = pd.DataFrame([])

for nSub in range(30):

    subj_df = pd.read_csv('Results/Subject_' + str(nSub) + '.txt')

    subj_df = subj_df.groupby(by=['Arousal', 'Valence'], as_index=False).mean()

    subj_df['Subject'] = nSub

    final_df = final_df.append(subj_df)


import seaborn as sns
import pingouin as pg
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
sns.violinplot(data=final_df, x='Arousal', y='RT', hue='Valence')
plt.savefig('Figures/firstplot.png', dpi=300)
pg.rm_anova(data=final_df, dv='RT', within=['Arousal', 'Valence'], subject='Subject')
