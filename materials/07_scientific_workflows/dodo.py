#!/usr/bin/env python
#coding=utf-8

import glob
import os

def task_analysis():
    input_files = glob.glob('data/*.txt')
    targets = [os.path.join('results', os.path.splitext(os.path.split(f)[1])[0]+'.npz')
               for f in input_files]
    return {
        'actions' : ['python batch_correlation.py %(dependencies)s'],
        'file_dep' : input_files,
        'targets' : targets
        }

def task_merge_lgn_data():
    input_file = glob.glob('results/lgn_session*.npz')
    return {
         'actions' : ['python merge_correlations.py %(dependencies)s --save %(targets)s'],
         'file_dep' : input_file,
         'targets' : ['results/lgn_pooled_correlations.npz']
         }

def task_merge_v1_data():
    input_file = glob.glob('results/v1_session*.npz')
    return {
         'actions' : ['python merge_correlations.py %(dependencies)s --save %(targets)s'],
         'file_dep' : input_file,
         'targets' : ['results/v1_pooled_correlations.npz']
         }

def task_make_plot():
    return {
         'actions' : ['python plot_corr_coef.py %(dependencies)s --save-fig %(targets)s'],
         'file_dep' : ['results/v1_pooled_correlations.npz',
                       'results/lgn_pooled_correlations.npz'],
         'targets' : ['results/correlation_plot.png']
         }
