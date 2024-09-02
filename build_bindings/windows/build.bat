@echo off

cd %USERPROFILE%\dev\src\pyside6_qtads\build_bindings || exit
CALL .\windows\setup.bat

cd %USERPROFILE%\dev\src\pyside6_qtads\build_bindings || exit
CALL .\windows\build-no-setup.bat