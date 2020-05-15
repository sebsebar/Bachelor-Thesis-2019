function memWrapper

%% initialize idiomatic stuff for starting psychtoolbox
AssertOpenGL;
clear all; close all;
screenSize = input('screen? 1=full, 2=test, 3=alt ')
% screenSize = 3;
Screen('Preference','SkipSyncTests', 1);

KbName('UnifyKeyNames');
PsychJavaTrouble()      
KbCheck;

if IsWin
    addpath([pwd '\functions']);
else
    addpath([pwd '/functions']);
end

olddebuglevel = Screen('Preference', 'VisualDebugLevel', 3);

%get params for experiment
p = getExpParams;

%if duplicate subID abort
if p.isTaken == 1;
    return
end

%%  open full screen window on main screen and set gamma to flat
if screenSize == 1
    screenDim = [];
    screenNum = 0;
elseif screenSize == 2
    screenDim = [100 100 1000 1000];    % set to [] for full screen
    screenNum = 0;
else
    screenDim = [];
    screens=Screen('Screens');
    screenNum=max(screens);
end

[wPtr,rect]=Screen('OpenWindow',screenNum, p.bgColor, screenDim);
HideCursor;
[p.midW p.midH] = getScreenMidpoint(wPtr);


%% condition randomization set-up

% randomize for each subject a 1-4 integer which will randomly be assigned to the block order, study list order, or study time order

subject_order = randi(4,1); 
blocks = eval(['p.BlockOrder', num2str(subject_order)]);

studied_list_order = eval(['p.studyListOrder', num2str(subject_order)]);


which_word_list = [0 0 0 0]; % initialize list counter for each condition

i = 1;

if mod(subject_order,2) ==0
    
    i = -1;
end

unstudied_list_order =  eval(['p.studyListOrder', num2str(subject_order)+i]);


study_time_order = eval(['p.studyTimeOrder', num2str(subject_order)]);

%% practice






%% run block loop



for block = 1:numel(blocks)
    

     
 
%%
    
    
condition = blocks(block);    % 1 = VHAH, 2 = VHAL, 3 = VLAH, 4 = VLAL 
which_word_list(condition) = which_word_list(condition) + 1; 
studied_list = studied_list_order(which_word_list(condition));
unstudied_list = unstudied_list_order(which_word_list(condition));
study_time = study_time_order(which_word_list(condition));

%  %% for testing
%  if screenSize == 2
%      study_time = 10;
%  end

roundNum = block;
mem_instructions(wPtr, p, roundNum);
[results m] = memTest(p.subID, wPtr, rect, studied_list, unstudied_list, study_time, p, roundNum, condition);    
m.fileName=['memExpData' p.subID{1} '_' num2str(roundNum) '.mat'];
cd data
save(m.fileName, 'results', 'p', 'm');
   
        
end


Screen('CloseAll');
ShowCursor;