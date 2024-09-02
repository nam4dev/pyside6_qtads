#!/usr/bin/env bash

#export HTTP_PROXY=127.0.0.1:XXXX
#export HTTPS_PROXY=127.0.0.1:XXXX
#export FTP_PROXY=127.0.0.1:XXXX

export QT_TARGET=gcc_64
export QT_VERSION=6.6.3
export QT_BASE_DIR="${HOME}/dev/Qt"
export QT6_DIR="${QT_BASE_DIR}/${QT_VERSION}/${QT_TARGET}"

export PYSIDE_VERSION=${QT_VERSION}

export PIP_EXTRA_INDEX_URL=https://download.qt.io/official_releases/QtForPython/
export TRUSTED_HOSTS="--trusted-host pypi.python.org --trusted-host download.qt.io"

export PYSIDE6_QTADS_VERSION=4.3.0.3.dev0
export PYSIDE6_QTADS_NO_HARD_PYSIDE_REQUIREMENT="0"