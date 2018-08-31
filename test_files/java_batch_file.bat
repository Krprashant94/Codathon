@echo off
set size=0
break > output.txt
set ad=%cd%
javac %1/%2 2> com.txt
call :filesize "com.txt"
if %size%==0 call :op %1 "%ad%" %3 
if not %size%==0 type com.txt
goto :eof

:filesize
	set size=%~z1	
	goto :eof

:op
	cd %1
	java %3 < %2/inp.txt > %2/output.txt
	cd %2
	fc output.txt outputreal.txt > res.txt
	type output.txt
	goto :eof