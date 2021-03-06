function exitNow = mem_instructions(window, parameters, roundNum)

structName='parameters';
unpackStructFields

sx=120;
sy='center';
wrapat=60;

    %% write text
if (roundNum == 1)


    i=1;
    pg{i} = ['Welcome to this experiment!\n',...
    'In this task we will ask you to complete a word memory test.\n',...
    'You will be shown 50 English words on the\n'...
    'screen, and will have between 30 seconds and 1.5 minutes\n'...
    'to study and memorize them.\n\n'...
    'Please do your best to remember as many of\n' ...
    'them as you can!\n\n'...
    'You will be told when there is 10 seconds\n' ...
    'left for you to study this list.\n\n'...
    'After the time is up, you will be asked to \n' ...
    'identify words on the list that you just\n'...
    'studied.\n\n'];

    nextpg{i}   = '__________\n\nPlease press any key to continue.';
    waitTime(i) = 1;

    i=i+1;
    pg{i} = ['MEMORY TEST\n\n' ...
        'You will see two words on the screen, one on the list, and one not on the list.\n\n'...
        'To indicate that the word on the LEFT was \n',...
        'on the list you studied, press the left arrow key.\n\n'...
        'To indicate that the word on the RIGHT was\n',...
        'on the list you studied, press the right arrow key.\n'...
        'There is no time limit.\n\n'];

    nextpg{i}   = '__________\n\nPress any key to continue.\nPress the left arrow key to go back.';
    waitTime(i) = 1;
    
    i=i+1;
    pg{i} = ['MEMORY TEST\n\n' ...
    'After you make a choice,\n' ...
    'you will see a sliding scale to allow you to rate your confidence in getting the right answer.\n\n'...
    'You can move the cursor around on the scale using the left and right arrow keys\n'... 
    'The left end of the scale means that you are less confident than normal, and\n'...
    'the right end of the scale means that you are more confident than normal.\n\n'...
    'As we are interested in relative changes in confidence, we encourage you to use the whole scale.\n\n'];

    nextpg{i}   = '__________\n\nPress any key to see some practice examples!';
    waitTime(i) = 1;

elseif (roundNum == 2)
   
    i=1;
    pg{i} = ['MEMORY TEST\n\n' ...
    'You will now be given between 30s and 1.5 minutes to\n' ...
    'study a new word list.\n\n\n'...
    'Please do your best; Good luck!\n\n'];

    nextpg{i}   = '__________\n\nPress any key to begin studying.';
    waitTime(i) = 1;

end

oldTextSize = Screen('TextSize',window,28);

exitNow = 0;

% waitTime = zeros(size(waitTime));



%% present instructions

j=1;
while j <= length(pg)
    DrawFormattedText(window,pg{j},sx,sy,0,wrapat);
    Screen('Flip',window);
    
    WaitSecs(waitTime(j));
    [nx ny] = DrawFormattedText(window,pg{j},sx,sy,0,wrapat);
    DrawFormattedText(window,nextpg{j},sx,ny);
    Screen('Flip',window);
    KbWait(keyboardNumber);
    
    waitTime(j) = .5;
    
    [k s key] = KbCheck(keyboardNumber);
    switch KbName(key)
        case exitKey, exitNow = 1; break;
        
        case 'LeftArrow'
            if j > 1, j=j-1; end
            
        otherwise
            % incremenet page counter
            j=j+1;
    end
end