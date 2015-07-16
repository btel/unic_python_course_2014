#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import subprocess

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('spike_files', nargs='+')
args = parser.parse_args()

for path in args.spike_files:
    _, filename = os.path.split(path)
    filename, ext = os.path.splitext(filename)

    out_filename = os.path.join('results', filename + '.npz')
    cmd = 'python calculate_correlations.py {} --save {}'.format(path, out_filename)
    subprocess.call(cmd, shell=True)
