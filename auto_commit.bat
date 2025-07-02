@echo off
setlocal enabledelayedexpansion

REM Obtenir la date au format YYYY-MM-DD
for /f "tokens=2 delims==" %%G in ('wmic os get localdatetime /value') do set datetime=%%G
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set today=%year%-%month%-%day%

REM Obtenir la branche actuelle
for /f "delims=" %%a in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%a

REM Demander à l'utilisateur une branche (optionnel)
set /p branch_name=Branche de push [%current_branch%] : 
if "%branch_name%"=="" set branch_name=%current_branch%

REM Demander un message de commit
set /p message=Que fait cette version ? : 

REM Ajouter la date au message
set "full_message=%today% %message%"

REM Étapes Git
git add .
git commit -m "%full_message%"
git tag "%full_message%"
git push origin %branch_name%
git push origin --tags

echo ✅ Commit envoyé sur [%branch_name%] avec le tag : "%full_message%"
pause