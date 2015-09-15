#!/usr/bin/python
__author__ = 'micha'

import sys
import os.path
from glob import glob

input_dir = "/home/micha/documents/latex/master_thesis/thesis/compile/"
output_dir = "/home/micha/documents/latex/master_thesis/thesis/sections/"

all_names = ["exp", "analysis", 'cms', 'motivation', 'data_acquisition', 'telescope', 'theory', 'setup']

userin = str(sys.argv[1])

in_filename = input_dir + userin
out_filename = output_dir + userin

def convert(infile, outfile):
    f = None
    if os.path.exists(infile):
        f = open(infile, 'r')
    else:
        print 'input filename does not exist. exit'
        exit(-1)

    data = []
    found_start = False

    for line in f:
        if line.startswith("\end{document}") or line.startswith("\chapter{bla}") or line.startswith("% TO GET IT COMP"):
            break
        elif line.startswith("\\begin{document}"):
            found_start = True
        elif line.startswith("\chapter{") or line.startswith("\\tableofcontents"):
            continue
        elif found_start:
            data.append(line)

    f.close()

    f = open(outfile, 'w')
    for i in data:
        if len(i) > 2:
            f.write(i)
    f.close()

if userin == 'all':
    for name in glob(input_dir + '*.tex'):
        in_filename = name
        out_filename = output_dir + name.split('/')[-1]
        convert(in_filename, out_filename)
else:
    convert(in_filename, out_filename)