@echo off
set ADB=adb
set CMD2="top"
%ADB% wait-for-device shell %CMD2%