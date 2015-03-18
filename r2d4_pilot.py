#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'testing_r2d4'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

#Add context
context = visual.Rect(win, width=1, height=1, autoDraw = True, lineColor='white', lineWidth = 6)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'Remember, choose the key corresponding to the number that you see displayed on the screen:\n2 -- index\n3 -- middle\n4 -- ring\n5 -- pinky',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Target = visual.TextStim(win=win, ori=0, name='Target',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial_2"
trial_2Clock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instrText)
InstructionsComponents.append(key_resp_2)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=2, method='random',
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)

    # set up handler to look after randomisation of conditions etc
    sequences = data.TrialHandler(nReps=1, method='sequential',
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(u'stimuli.csv'),
        seed=None, name='sequences')
    thisExp.addLoop(sequences)  # add the loop to the experiment
    thisSequence = sequences.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSequence.rgb)
    if thisSequence != None:
        for paramName in thisSequence.keys():
            exec(paramName + '= thisSequence.' + paramName)

    for thisSequence in sequences:
        currentLoop = sequences
        # abbreviate parameter names if possible (e.g. rgb = thisSequence.rgb)
        if thisSequence != None:
            for paramName in thisSequence.keys():
                exec(paramName + '= thisSequence.' + paramName)

        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        Target.setText(stimulus)
        response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        response.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(Target)
        trialComponents.append(response)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *Target* updates
            if t >= 0.5 and Target.status == NOT_STARTED:
                # keep track of start time/frame for later
                Target.tStart = t  # underestimates by a little under one frame
                Target.frameNStart = frameN  # exact frame index
                Target.setAutoDraw(True)
            if Target.status == STARTED and t >= (0.5 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                Target.setAutoDraw(False)

            # *response* updates
            if t >= 0.5 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t  # underestimates by a little under one frame
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                response.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if response.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                response.status = STOPPED
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['2', '3', '4', '5'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    response.keys = theseKeys[-1]  # just the last key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(cor_ans)) or (response.keys == cor_ans):
                        response.corr = 1
                    else:
                        response.corr = 0
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
           response.keys=None
           # was no response the correct answer?!
           if str(cor_ans).lower() == 'none': response.corr = 1  # correct non-response
           else: response.corr = 0  # failed to respond (incorrectly)
        # store data for sequences (TrialHandler)
        sequences.addData('response.keys',response.keys)
        sequences.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            sequences.addData('response.rt', response.rt)
        thisExp.nextEntry()

    # completed 1 repeats of 'sequences'


    # set up handler to look after randomisation of conditions etc
    remap = data.TrialHandler(nReps=1, method='sequential',
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(u'image_stim.csv'),
        seed=None, name='remap')
    thisExp.addLoop(remap)  # add the loop to the experiment
    thisRemap = remap.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisRemap.rgb)
    if thisRemap != None:
        for paramName in thisRemap.keys():
            exec(paramName + '= thisRemap.' + paramName)

    for thisRemap in remap:
        currentLoop = remap
        # abbreviate parameter names if possible (e.g. rgb = thisRemap.rgb)
        if thisRemap != None:
            for paramName in thisRemap.keys():
                exec(paramName + '= thisRemap.' + paramName)

        #------Prepare to start Routine "trial_2"-------
        t = 0
        trial_2Clock.reset()  # clock
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        image.setImage(image_id)
        key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_3.status = NOT_STARTED
        # keep track of which components have finished
        trial_2Components = []
        trial_2Components.append(image)
        trial_2Components.append(key_resp_3)
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "trial_2"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *image* updates
            if t >= .5 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            if image.status == STARTED and t >= (.5 + (.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                image.setAutoDraw(False)

            # *key_resp_3* updates
            if t >= .5 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t  # underestimates by a little under one frame
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                key_resp_3.clock.reset()  # now t=0
            if key_resp_3.status == STARTED and t >= (.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_3.status = STOPPED
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=['2', '3', '4', '5'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_3.keys == str(cor_ans_img)) or (key_resp_3.keys == cor_ans_img):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial_2"-------
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
           key_resp_3.keys=None
           # was no response the correct answer?!
           if str(cor_ans_img).lower() == 'none': key_resp_3.corr = 1  # correct non-response
           else: key_resp_3.corr = 0  # failed to respond (incorrectly)
        # store data for remap (TrialHandler)
        remap.addData('key_resp_3.keys',key_resp_3.keys)
        remap.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            remap.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.nextEntry()

    # completed 1 repeats of 'remap'

    thisExp.nextEntry()

# completed 2 repeats of 'blocks'

win.close()
core.quit()
