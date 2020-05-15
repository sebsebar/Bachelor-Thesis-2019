function p = getExpParams
% Modified by SF 24/10/12 to have only one day, six sessions

p.textColor = [0 0 0];
p.bgColor = [127 127 127];
p.sittingDist = 60; % in cm

p.exitKey='ESCAPE';

if IsOSX
    p.keyboardNumber = getKeyboardNumber;
else
    p.keyboardNumber = [];
end

p.isTaken = 0;
p.subID = inputdlg('Please Enter SubjectID','SubjectID');
% p.age = inputdlg('Age? ','Age');
% p.gender = inputdlg('Gender? M/F','Gender');
% p.hand = inputdlg('Handedness? R/L ','Hand');

% check if this filename is OK
p.filename = ['memData' p.subID{1} '.mat'];

if IsWin
    dataDir = [pwd '\memData\'];
else
    dataDir = [pwd '/memData/'];
end

% check inputs
d = dir(dataDir);

for i = 1:length(d)
    if strcmp(p.filename,d(i).name)
        disp('This subjectID / day combination is already taken! Please use a different subject ID.');
        p.isTaken = 1;
        return
    end
end

p.filename = [dataDir p.filename];

% confidence scale
p.VASwidth_inDegrees = 6;
p.VASheight_inDegrees = 2;
p.VASoffset_inDegrees = 0;
p.arrowWidth_inDegrees = 0.5;


p.VASwidth_inPixels = degrees2pixels(p.VASwidth_inDegrees, p.sittingDist);
p.VASheight_inPixels = degrees2pixels(p.VASheight_inDegrees, p.sittingDist);
p.VASoffset_inPixels = degrees2pixels(p.VASoffset_inDegrees, p.sittingDist);
p.arrowWidth_inPixels = degrees2pixels(p.arrowWidth_inDegrees, p.sittingDist);

% Stimulus timings

p.chDuration_inSecs       = 0.7;
p.memDuration_inSecs = Inf;
p.memConfirm_inSecs = .5;
p.confDuration_inSecs = 4;
p.confFBDuration_inSecs = 0.25;
p.ITIDuration_inSecs      = 0.25;  % extra time at end of trial to finalize data collection

%% block & list orders

p.BlockOrder1 = [2 1 4 3, 4 3 2 1, 2 3 4 1] ; % pseudo randomized so no arousal repeats
p.BlockOrder2 = flip(p.BlockOrder1);  % counter balanced across participants
p.BlockOrder3 = [4 3 2 1, 2 3 4 1,  3 2 1 4] ; % pseudo randomized so no arousal repeats
p.BlockOrder4 = flip(p.BlockOrder3);  % counter balanced across participants


p.studyListOrder1 = [1 3 5];
p.studyListOrder2 = [2 4 6];
p.studyListOrder3 = [5 3 1];
p.studyListOrder4 = [6 4 2];


p.studyTimeOrder1= [0.5 1 1.5]*60;
p.studyTimeOrder2= [1 0.5 1.5]*60;
p.studyTimeOrder3= [1.5 0.5 1]*60;
p.studyTimeOrder4= [0.5 1.5 1]*60;



