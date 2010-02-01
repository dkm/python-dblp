#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 Marc Poulhiès
#
# Python module for DBLP
#
# Plopifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-dblp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-dblp.  If not, see <http://www.gnu.org/licenses/>.

import urllib
from BeautifulSoup import BeautifulSoup

import pycurl
import re
import StringIO

SIMPLE_AUTHOR_SEARCH_URL="http://dblp.uni-trier.de/search/author"
USER_AGENT="DBLP python module"

bibtex_re = re.compile('(?P<url>http://dblp\.uni-trier\.de/rec/bibtex/[^".]*)"')

class CurlAnswer:

    def __init__(self):
        self.data = ''

    def write_callback(self, buf):
        self.data += buf

    def get_stringio(self):
        sio = StringIO.StringIO()
        sio.write(self.data)
        sio.seek(0)
        return sio

    def __str__(self):
        return self.data
        
def do_post_request(url, args):
    ans = CurlAnswer()
    
    _args = [(k,str(v)) for (k,v) in args.items()]
    c = pycurl.Curl()
    c.setopt(c.POST, 1)
    c.setopt(c.URL, url)
    c.setopt(c.HTTPPOST, _args)

    c.setopt(c.WRITEFUNCTION, ans.write_callback)
    
    c.perform()
    c.close()
    return ans

def do_complex_get_request(url, args):
    ans = CurlAnswer()
    _args = [(k,str(v)) for (k,v) in args.items()]
    _args = urllib.urlencode(_args)

    url += "?" + _args

    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.FOLLOWLOCATION, 1)
    c.setopt(c.HTTPGET, 1)

    c.setopt(c.WRITEFUNCTION, ans.write_callback)
    
    c.perform()
    c.close()
    return ans

def do_simple_request(url):
    ans = CurlAnswer()
    c = pycurl.Curl()
    c.setopt(pycurl.USERAGENT, USER_AGENT)
    c.setopt(c.URL, url)

    c.setopt(c.WRITEFUNCTION, ans.write_callback)
    c.perform()
    c.close()
    return ans


def extract_bibtex(url):
    ans = do_simple_request(str(url))
    soup = BeautifulSoup(str(ans))
    r = soup.findAll('pre')
    
    ## DBLP adds an HTML link in the bibtex. Rip it off
    a = r[0].contents[1]
    a.replaceWith(a.string)
    return "".join(r[0].contents)
    


def simple_author_search(author, get=True):
    args = {'author': author }
    ans = do_complex_get_request(SIMPLE_AUTHOR_SEARCH_URL, args)
    bibtex = {}

    soup = BeautifulSoup(str(ans))
    r = soup.findAll('a', attrs={'name': re.compile("^p[0-9]+$")})
    for a in r:
        url = a['href']
        key = url.split('/')[-1]
        if get:
            bibtex[key] = extract_bibtex(a['href'])
        else:
            bibtex[key] = url

    return bibtex
