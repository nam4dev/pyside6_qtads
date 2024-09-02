@echo off

@REM set HTTP_PROXY=127.0.0.1:XXXX
@REM set HTTPS_PROXY=127.0.0.1:XXXX
@REM set FTP_PROXY=127.0.0.1:XXXX

set QT_TARGET=msvc2019_64
set QT_VERSION=6.7.2
set QT_BASE_DIR=%USERPROFILE%\dev\Qt
set QT6_DIR=%QT_BASE_DIR%\%QT_VERSION%\%QT_TARGET%

set PYSIDE_VERSION=%QT_VERSION%

set PIP_EXTRA_INDEX_URL=https://download.qt.io/official_releases/QtForPython/
set TRUSTED_HOSTS=--trusted-host pypi.python.org --trusted-host download.qt.io

set PYSIDE6_QTADS_VERSION=4.3.0.3.dev0
set PYSIDE6_QTADS_NO_HARD_PYSIDE_REQUIREMENT="0"