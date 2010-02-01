#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 Marc Poulhiès
#
# Python module for DBLP
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-dblp.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup

setup (
    name = "python-dblp",
    description = "DBLP python module",
    long_description = """
This package provides a python module for interacting with DBLP. It
also comes with a frontend script
""",
    version = "0.1",
    author = 'Marc Poulhiès',
    author_email = 'dkm@kataplop.net',
    url = "http://github.com/dkm/python-dblp",
    maintainer = 'Marc Poulhiès',
    maintainer_email = 'dkm@kataplop.net',
    license = "GPL",
    packages = ['dblp'],
    scripts=['bin/dblp-request.py'],
    )

