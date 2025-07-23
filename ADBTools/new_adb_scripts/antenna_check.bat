@echo off
set CMD1=sldd region gethalsystemnation
@echo off
%ADB_PATH% wait-for-device shell %CMD1%
