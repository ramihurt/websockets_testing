@echo off
set CMD1=sldd Diag readDidinternal 1022

@echo off
%ADB_PATH% wait-for-device shell %CMD1%

%ADB_PATH% wait-for-device shell %CMD1%
