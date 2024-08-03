#!/usr/bin/env python3
import os
import sys
import argparse


def normed_path(path: str):
	return os.path.abspath(path).replace('\\', '/')


_dirname_ = normed_path(os.path.dirname(__file__))


class CppEnvironmentBuilder:

	_templates_dir = f'{_dirname_}/templates'

	@classmethod
	def _build_parser(cls) -> argparse.ArgumentParser:
		parser = argparse.ArgumentParser()
		parser.add_argument('qt_base_dir')
		parser.add_argument('pyside6_version')
		parser.add_argument('qt_target')
		parser.add_argument('qtads_version')
		return parser

	@property
	def cmake_prefix_path(self) -> str:
		return normed_path(f'{self.options.qt_base_dir}/{self.options.pyside6_version}/{self.options.qt_target}')

	def __init__(self, ):
		parser = self._build_parser()
		self.options = parser.parse_args()

	def _render_template(self, filename: str, **context):
		with open(f'{self._templates_dir}/{filename}', encoding='utf-8') as fd_template:
			template_content = fd_template.read()
			with open(filename, 'w', encoding='utf-8') as fd_destination:
				fd_destination.write(template_content % context)

	def build_setup_cfg_file(self):
		self._render_template('setup.cfg', qtads_version=self.options.qtads_version)

	def build_cmake_lists_file(self):
		self._render_template('CMakeLists.txt', cmake_prefix_path=self.cmake_prefix_path)

	def build_toml_project_file(self):
		self._render_template('pyproject.toml', pyside6_version=self.options.pyside6_version)

	def build(self) -> int:
		try:
			rc = 0
			self.build_setup_cfg_file()
			self.build_cmake_lists_file()
			self.build_toml_project_file()
		except Exception as error:
			rc = -1
			print('Error while building C++ Environment', error)
		return rc


if __name__ == '__main__':
	builder = CppEnvironmentBuilder()
	sys.exit(builder.build())
