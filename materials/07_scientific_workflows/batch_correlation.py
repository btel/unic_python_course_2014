#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import subprocess

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('spike_files', nargs='+')
parser.add_argument('--save')
args = parser.parse_args()

pooled_data = []
for path in args.spike_files:
    _, filename = os.path.split(path)

    out_filename = os.path.join('results', filename + '.npz')
    cmd = 'python calculate_correlations.py {} --save {}'.format(path, out_filename)
    subprocess.call(cmd, shell=True)
    corr_coef = np.load(out_filename)
    pooled_data.append(corr_coef['corr_coefs'])

pooled_data = np.concatenate(pooled_data)

np.savez(args.save, corr_coefs=pooled_data)
