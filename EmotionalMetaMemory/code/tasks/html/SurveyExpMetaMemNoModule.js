/************************* 
 * Surveyexpmetamem Test *
 *************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'SurveyExpMetaMem';  // from the Builder filename that created this script
let expInfo = {'ParticipantID': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Intro_To_ClickRoutineBegin);
flowScheduler.add(Intro_To_ClickRoutineEachFrame);
flowScheduler.add(Intro_To_ClickRoutineEnd);
flowScheduler.add(introductionRoutineBegin);
flowScheduler.add(introductionRoutineEachFrame);
flowScheduler.add(introductionRoutineEnd);
flowScheduler.add(valence_instructionRoutineBegin);
flowScheduler.add(valence_instructionRoutineEachFrame);
flowScheduler.add(valence_instructionRoutineEnd);
flowScheduler.add(arousal_instructionRoutineBegin);
flowScheduler.add(arousal_instructionRoutineEachFrame);
flowScheduler.add(arousal_instructionRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(goodbyeRoutineBegin);
flowScheduler.add(goodbyeRoutineEachFrame);
flowScheduler.add(goodbyeRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var Intro_To_ClickClock;
var text;
var mouse_4;
var introductionClock;
var introText;
var mouse;
var valence_instructionClock;
var InstructValenceText;
var Valence;
var mouse_2;
var arousal_instructionClock;
var InstructArousalText;
var Arousal;
var mouse_3;
var Arousal_2Clock;
var WordPresentation;
var ArousalGuide;
var text_3;
var A_key_resp;
var Valence_2Clock;
var WordPresentation2;
var ValenceImage;
var text_2;
var key_resp;
var goodbyeClock;
var GoodbyeText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Intro_To_Click"
  Intro_To_ClickClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome To The Emotional Meta-Memory Survey\n\nClick On the Screen To Continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  mouse_4 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_4.mouseClock = new util.Clock();
  // Initialize components for Routine "introduction"
  introductionClock = new util.Clock();
  introText = new visual.TextStim({
    win: psychoJS.window,
    name: 'introText',
    text: 'Welcome To The Word-Rating Survey \nI appreciate you for participating in this part of the study. The survey being conducted today is investigating emotion, and concerns how people respond to different types of words. On the next screens you will see some figures.\nWe call these figures SAM, and you will be using these figures to rate how different words seem to you. \nSAM shows two different kinds of feelings:\n\nHappy vs. Unhappy \nand \nExcited vs. Calm.\n \nYou will use both of these ratings for each word that is presented to you. Please notice that both feelings are arrayed along a 9-point scale. \n\nOn the happy vs. unhappy scale, which ranges from a frown to a smile, 9 means happy, pleased, satisfied, contented or hopeful. 1 on the other hand means unhappy, annoyed, unsatisfied, melancholic, despaired, or bored. If the word feels neutral to you, neither happy nor sad, you can select 5 on the ratingscale. \n\nOn the excited vs. calm scale, which ranges from a SAM to an exploding SAM, 9 means stimulated, excited, frenzied, jittered, or aroused. 1 on the other hand means relaxed, calm, sluggish, dull, sleepy, or unaroused. If the word feels neutral to you, neither exciting nor calm, you can select 5 on the ratingscale. \n\nThere will be a total of 1200 words that you will need to rated and you will be compensated 100kr for helping us with this survey part ofthe study.\n\nPlease work at a rapid place and don’t spend too much time thinking about each word. Rather, make your ratings based on your first\nand immediate reaction as you read each word. \n\nClick the screen to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "valence_instruction"
  valence_instructionClock = new util.Clock();
  InstructValenceText = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructValenceText',
    text: 'This Is The Scale For Valence Ratings\n\nA 1 On The Scale Equals To Very Low Valence (Unhappy)\n\nA 5 On The Scale Equals To Neutral\n\nA 9 On The Scale Equals To Very High Valence (Happy)\n\nYou select a number on the scale using your keyboards keys: 1-9\n\nClick on the screen to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Valence = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Valence', units : undefined, 
    image : 'Valence.png', mask : undefined,
    ori : 0, pos : [0, 0.3], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "arousal_instruction"
  arousal_instructionClock = new util.Clock();
  InstructArousalText = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructArousalText',
    text: 'This Is The Scale For Arousal Ratings\n\nA 1 On The Scale Equals To Very Low Arousal (Calm)\n\nA 5 On The Scale Equals To Neutral\n\nA 9 On The Scale Equals To Very High Arousal (Excited)\n\nYou select a number on the scale using your keyboards keys: 1-9\n\nClick on the screen to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Arousal = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Arousal', units : undefined, 
    image : 'Arousal.png', mask : undefined,
    ori : 0, pos : [0, 0.3], size : [0.5, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  mouse_3 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_3.mouseClock = new util.Clock();
  // Initialize components for Routine "Arousal_2"
  Arousal_2Clock = new util.Clock();
  WordPresentation = new visual.TextStim({
    win: psychoJS.window,
    name: 'WordPresentation',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.2)], height: 0.09,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ArousalGuide = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ArousalGuide', units : undefined, 
    image : 'Arousal.png', mask : undefined,
    ori : 0, pos : [0, 0.25], size : [0.8, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Arousal\n1 = Calm, 9 = Excited',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  A_key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Valence_2"
  Valence_2Clock = new util.Clock();
  WordPresentation2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WordPresentation2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.2)], height: 0.09,  wrapWidth: undefined, ori: 0,
    color: new util.Color('White'),  opacity: 1,
    depth: 0.0 
  });
  
  ValenceImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ValenceImage', units : undefined, 
    image : 'Valence.png', mask : undefined,
    ori : 0, pos : [0, 0.25], size : [0.8, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Valence\n1 = Unhappy, 9 = Happy',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "goodbye"
  goodbyeClock = new util.Clock();
  GoodbyeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'GoodbyeText',
    text: 'Thank You For Participating \nIn This Survey Part Of The Experiment!\n\nIt Has Been A PleasureTo Have You On Board!\n\nTake Care!',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var gotValidClick;
var Intro_To_ClickComponents;
function Intro_To_ClickRoutineBegin() {
  //------Prepare to start Routine 'Intro_To_Click'-------
  t = 0;
  Intro_To_ClickClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse_4
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  Intro_To_ClickComponents = [];
  Intro_To_ClickComponents.push(text);
  Intro_To_ClickComponents.push(mouse_4);
  
  Intro_To_ClickComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
var continueRoutine;
function Intro_To_ClickRoutineEachFrame() {
  //------Loop for each frame of Routine 'Intro_To_Click'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Intro_To_ClickClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  // *mouse_4* updates
  if (t >= 0.0 && mouse_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse_4.tStart = t;  // (not accounting for frame time here)
    mouse_4.frameNStart = frameN;  // exact frame index
    mouse_4.status = PsychoJS.Status.STARTED;
    mouse_4.mouseClock.reset();
    prevButtonState = mouse_4.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse_4.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  Intro_To_ClickComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Intro_To_ClickRoutineEnd() {
  //------Ending Routine 'Intro_To_Click'-------
  Intro_To_ClickComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  const xys = mouse_4.getPos();
  const buttons = mouse_4.getPressed();
  psychoJS.experiment.addData('mouse_4.x', xys[0]);
  psychoJS.experiment.addData('mouse_4.y', xys[1]);
  psychoJS.experiment.addData('mouse_4.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse_4.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse_4.rightButton', buttons[2]);
  // the Routine "Intro_To_Click" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var introductionComponents;
function introductionRoutineBegin() {
  //------Prepare to start Routine 'introduction'-------
  t = 0;
  introductionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  introductionComponents = [];
  introductionComponents.push(introText);
  introductionComponents.push(mouse);
  
  introductionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function introductionRoutineEachFrame() {
  //------Loop for each frame of Routine 'introduction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = introductionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *introText* updates
  if (t >= 0.0 && introText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    introText.tStart = t;  // (not accounting for frame time here)
    introText.frameNStart = frameN;  // exact frame index
    introText.setAutoDraw(true);
  }

  // *mouse* updates
  if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse.tStart = t;  // (not accounting for frame time here)
    mouse.frameNStart = frameN;  // exact frame index
    mouse.status = PsychoJS.Status.STARTED;
    mouse.mouseClock.reset();
    prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  introductionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function introductionRoutineEnd() {
  //------Ending Routine 'introduction'-------
  introductionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  const xys = mouse.getPos();
  const buttons = mouse.getPressed();
  psychoJS.experiment.addData('mouse.x', xys[0]);
  psychoJS.experiment.addData('mouse.y', xys[1]);
  psychoJS.experiment.addData('mouse.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse.rightButton', buttons[2]);
  // the Routine "introduction" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var valence_instructionComponents;
function valence_instructionRoutineBegin() {
  //------Prepare to start Routine 'valence_instruction'-------
  t = 0;
  valence_instructionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse_2
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  valence_instructionComponents = [];
  valence_instructionComponents.push(InstructValenceText);
  valence_instructionComponents.push(Valence);
  valence_instructionComponents.push(mouse_2);
  
  valence_instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function valence_instructionRoutineEachFrame() {
  //------Loop for each frame of Routine 'valence_instruction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = valence_instructionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *InstructValenceText* updates
  if (t >= 0.0 && InstructValenceText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    InstructValenceText.tStart = t;  // (not accounting for frame time here)
    InstructValenceText.frameNStart = frameN;  // exact frame index
    InstructValenceText.setAutoDraw(true);
  }

  
  // *Valence* updates
  if (t >= 0.0 && Valence.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Valence.tStart = t;  // (not accounting for frame time here)
    Valence.frameNStart = frameN;  // exact frame index
    Valence.setAutoDraw(true);
  }

  // *mouse_2* updates
  if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse_2.tStart = t;  // (not accounting for frame time here)
    mouse_2.frameNStart = frameN;  // exact frame index
    mouse_2.status = PsychoJS.Status.STARTED;
    mouse_2.mouseClock.reset();
    prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse_2.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  valence_instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function valence_instructionRoutineEnd() {
  //------Ending Routine 'valence_instruction'-------
  valence_instructionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  const xys = mouse_2.getPos();
  const buttons = mouse_2.getPressed();
  psychoJS.experiment.addData('mouse_2.x', xys[0]);
  psychoJS.experiment.addData('mouse_2.y', xys[1]);
  psychoJS.experiment.addData('mouse_2.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse_2.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse_2.rightButton', buttons[2]);
  // the Routine "valence_instruction" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var arousal_instructionComponents;
function arousal_instructionRoutineBegin() {
  //------Prepare to start Routine 'arousal_instruction'-------
  t = 0;
  arousal_instructionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse_3
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  arousal_instructionComponents = [];
  arousal_instructionComponents.push(InstructArousalText);
  arousal_instructionComponents.push(Arousal);
  arousal_instructionComponents.push(mouse_3);
  
  arousal_instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function arousal_instructionRoutineEachFrame() {
  //------Loop for each frame of Routine 'arousal_instruction'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = arousal_instructionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *InstructArousalText* updates
  if (t >= 0.0 && InstructArousalText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    InstructArousalText.tStart = t;  // (not accounting for frame time here)
    InstructArousalText.frameNStart = frameN;  // exact frame index
    InstructArousalText.setAutoDraw(true);
  }

  
  // *Arousal* updates
  if (t >= 0.0 && Arousal.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Arousal.tStart = t;  // (not accounting for frame time here)
    Arousal.frameNStart = frameN;  // exact frame index
    Arousal.setAutoDraw(true);
  }

  // *mouse_3* updates
  if (t >= 0.0 && mouse_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse_3.tStart = t;  // (not accounting for frame time here)
    mouse_3.frameNStart = frameN;  // exact frame index
    mouse_3.status = PsychoJS.Status.STARTED;
    mouse_3.mouseClock.reset();
    prevButtonState = mouse_3.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse_3.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  arousal_instructionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function arousal_instructionRoutineEnd() {
  //------Ending Routine 'arousal_instruction'-------
  arousal_instructionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  const xys = mouse_3.getPos();
  const buttons = mouse_3.getPressed();
  psychoJS.experiment.addData('mouse_3.x', xys[0]);
  psychoJS.experiment.addData('mouse_3.y', xys[1]);
  psychoJS.experiment.addData('mouse_3.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse_3.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse_3.rightButton', buttons[2]);
  // the Routine "arousal_instruction" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
var trialIterator;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Workbook2.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(Arousal_2RoutineBegin);
    thisScheduler.add(Arousal_2RoutineEachFrame);
    thisScheduler.add(Arousal_2RoutineEnd);
    thisScheduler.add(Valence_2RoutineBegin);
    thisScheduler.add(Valence_2RoutineEachFrame);
    thisScheduler.add(Valence_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var Arousal_2Components;
function Arousal_2RoutineBegin() {
  //------Prepare to start Routine 'Arousal_2'-------
  t = 0;
  Arousal_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  WordPresentation.setText(word);
  A_key_resp.keys = undefined;
  A_key_resp.rt = undefined;
  // keep track of which components have finished
  Arousal_2Components = [];
  Arousal_2Components.push(WordPresentation);
  Arousal_2Components.push(ArousalGuide);
  Arousal_2Components.push(text_3);
  Arousal_2Components.push(A_key_resp);
  
  Arousal_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function Arousal_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Arousal_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Arousal_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *WordPresentation* updates
  if (t >= 0.0 && WordPresentation.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    WordPresentation.tStart = t;  // (not accounting for frame time here)
    WordPresentation.frameNStart = frameN;  // exact frame index
    WordPresentation.setAutoDraw(true);
  }

  
  // *ArousalGuide* updates
  if (t >= 0.0 && ArousalGuide.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ArousalGuide.tStart = t;  // (not accounting for frame time here)
    ArousalGuide.frameNStart = frameN;  // exact frame index
    ArousalGuide.setAutoDraw(true);
  }

  
  // *text_3* updates
  if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  
  // *A_key_resp* updates
  if (t >= 0.0 && A_key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    A_key_resp.tStart = t;  // (not accounting for frame time here)
    A_key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    A_key_resp.clock.reset();
    A_key_resp.start();
    A_key_resp.clearEvents();
  }

  if (A_key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = A_key_resp.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      A_key_resp.keys = theseKeys[0].name;  // just the last key pressed
      A_key_resp.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  Arousal_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Arousal_2RoutineEnd() {
  //------Ending Routine 'Arousal_2'-------
  Arousal_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('A_key_resp.keys', A_key_resp.keys);
  if (typeof A_key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('A_key_resp.rt', A_key_resp.rt);
      routineTimer.reset();
      }
  
  A_key_resp.stop();
  // the Routine "Arousal_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var Valence_2Components;
function Valence_2RoutineBegin() {
  //------Prepare to start Routine 'Valence_2'-------
  t = 0;
  Valence_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  WordPresentation2.setText(word);
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  Valence_2Components = [];
  Valence_2Components.push(WordPresentation2);
  Valence_2Components.push(ValenceImage);
  Valence_2Components.push(text_2);
  Valence_2Components.push(key_resp);
  
  Valence_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function Valence_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Valence_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Valence_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *WordPresentation2* updates
  if (t >= 0.0 && WordPresentation2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    WordPresentation2.tStart = t;  // (not accounting for frame time here)
    WordPresentation2.frameNStart = frameN;  // exact frame index
    WordPresentation2.setAutoDraw(true);
  }

  
  // *ValenceImage* updates
  if (t >= 0.0 && ValenceImage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ValenceImage.tStart = t;  // (not accounting for frame time here)
    ValenceImage.frameNStart = frameN;  // exact frame index
    ValenceImage.setAutoDraw(true);
  }

  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    key_resp.clock.reset();
    key_resp.start();
    key_resp.clearEvents();
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['1', '2', '3', '4', '5', '6', '7', '8', '9'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp.keys = theseKeys[0].name;  // just the last key pressed
      key_resp.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  Valence_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Valence_2RoutineEnd() {
  //------Ending Routine 'Valence_2'-------
  Valence_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "Valence_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var goodbyeComponents;
function goodbyeRoutineBegin() {
  //------Prepare to start Routine 'goodbye'-------
  t = 0;
  goodbyeClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  goodbyeComponents = [];
  goodbyeComponents.push(GoodbyeText);
  
  goodbyeComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function goodbyeRoutineEachFrame() {
  //------Loop for each frame of Routine 'goodbye'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = goodbyeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *GoodbyeText* updates
  if (t >= 0.0 && GoodbyeText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    GoodbyeText.tStart = t;  // (not accounting for frame time here)
    GoodbyeText.frameNStart = frameN;  // exact frame index
    GoodbyeText.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (GoodbyeText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    GoodbyeText.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  goodbyeComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function goodbyeRoutineEnd() {
  //------Ending Routine 'goodbye'-------
  goodbyeComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
