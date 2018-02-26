#win = visual.Window([600,600])
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'checkerboard_block_easy'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/[%s]_[%s_%s]_%s' %(expInfo['date'],expInfo['participant'], expInfo['session'],expName )

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


# ##################################################################################################################################################################

time_period=1/8# 8 Hz
#flash_rate_time=1/8# 8 Hz
total_scan=1920#Qty
change_fix_flag_hard=0
param_fix_stim1=30 #Qty
total_time=total_scan*time_period #sec
dummy_trigger=0
LCM=1/time_period/4*2




# Create some handy timers
trialClock = core.Clock()
press1_count=0
trigger_count=0
time_stamp=0
press_any=0
param_fix_flag=0
dummy_trigger_flag=0
param=[]
contrast_flag=[]
trigger_time=100000000
this_time_frame_count_flag=100000000
time_frame_count=0
kk_old=-1
kk_old2=-1

#-------stimulus
block_scan=96
tmp_event2=[1]*(int( 0))# condition1: R high
tmp_event2.extend([2]*(int( 0)))# condition2: L high
tmp_event2.extend([3]*(int( 0)))# condition3: R low
tmp_event2.extend([4]*(int( 0)))# condition4: L low
tmp_event2.extend([5]*(int( 10)))# condition5: R+L high
tmp_event2.extend([6]*(int( 0)))# condition6: R+L low
tmp_event2.extend([7]*(int( 0)))# condition7: R+Lsmall high


tmp_event2=np.random.permutation(tmp_event2)

tmp_event=[]
i=0
for i in range(len(tmp_event2)):
    tmp_event.extend([0])
    tmp_event.extend([tmp_event2[i]])
    

param_event_series= [0]* (len(tmp_event))
contrast_flag_series=[0]* (len(tmp_event))

for i in range(len(tmp_event)):
    if tmp_event[i]==1:
        param_event_series[i]=1
        contrast_flag_series[i]=1
    if tmp_event[i]==2:
        param_event_series[i]=2
        contrast_flag_series[i]=1
    if tmp_event[i]==3:
        param_event_series[i]=1
        contrast_flag_series[i]=2
    if tmp_event[i]==4:
        param_event_series[i]=2
        contrast_flag_series[i]=2
    if tmp_event[i]==5:
        param_event_series[i]=3
        contrast_flag_series[i]=1
    if tmp_event[i]==6:
        param_event_series[i]=3
        contrast_flag_series[i]=2
    if tmp_event[i]==7:
        param_event_series[i]=4
        contrast_flag_series[i]=1




for i in range(len(param_event_series)):
    param.extend( [param_event_series[i]] * block_scan)#4=> 125ms*4=500ms(event stimlus : flip 4 times)


for i in range(len(param_event_series)):
    contrast_flag.extend( [contrast_flag_series[i]] * block_scan)

param.extend([0]* (total_scan-len(param)))
contrast_flag.extend([0]* (total_scan-len(contrast_flag)))
#print contrast_flag
#print param

#----------------------param_fix


tmp2=[1]*(int( param_fix_stim1))
tmp2.extend([0]*int( total_scan/16-param_fix_stim1))

tmp=np.random.permutation(tmp2)


i=0
param_fix=[]
while i<len(tmp):
    
    param_fix.extend( [tmp[i]]*2 )
    param_fix.extend( [0]*2 )
    param_fix.extend( [tmp[i]]*2 )
    param_fix.extend([0]*(16-6))
    i=i+1


fix_choose =["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","J","K","L"]

thisExp.addData('Note', param)
thisExp.nextEntry()
thisExp.addData('Note', contrast_flag)
thisExp.nextEntry()
thisExp.addData('Note', param_fix)
thisExp.nextEntry()
#print fix_choose
#print param
#print contrast_flag
#print param_fix_tmp
#print param_fix


# ##################################################################################################################################################################


# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


