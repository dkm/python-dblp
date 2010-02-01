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

import dblp
import sys
import optparse

def main(argv):
    parser = optparse.OptionParser(
        usage='Usage: %prog [options]',
        description="Simple DBLP cli")
    
    parser.add_option('-a', '--author-name',
                      help="Author name")
    parser.add_option('-p', '--parser-friendly',
                      help="Enable the parser friendly output",
                      action="store_true", default=False)
    parser.add_option('-o', '--output',
                      help="Output file")

    (options, args) = parser.parse_args(argv[1:])
    
    if options.author_name == None:
        print "Missing author..."
        parser.print_help()
        sys.exit(-1)

    out_file = sys.stdout
    if options.output != None:
        out_file = open(options.output, "w")

    correct_match, res = dblp.simple_author_search(options.author_name)

    if correct_match:
        if options.parser_friendly:
            print >> out_file, "1"
        for bib in res.values():
            print >> out_file, bib
    else:
        if options.parser_friendly:
            print >> out_file, "0"
        else:
            print >> out_file, "There is more than one author with the name '%s', " %options.author_name,
            print >> out_file, "please refine your request:"
        print >> out_file, "\n".join(res)
    
    
if __name__ == '__main__':
    main(sys.argv)
