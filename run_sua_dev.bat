@echo off

rem ----------------------------------------------------------------------------
rem
rem run_sua.bat: Process SUA tasks.
rem
rem ----------------------------------------------------------------------------

setlocal EnableDelayedExpansion

set ERRORLEVEL=

if ["!ENV_FOR_DYNACONF!"] EQU [""] (
    set ENV_FOR_DYNACONF=dev
)
set PYTHONPATH=

echo.
echo Script %0 is now running

if exist logging_sua.log (
    del /f /q logging_sua.log
)

echo =======================================================================
echo Start %0
echo -----------------------------------------------------------------------
echo SUA - Template Library.
echo -----------------------------------------------------------------------
echo ENVIRONMENT_TYPE : %ENV_FOR_DYNACONF%
echo PYTHONPATH       : %PYTHONPATH%
echo -----------------------------------------------------------------------
echo:| TIME
echo =======================================================================

pipenv run python src\launcher.py
if ERRORLEVEL 1 (
    echo Processing of the script: %0 - step: 'python src\launcher.py was aborted
)

echo.
echo -----------------------------------------------------------------------
echo:| TIME
echo -----------------------------------------------------------------------
echo End   %0
echo =======================================================================
