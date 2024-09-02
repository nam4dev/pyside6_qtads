#!/usr/bin/env bash

cd "${HOME}/dev/src/pyside6_qtads/build_bindings" || exit

source ./linux/setup-vars.sh

source "${HOME}/dev/virtualenv/pyside6_qtads/bin/activate"
python --version

python -m build --wheel "${HOME}/dev/src/pyside6_qtads"
python -m pip install --force-reinstall "${HOME}/dev/src/pyside6_qtads/dist/PySide6_QtAds-${PYSIDE6_QTADS_VERSION}-cp311-abi3-linux_x86_64.whl"

cd "${HOME}/dev/src/pyside6_qtads/Qt-Advanced-Docking-System/examples/autohide" || exit
python main.py