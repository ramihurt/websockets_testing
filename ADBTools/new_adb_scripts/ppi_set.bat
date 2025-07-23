@echo off
set CMD1=sldd PPI setConsentState 2 2 2 2
@echo off
echo .....//Set PPI//.....
@echo off
%ADB_PATH% wait-for-device shell %CMD1%