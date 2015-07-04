#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('corr_file')
args = parser.parse_args()

data = np.load(args.corr_file)
corr_coefs = data['corr_coefs']

plt.hist(corr_coefs, 10)

plt.xlabel('correlation coefficient')
plt.ylabel('number of pairs')

plt.show()
