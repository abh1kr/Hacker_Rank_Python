@echo off
cd /d "%~dp0"

echo === Pushing all changes to GitHub ===
echo.

git add .

for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set "stamp=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%"

git commit -m "Update solutions (%stamp%)"
git push origin main

echo.
echo === Done. Press any key to close. ===
pause >nul
