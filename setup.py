#!/usr/bin/env python3
# encoding: utf-8

import os.path

import pkg_resources
import setuptools

actual_pip_version = pkg_resources.get_distribution('pip').parsed_version
# this class recently moved packages
Version = type(actual_pip_version)
required_pip_version = Version('18.1')

if actual_pip_version < required_pip_version:
	raise RuntimeError(f'pip >= {required_pip_version} required')

setuptools.setup(
	name='simple_help_formatter',
	version='0.0.1',

	py_modules=['simple_help_formatter'],

	install_requires=[
		'discord.py @ git+https://github.com/Rapptz/discord.py@rewrite'])
