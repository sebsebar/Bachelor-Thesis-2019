function [results m] = memTest(subID, wPtr, rect, studyList, unstudiedList, studyTime, p, blockNumber, condition)

%get params for experiment
m = getMemParams(subID, studyList, unstudiedList, condition);

if IsWin
    dataDir = [pwd '\memData\'];
else
    dataDir = [pwd '/memData/'];
end

if IsWin
    addpath([pwd '\functions']);
else
    addpath([pwd '/functions']);
end

KbName('UnifyKeyNames');

%initialize results struct
results.subID = m.subID;
results.studiedListNum = m.studiedListNum;
results.unstudiedListNum = m.unstudiedListNum;
results.studiedOrder = m.studiedPerm;
results.unstudiedOrder = m.unstudiedPerm;
results.studiedWordList = m.studied_list(results.studiedOrder);
results.unstudiedWordList = m.unstudied_list(results.unstudiedOrder);
results.condition = condition;
results.studiedWord = {};
results.unstudiedWord = {};
results.studiedSide = {};
results.rtChoice = [];
results.rtConf = [];
results.responseChoice = {};
results.responseConf = [];


%screen center
[mx, my] = RectCenter(rect);
[p.mx,p.my] = RectCenter(rect);
%text positions
positions = [mx - 200, mx + 100];
fixCrossBlack = Screen('MakeTexture', wPtr, m.FixCrB);
fixCrossWhite = Screen('MakeTexture', wPtr, m.FixCrW);


%% initialize triggers

if p.send_triggers
    
    send_trigger = initialiseSerialPortTrigger(p.port_number);
    
    send_trigger(p.reset_trigger);
    
end


%% Main experiment
% Get ready to see the display
Screen('TextSize',wPtr,24);
if blockNumber == 1
    DrawFormattedText(wPtr, 'We will now show you the first list of words to study...', 'center', my-200, m.textColor, [], [], [], 1.5);
else
    DrawFormattedText(wPtr, 'We will now show you the next list of words to study...', 'center', my-200, m.textColor, [], [], [], 1.5);
end
DrawFormattedText(wPtr, 'Press any key to start studying!', 'center', 'center', m.textColor, [], [], [], 1.5);
studyStart = Screen('Flip', wPtr);
KbWait;

%display list to study
DrawFormattedText(wPtr,m.studyListDisplay1, mx-450, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay2, mx-250, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay3, mx-50, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay4, mx+150, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay5, mx+350, 'center', m.textColor, [], [], [], 1.5);
studyStart = Screen('Flip', wPtr);

if p.send_triggers
    
    send_trigger(p.block_trigger+condition);
    WaitSecs(p.trig_reset_wait);
    send_trigger(p.reset_trigger);
    
end


disp(studyStart);
disp(studyTime);
disp(studyStart + (studyTime - 10));
%WaitSecs(studyTime - 10);
DrawFormattedText(wPtr,m.studyListDisplay1, mx-450, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay2, mx-250, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay3, mx-50, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay4, mx+150, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,m.studyListDisplay5, mx+350, 'center', m.textColor, [], [], [], 1.5);
DrawFormattedText(wPtr,'10 seconds left...', 'center', my*2 - 200, m.textColor, [], [], [], 1.5);
thirtySecsLeft = Screen('Flip', wPtr, studyStart + (studyTime - 10));
%WaitSecs(10);

DrawFormattedText(wPtr,m.instructions2, 'center', 'center', m.textColor);
Screen('Flip', wPtr, thirtySecsLeft + 10);
KbWait;

for i = 1:size(m.studied_list,1)
    
    sidechoice = randperm(2);
    
    DrawFormattedText(wPtr,results.studiedWordList{i}, positions(sidechoice(1)), 'center', m.textColor);
    DrawFormattedText(wPtr,results.unstudiedWordList{i}, positions(sidechoice(2)), 'center', m.textColor);
    Screen('DrawTexture', wPtr, fixCrossBlack,[],[mx-10,my-10,mx+10,my+10]);
    vbl = Screen('Flip',wPtr);
    
    if p.send_triggers
        
        send_trigger(condition);
        WaitSecs(p.trig_reset_wait);
        send_trigger(p.reset_trigger);
        
    end
    
    FlushEvents;
    trialComplete = false;
    start_secs = GetSecs;
    secs = start_secs;
    while ~trialComplete & (secs-start_secs) < p.times.words
        [k respTime keyCode] = KbCheck();
        
        
        if strcmp(KbName(keyCode),'LeftArrow') | strcmp(KbName(keyCode),'RightArrow')
            trialComplete = true;
            rt = respTime-vbl;
        elseif strcmp(KbName(keyCode),'ESCAPE')
            Screen('CloseAll')
            return
        end
          
      
        secs = GetSecs;
        
    end
   
    response = KbName(keyCode);     
    
    % show confirmation of response
    DrawFormattedText(wPtr,results.studiedWordList{i}, positions(sidechoice(1)), 'center', m.textColor);
    DrawFormattedText(wPtr,results.unstudiedWordList{i}, positions(sidechoice(2)), 'center', m.textColor);
    Screen('DrawTexture', wPtr, fixCrossBlack,[],[mx-10,my-10,mx+10,my+10]);
    
    Screen('TextSize',wPtr,48);
    if strcmp(response, 'LeftArrow')
        DrawFormattedText(wPtr,'*', positions(1), my-100, m.textColor);
    elseif strcmp(response, 'RightArrow')
        DrawFormattedText(wPtr,'*', positions(2), my-100, m.textColor);
    end
    Screen('TextSize',wPtr,24);
    vbl = Screen('Flip',wPtr);
    pause(p.memConfirm_inSecs);
    
    %record results
    results.studiedWord{i} = results.studiedWordList{i};
    results.unstudiedWord{i} = results.unstudiedWordList{i};
    results.studiedSide{i} = m.positions(sidechoice(1));
    results.rtChoice(i) = rt;
    results.responseChoice{i} = response;
    
    if p.send_triggers
        
        send_trigger(p.confidence_trig+condition);
        WaitSecs(p.trig_reset_wait);
        send_trigger(p.reset_trigger);
        
    end
    
    
    if (k == 1)
        
        % now collect confidence
        [conf RT] = collectConfidenceDiscrete(wPtr,p);
        
        results.responseConf(i) = conf;
        results.rtConf(i) = RT;
    else
        DrawFormattedText(wPtr,'No response!','center','center');
        Screen('Flip',wPtr);
        pause(p.confFBDuration_inSecs + p.confDuration_inSecs);
        
        results.responseConf(i) = NaN;
        results.rtConf(i) = NaN;
    end
    %
    %     if i == size(m.wordLists,1)/2   % give a break halfway through
    %         DrawFormattedText(wPtr, 'Please take a break!', 'center', my-150, m.textColor, [], [], [], 1.5);
    %         DrawFormattedText(wPtr, 'Press any key to answer the remaining questions on this list...', 'center', 'center', m.textColor, [], [], [], 1.5);
    %         Screen('Flip', wPtr);
    %         KbWait;
    %     end
    %
end
