#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('spike_files', nargs='+')
    parser.add_argument('--save')
    args = parser.parse_args()

    pooled_data = []
    for path in args.spike_files:
        corr_coef = np.load(path)
        pooled_data.append(corr_coef['corr_coefs'])

    pooled_data = np.concatenate(pooled_data)

    np.savez(args.save, corr_coefs=pooled_data)
