@echo off
set CMD1="strings /tmp/property | grep version"
set CMD2="strings /opt/dce/bin/dce* | grep VERSION"
%ADB_PATH% wait-for-device shell %CMD1%
%ADB_PATH% shell %CMD2%