#make two wedges (in opposite contrast) and alternate them for flashing
wedgeRonC1 = visual.RadialStim(win, tex='sqrXsqr', color=1,size=2,
    visibleWedge=[15, 165], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeRoffC1 = visual.RadialStim(win, tex='sqrXsqr', color=-1,size=2,
    visibleWedge=[15, 165], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLonC1 = visual.RadialStim(win, tex='sqrXsqr', color=1,size=2,
    visibleWedge=[195, 345], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLoffC1 = visual.RadialStim(win, tex='sqrXsqr', color=-1,size=2,
    visibleWedge=[195, 345], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeRonC2 = visual.RadialStim(win, tex='sqrXsqr', color=0.1,size=2,
    visibleWedge=[15, 165], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeRoffC2 = visual.RadialStim(win, tex='sqrXsqr', color=-0.1,size=2,
    visibleWedge=[15, 165], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLonC2 = visual.RadialStim(win, tex='sqrXsqr', color=0.1,size=2,
    visibleWedge=[195, 345], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLoffC2 = visual.RadialStim(win, tex='sqrXsqr', color=-0.1,size=2,
    visibleWedge=[195, 345], radialCycles=6, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
    
    
    
wedgeRonC1s = visual.RadialStim(win, tex='sqrXsqr', color=1,size=1,
    visibleWedge=[15, 165], radialCycles=3, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeRoffC1s = visual.RadialStim(win, tex='sqrXsqr', color=-1,size=1,
    visibleWedge=[15, 165], radialCycles=3, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLonC1s = visual.RadialStim(win, tex='sqrXsqr', color=1,size=1,
    visibleWedge=[195, 345], radialCycles=3, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful
wedgeLoffC1s = visual.RadialStim(win, tex='sqrXsqr', color=-1,size=1,
    visibleWedge=[195, 345], radialCycles=3, angularCycles= 10, interpolate=False,ori=0,opacity=1,
    autoLog=False)#this stim changes too much for autologging to be useful

center_block = visual.Circle(win, radius=0.2, units='', lineWidth=0.5, lineColor=(0, 0, 0),
    lineColorSpace='rgb', fillColor=(0,0,0), fillColorSpace='rgb', edges=1024, closeShape=True, pos=(0, 0), size=0.25, ori=0.0, opacity=1.0,
    contrast=1.0, depth=0, interpolate=False, lineRGB=None, fillRGB=None, name=None,
    autoLog=None, autoDraw=False)
    
instruction = visual.TextStim(win=win, ori=0, name='instruction',
    text=u'',font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, bold=True,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)

End_instruction = visual.TextStim(win=win, ori=0, name='End_instruction',
    text=u'\u672c\u6b21\u5be6\u9a57\u7d50\u675f\uff0c\u4e0b\u4e00\u500b\u5be6\u9a57\u5373\u5c07\u958b\u59cb',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,bold=True,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)

fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'+',    font=u'Arial',
    pos=[0, 0.0075], height=0.15, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-4.0)
    
none_blank = visual.TextStim(win=win, ori=0, name='fixation',
    text=u'',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)
    
    
clock_disp = visual.TextStim(win=win, ori=0, name='clock_disp',
    text=u'-',    font=u'Arial',
    pos=[0.9, -0.9], height=0.1, wrapWidth=None,
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-4.0)
    
    
#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
kk=np.random.randint(3,20, size=1)
#routineTimer.add(40.000000)
# update component parameters for each repeat
keybrd_input = event.BuilderKeyResponse()  # create an object of type KeyResponse
keybrd_input.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(instruction)
trialComponents.append(keybrd_input)
trialComponents.append(fixation)
trialComponents.append(End_instruction)
trialComponents.append(clock_disp)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True

while continueRoutine:
    t = trialClock.getTime()
    #clock_disp.setAutoDraw(True)
    #clock_disp.setText(u"%.2f sec" % (t))
    #do_not_come_in=1
    if t >= 0.0 and instruction.status == NOT_STARTED and keybrd_input.status == NOT_STARTED:
        keybrd_input.status = STARTED
        # keyboard checking is just starting
        keybrd_input.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')        
        if change_fix_flag_hard==1:
            thisExp.addData('Note', 'hard task')
            instruction.text=u'\u63A5\u4E0B\u4F86\u7684\u5BE6\u9A57\uFF0C\u8ACB\u5C08\u6CE8\u4E2D\u9593\u7684\u6587\u5B57\u8B8A\u5316\uFF0C\n\n\u51FA\u73FE"1"\u6216"2"\u6216"3"\u6642\uFF0C\u8ACB\u5FEB\u901F\u6309\u4E0B\u6309\u9215\u3002\n\n\u5BE6\u9A57\u5373\u5C07\u958B\u59CB\uFF0C\u8ACB\u4FDD\u6301\u982D\u90E8\u8EAB\u9AD4\u4E0D\u8981\u6643\u52D5\u3002\n\n\u82E5\u7121\u554F\u984C\uFF0C\u8ACB\u6309\u4E00\u4E0B\u6309\u9215\u3002'
        if change_fix_flag_hard==0:
            thisExp.addData('Note', 'easy task')
            instruction.text=u'\u63A5\u4E0B\u4F86\u7684\u5BE6\u9A57\uFF0C\u8ACB\u5C08\u6CE8\u4E2D\u9593\u7684\u5341\u5B57\u8B8A\u5316\uFF0C\n\n\u5341\u5B57\u8B8A\u6210\u7D05\u8272\u6642\uFF0C\u8ACB\u5FEB\u901F\u6309\u4E0B\u6309\u9215\u3002\n\n\u5BE6\u9A57\u5373\u5C07\u958B\u59CB\uFF0C\u8ACB\u4FDD\u6301\u982D\u90E8\u8EAB\u9AD4\u4E0D\u8981\u6643\u52D5\u3002\n\n\u82E5\u7121\u554F\u984C\uFF0C\u8ACB\u6309\u4E00\u4E0B\u6309\u9215\u3002'
        instruction.setAutoDraw(True)
        win.flip()
        
        thisExp.nextEntry()
        theseKeys = event.getKeys(keyList=['1','2','3','4','5','n'])
        while ("2" in theseKeys)==0 :
            theseKeys = event.getKeys(keyList=['1','2','3','4','5','n'])
        
        instruction.text=u'Welcome! \u8ACB\u4FDD\u6301\u982D\u90E8\u8EAB\u9AD4\u4E0D\u8981\u6643\u52D5\uFF0C\u5BE6\u9A57\u5373\u5C07\u958B\u59CB\u3002'
        instruction.setAutoDraw(True)
        win.flip()
        
        while ("n" in theseKeys)==0 :
            theseKeys = event.getKeys(keyList=['1','2','3','4','5','n'])
        
        instruction.text=u'\u523A\u6FC0\u5373\u5C07\u64AD\u653E\uFF0C\u8ACB\u6CE8\u610F\u87A2\u5E55\u4E2D\u5FC3\u4F4D\u7F6E\u3002'
        instruction.setAutoDraw(True)
        win.flip()
        # *keybrd_input* updates
        # keep track of start time/frame for later

    if keybrd_input.status == STARTED:
        # listen key input
        theseKeys = event.getKeys(keyList=['1','2','3','4','5'])
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0 and trigger_count==0:  # at least one key was pressed
            if "5" in theseKeys:
                trigger_count=trigger_count+1
                press_any=press_any+1
                dummy_trigger_flag=dummy_trigger_flag+1
                if dummy_trigger_flag<=dummy_trigger:
                    trigger_count=0
                    #print dummy_trigger_flag
                
                if trigger_count==1:
                    trigger_time=trialClock.getTime()
                    thisExp.addData('Note', 'start time')
                    thisExp.addData('time', trigger_time)
                    thisExp.nextEntry()
                    instruction.setAutoDraw(False)
                    fixation.setAutoDraw(True)
                    win.flip()
                    this_time_frame_count_flag=-1
                    time_frame_count=0
    if  trigger_count>0 and t >=trigger_time+(time_frame_count+1)*time_period and t <= trigger_time+total_time:
        time_frame_count=time_frame_count+1



    if t >= 0.0 and trigger_count>0 and t > trigger_time and t <= trigger_time+total_time and End_instruction.status == NOT_STARTED :
        if len(theseKeys) > 0:  # at least one key was pressed
            press_any=press_any+len(theseKeys)
            t = trialClock.getTime()
            thisExp.addData('Note', theseKeys)
            thisExp.addData('time', t)
            thisExp.nextEntry()
        if "5" in theseKeys or "5,2" in theseKeys or "2,5" in theseKeys:
            trigger_count=trigger_count+1
        if "2" in theseKeys or "5,2" in theseKeys or "2,5" in theseKeys:
            if param_fix[time_frame_count]==1 or param_fix[time_frame_count-1]==1 or param_fix[time_frame_count-2]==1 or param_fix[time_frame_count-3]==1:
                press1_count=press1_count+1
        if endExpNow or event.getKeys(keyList=["escape"]):
            keybrd_input.status = STOPPED
            continueRoutine = False
            core.quit()
                
    
    if t >= 0.0 and trigger_count>0 and t > trigger_time and t <= trigger_time+total_time and End_instruction.status == NOT_STARTED :
        
        #print time_frame_count
        if time_frame_count==this_time_frame_count_flag+1:
            this_time_frame_count_flag=time_frame_count
            if param_fix[time_frame_count]==1:
                if change_fix_flag_hard==1 :
                    if time_frame_count%2==0:
                        kk=np.random.randint(0,3, size=1)
                        kk_old=kk
                    fixation.text=fix_choose[kk]
                    
                else:
                    kk=1
                    fixation.color=u'red'
            else:
                if change_fix_flag_hard==1:
                    #kk=np.random.randint(3,20, size=1)
                    if time_frame_count%2==0:
                        while kk_old == kk:
                            kk=np.random.randint(3,20, size=1)
                        kk_old=kk
                    fixation.text=fix_choose[kk]
                    
                else:
                    kk=0
                    fixation.color=u'black'

            if time_frame_count%2==1:
                if param[time_frame_count]==0 :
                    stim = none_blank
                if param[time_frame_count]==1 and contrast_flag[time_frame_count]==1:
                    stim = wedgeRonC1
                if param[time_frame_count]==2 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLonC1                    
                if param[time_frame_count]==1 and contrast_flag[time_frame_count]==2:
                    stim = wedgeRonC2
                if param[time_frame_count]==2 and contrast_flag[time_frame_count]==2:
                    stim = wedgeLonC2
                if param[time_frame_count]==3 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLonC1
                    stim2= wedgeRonC1
                if param[time_frame_count]==3 and contrast_flag[time_frame_count]==2:
                    stim = wedgeLonC2
                    stim2= wedgeRonC2
                if param[time_frame_count]==4 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLonC1s
                    stim2= wedgeRonC1s
            else:
                if param[time_frame_count]==0 :
                    stim = none_blank
                if param[time_frame_count]==1 and contrast_flag[time_frame_count]==1:
                    stim = wedgeRoffC1
                if param[time_frame_count]==2 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLoffC1                    
                if param[time_frame_count]==1 and contrast_flag[time_frame_count]==2:
                    stim = wedgeRoffC2
                if param[time_frame_count]==2 and contrast_flag[time_frame_count]==2:
                    stim = wedgeLoffC2
                if param[time_frame_count]==3 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLoffC1
                    stim2= wedgeRoffC1
                if param[time_frame_count]==3 and contrast_flag[time_frame_count]==2:
                    stim = wedgeLoffC2
                    stim2= wedgeRoffC2
                if param[time_frame_count]==4 and contrast_flag[time_frame_count]==1:
                    stim = wedgeLoffC1s
                    stim2= wedgeRoffC1s
            stim.draw()
            if param[time_frame_count]>=3:
                stim2.draw()
            center_block.draw()
            fixation.draw()
            win.flip()
            thisExp.addData('time', t)
            thisExp.addData('fix type', fix_choose[kk])
            thisExp.addData('stim', param_fix[time_frame_count])
            thisExp.addData('R or L', param[time_frame_count])
            thisExp.addData('HC or LC', contrast_flag[time_frame_count])
            thisExp.nextEntry()
            #print time_frame_count
        
    if t>=trigger_time+total_time  and End_instruction.status == NOT_STARTED and trigger_count>0:
        End_instruction_time = trialClock.getTime()  # underestimates by a little under one frame
        fixation.setAutoDraw(False)
        End_instruction.setAutoDraw(True)
        win.flip()
        thisExp.addData('Note', 'END')
        thisExp.addData('time', End_instruction_time)
        thisExp.nextEntry()
        thisExp.addData('Note', ['stimlus:',param_fix_stim1,'  press 1:',press1_count,'  trigger:',trigger_count, '  press any:', press_any])
        thisExp.nextEntry()
        print 'stimlus:',param_fix_stim1,'  press 1:',press1_count,'  trigger:',trigger_count, '  press any:', press_any
            
    if t>=0 and trigger_count>0 and event.getKeys(keyList=["a"]):
        fixation.setAutoDraw(False)
        End_instruction.setText(u'\u6709\u6B63\u78BA\u6309\u9375\u53CD\u61C9: %d / %d \n\u8AA4\u6309: %d \n\n\u7E3D\u8A08\u932F\u8AA4\u7387: %0.1f%%' %(press1_count,param_fix_stim1*2,press_any-press1_count-trigger_count-dummy_trigger,((press_any-press1_count-trigger_count-dummy_trigger)+(param_fix_stim1*2-press1_count))/param_fix_stim1/2*100))
        End_instruction.setAutoDraw(True)
        win.flip()
            
    if t>=0 and trigger_count>0 and event.getKeys(keyList=["r"]):
        fixation.setAutoDraw(False)
        End_instruction.setText(u'\u8ACB\u9589\u773C\u4F11\u606F1\u5206\u9418\n\n\u982D\u90E8\u8EAB\u9AD4\u4FDD\u6301\u4E0D\u8981\u6643\u52D5\n\n\u5BE6\u9A57\u5373\u5C07\u958B\u59CB\u3002')
        End_instruction.setAutoDraw(True)
        win.flip()
        
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        End_instruction.setAutoDraw(False)
        keybrd_input.status = STOPPED
        continueRoutine = False
        core.quit()
    




win.close()
core.quit()