#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import fnmatch
import os


def is_package(path):
    is_svn_dir = fnmatch.fnmatch(path, '*/.svn*')
    is_test_module = fnmatch.fnmatch(path, '*tests')
    return not (is_svn_dir or is_test_module)

packages = [p for p, _, _ in os.walk('xivo_confgen') if is_package(p)]


setup(
    name='xivo-confgend-client',
    version='0.1',
    description='XIVO Configurations Generator client',
    author='Avencall',
    author_email='xivo-dev@lists.proformatique.com',
    url='http://www.xivo.io/',
    license='GPLv3',
    packages=packages,
    scripts=['bin/xivo-confgen'],
    data_files=[('/etc/xivo', ['etc/xivo-confgend-client/config.conf'])],
)
