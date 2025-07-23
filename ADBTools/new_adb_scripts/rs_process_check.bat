@echo off
set ADB=adb
set CMD1="top"
%ADB% wait-for-device shell %CMD1%