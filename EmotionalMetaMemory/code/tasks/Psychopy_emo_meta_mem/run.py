import os
import serial
import pandas as pd
from task import sequence, training
from parameters import getParameters
from recording import Oximeter
from psychopy import visual, gui, monitors

path = os.getcwd()

# Wrapper function
##################

# Get parameters
parameters = getParameters()

# Create a GUI and store subject ID
g = gui.Dlg()
g.addField("Subject Number:")
g.addField("Subject ID:")
g.show()
nSub = g.data[0]
subID = g.data[1]

# Open window
mon = monitors.Monitor('testMonitor', width=60, distance=57)
win = visual.Window(size=(1920, 1080), fullscr=True, units='height', monitor=mon)

# Create the recording instance
ser = serial.Serial('COM4',
                    baudrate=9600,
                    timeout=1/75,
                    stopbits=1,
                    parity=serial.PARITY_NONE)

# Run training sequence
training_df = pd.read_csv(path + '/Material/Training.txt', sep='\t')
training(parameters, path, win, None, training_df, subID=subID, nTrials=10)

# Create Oximeter instance
oximeter = Oximeter(serial=ser, sample=75)

# Run the entire test sequence
sequence(parameters, subNumber=int(nSub), subID=subID, simulate=False, win=win,
         oxi=oximeter, path=path)
win.close()
