@echo off
setlocal

REM Obtenir la date au format AAAA-MM-JJ depuis PowerShell
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set today=%%i

REM Récupérer le nom de la branche actuelle
for /f "tokens=*" %%a in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%a

REM Demander le nom de la branche (valeur par défaut = branche actuelle)
set /p branch_name="Branch to push to [%current_branch%]: "
if "%branch_name%"=="" set branch_name=%current_branch%

REM Demander un message de commit
set /p message="What is this version about? "

REM Préparer le message complet avec la date
set full_message=%today% %message%

REM Remplacer les espaces pour le nom de tag
set tag_name=%full_message: =_%

REM Étapes Git
git add .
git commit -m "%full_message%"
git tag "%tag_name%"
git push origin %branch_name%
git push origin --tags

echo Done! Committed to [%branch_name%] with tag: "%tag_name%"
pause
