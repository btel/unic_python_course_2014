#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

import argparse
from itertools import cycle

parser = argparse.ArgumentParser()
parser.add_argument('corr_file', nargs='+')
parser.add_argument('--save-fig')
args = parser.parse_args()
bin_width = 0.02

colors = cycle(['r', 'b'])
bins = np.arange(-1, 1, bin_width)
for filename in args.corr_file:

    data = np.load(filename)
    corr_coefs = data['corr_coefs']

    n, _ = np.histogram(corr_coefs,  bins)
    plt.bar(bins[:-1], n, bin_width, fc=colors.next())

plt.xlabel('correlation coefficient')
plt.ylabel('number of pairs')

if args.save_fig:
    plt.savefig(args.save_fig)
else:
    plt.show()
