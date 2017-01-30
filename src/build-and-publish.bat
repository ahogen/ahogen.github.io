ECHO OFF
SET destDir=..
SET srcDir=./public


hugo --cleanDestinationDir 

for /d /r "%srcDir%" %%i in (*) do if exist "%destDir%\%%~ni" (dir "%%i" | find "0 File(s)" > NUL & if errorlevel 1 move /y "%%i\*.*" "%destDir%\%%~ni") else (move /y "%%i" "%destDir%")

move /y %srcDir%\*.* %destDir%

rd /s /q %srcDir%