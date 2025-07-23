@echo off
set ADB=adb
set DPATH=

set time2=%time: =0%
set hour=%time2:~0,2%
set minute=%time2:~3,2%
set second=%time2:~6,2%

set logname=%hour%-%minute%-%second%

mkdir %DPATH%\Logs_%logname%	

%ADB% wait-for-device devices
%ADB% wait-for-device root
%ADB% wait-for-device shell mount -o rw,remount /

%ADB% pull /uplog %DPATH%\Logs_%logname%\uplog

pause

