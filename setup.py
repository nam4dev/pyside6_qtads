#!/usr/bin/env python3
import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List

import cmake_build_extension
import setuptools
from wheel.bdist_wheel import bdist_wheel


if os.environ.get('PYSIDE6_QTADS_NO_HARD_PYSIDE_REQUIREMENT') == '1':
    install_requirements = [
        'PySide6-Essentials', 'shiboken6'
    ]
else:
    version = os.environ.get('PYSIDE_VERSION')
    install_requirements = [
        f'PySide6=={version}',
        f'PySide6-Addons=={version}',
        f'PySide6-Essentials=={version}',
        f'shiboken6=={version}'
    ]


class qtads_bdist_wheel(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.11+
            return "cp311", "abi3", plat

        return python, abi, plat

    # def run_command(self, command: str):
    #     super().run_command(command)
    #     if command == 'install':
    #         try:
    #             self._generate_pyi_support()
    #         except Exception as error:
    #             print(f'generate_pyi_support -> ERROR -> {error}')
    #
    # @classmethod
    # def _generate_pyi_support(cls) -> None:
    #     options = argparse.Namespace(modules=['PySide6QtAds'])
    #
    #     logging.basicConfig(level=logging.INFO)
    #     logger = logging.getLogger("generate_pyi")
    #     outpath = './build/lib.win-amd64-cpython-311'
    #     if outpath and not Path(outpath).exists():
    #         os.makedirs(outpath)
    #         logger.info(f"+++ Created path {outpath}")
    #     options._pyside_call = True
    #     options.logger = logger
    #
    #     # now we can import
    #     global PySide6, inspect, typing, HintingEnumerator, build_brace_pattern
    #     import PySide6
    #     import PySide6QtAds
    #     from PySide6.support.signature.lib.enum_sig import HintingEnumerator
    #     from PySide6.support.signature.lib.tool import build_brace_pattern
    #     from PySide6.support.signature.lib.pyi_generator import generate_pyi
    #
    #     # propagate USE_PEP563 to the mapping module.
    #     # Perhaps this can be automated?
    #     PySide6.support.signature.mapping.USE_PEP563 = sys.version_info[:2] >= (3, 7)
    #
    #     outpath = Path(outpath) if outpath and os.fspath(outpath) else Path(PySide6QtAds.__file__).parent
    #     for mod_name in options.modules:
    #         import_name = mod_name
    #         if hasattr(sys, "pypy_version_info"):
    #             # PYSIDE-535: We cannot use __feature__ yet in PyPy
    #             generate_pyi(import_name, outpath, options)
    #         else:
    #             from PySide6.support import feature
    #             feature_id = feature.get_select_id(options.feature)
    #             with feature.force_selection(feature_id, import_name):
    #                 generate_pyi(import_name, outpath, options)


class CustomCMakeExtension(cmake_build_extension.CMakeExtension):
    """XXX: Override CMakeExtension to support extra kwargs"""
    def __init__(
            self,
            name: str,
            install_prefix: str = "",
            disable_editable: bool = False,
            write_top_level_init: str = None,
            cmake_configure_options: List[str] = (),
            source_dir: str = str(Path(".").absolute()),
            cmake_build_type: str = "Release",
            cmake_component: str = None,
            cmake_depends_on: List[str] = (),
            expose_binaries: List[str] = (),
            cmake_generator: str = "Ninja",
            **kwargs
    ):
        setuptools.Extension.__init__(self, name=name, sources=[], **kwargs)

        if not Path(source_dir).is_absolute():
            source_dir = str(Path(".").absolute() / source_dir)

        if not Path(source_dir).absolute().is_dir():
            raise ValueError(f"Directory '{source_dir}' does not exist")

        self.install_prefix = install_prefix
        self.cmake_build_type = cmake_build_type
        self.disable_editable = disable_editable
        self.write_top_level_init = write_top_level_init
        self.cmake_depends_on = cmake_depends_on
        self.source_dir = str(Path(source_dir).absolute())
        self.cmake_configure_options = cmake_configure_options
        self.cmake_component = cmake_component
        self.expose_binaries = expose_binaries
        self.cmake_generator = cmake_generator


init_py = Path("init.py").read_text()


class CustomBuildCommand(setuptools.Command):
    """A custom command that ensures that build_ext is executed before build_py."""

    description = 'Build package'
    user_options = []

    def finalize_options(self) -> None:
        pass

    def initialize_options(self) -> None:
        pass

    def run(self):
        self.run_command('install')
        p = subprocess.run(r"python "
                           r".\scripts\generate_pyi.py "
                           r"PySide6QtAds "
                           # r"--sys-path .\build\temp.win-amd64-cpython-311 "
                           r"--outpath .\build\lib.win-amd64-cpython-311", shell=True)
        # self.run_command('bdist_wheel')


setuptools.setup(
    ext_modules=[
        CustomCMakeExtension(
            name="PySide6-QtAds",
            install_prefix="PySide6QtAds",
            write_top_level_init=init_py,
            source_dir=str(Path(__file__).parent.absolute()),
            cmake_configure_options=[
                '-DCMAKE_C_FLAGS=-v',
                "-DBUILD_EXAMPLES:BOOL=OFF",
                "-DBUILD_STATIC:BOOL=ON",
                "-DADS_VERSION=4.3.0",
                f"-DPython3_ROOT_DIR={Path(sys.prefix)}"
            ],
            py_limited_api=True
        ),
    ],
    cmdclass=dict(
        build_all=CustomBuildCommand,
        build_ext=cmake_build_extension.BuildExtension,
        bdist_wheel=qtads_bdist_wheel
    ),
    install_requires=install_requirements,
)
