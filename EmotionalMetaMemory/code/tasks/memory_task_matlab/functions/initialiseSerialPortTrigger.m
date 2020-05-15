function sendTrigger = initialiseSerialPortTrigger(DEVICE_ID)

if nargin < 1
    DEVICE_ID = 'COM3';
end

configStr = ['BaudRate=9600 Parity=None DataBits=8 StopBits=1 '...
             'FlowControl=None ReceiverEnable=0 DTR=1 RTS=0'];
% configStr = 'DTR=1';

try
    ph = check_ioport(DEVICE_ID, configStr);
    sendTrigger = @(code) send_serial_trigger(ph, code); 
catch
    sendTrigger = @(code) print_if_nonzero(code);
end
end

function port_handle = check_ioport(DEVICE_ID, configStr)

port_handle = IOPort('OpenSerialPort', DEVICE_ID, configStr);
end

function send_serial_trigger(ph, int_code)

if int_code < 0
    IOPort('Close', ph);
else
    blocking=1;

    [nwritten, when, errmsg, prewritetime, postwritetime, lastchecktime] = ...
        IOPort('Write', ph, uint8(int_code), blocking);

end
end

function print_if_nonzero(code)
    if code > 0
        fprintf(1, 'TRIG: %d\n', code);
    end
end