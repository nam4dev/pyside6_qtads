@echo off

cd %USERPROFILE%\dev\src\pyside6_qtads\build_bindings || exit
CALL .\windows\setup-vars.bat

CALL %USERPROFILE%\dev\virtualenv\pyside6_qtads\Scripts\activate
python --version

python -m build --wheel %USERPROFILE%\dev\src\pyside6_qtads
python -m pip install --force-reinstall %USERPROFILE%\dev\src\pyside6_qtads\dist\PySide6_QtAds-%PYSIDE6_QTADS_VERSION%-cp311-abi3-win_amd64.whl

cd %USERPROFILE%\dev\src\pyside6_qtads\Qt-Advanced-Docking-System\examples\autohide || exit
python main.py