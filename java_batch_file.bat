@echo off
set size=0
break > output.txt
set ad=%cd%
javac %1/%2 2> com.txt
call :filesize "com.txt"
if %size%==0 (
cd %1
java A < %ad%/inp.txt > %ad%/output.txt
cd..
cd..
cd..
fc output.txt outputreal.txt > res.txt
) else type com.txt
exit

:filesize
	set size=%~z1
	exit /b 0	