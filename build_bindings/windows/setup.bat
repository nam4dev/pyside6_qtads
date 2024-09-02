@echo off

cd %USERPROFILE%\dev\pyside6_qtads\build_bindings || exit
CALL .\windows\setup-vars.bat

CALL %USERPROFILE%\dev\venv\pyside6_qtads\Scripts\activate
python --version

python -m pip install --upgrade pip

python -m pip install -U aqtinstall auditwheel %TRUSTED_HOSTS%
python -m aqt install-qt windows desktop %QT_VERSION% win64_%QT_TARGET% --outputdir %QT_BASE_DIR%

cd %USERPROFILE%\dev\pyside6_qtads || exit

python .\scripts\build_cpp_environment.py %QT_BASE_DIR% %PYSIDE_VERSION% %QT_TARGET% %PYSIDE6_QTADS_VERSION%

python -m pip install -U build %TRUSTED_HOSTS%
python -m pip install -U wheel %TRUSTED_HOSTS%
python -m pip install -U setuptools>=45 %TRUSTED_HOSTS%
python -m pip install -U setuptools_scm[toml]>=6.0 %TRUSTED_HOSTS%
python -m pip install -U cmake_build_extension %TRUSTED_HOSTS%
python -m pip install -U PySide6==%PYSIDE_VERSION% %TRUSTED_HOSTS%
python -m pip install -U PySide6_Addons==%PYSIDE_VERSION% %TRUSTED_HOSTS%
python -m pip install -U PySide6_Essentials==%PYSIDE_VERSION% %TRUSTED_HOSTS%
python -m pip install -U shiboken6==%PYSIDE_VERSION% %TRUSTED_HOSTS%
python -m pip install -U shiboken6_generator==%PYSIDE_VERSION% %TRUSTED_HOSTS%