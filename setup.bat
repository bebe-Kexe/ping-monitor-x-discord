@echo off
chcp 65001 >nul
title Installing Dependencies...
setlocal EnableDelayedExpansion

echo Installing dependencies from requirements.txt...
echo.


set count=0
for /f "usebackq delims=" %%a in ("requirements.txt") do (
    set /a count+=1
)

set current=0


for /f "usebackq delims=" %%a in ("requirements.txt") do (
    set /a current+=1
    pip install %%a >nul 2>&1
    set /a percent=100*current/count

    set bar=[ ]
    set /a filled=percent/10
    set empty=10

    set progress=
    for /l %%b in (1,1,!filled!) do set progress=!progress!█
    set /a empty=empty-filled

    for /l %%c in (1,1,!empty!) do set progress=!progress!-

    echo !bar: =! !percent!%% %%a
    echo !progress!
    timeout /nobreak /t 1 >nul
)

echo.
echo All dependencies installed. You can proceed to run start.bat.
pause
