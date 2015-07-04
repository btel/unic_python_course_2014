#!/usr/bin/env python
#coding=utf-8

import glob

def task_v1_analysis():
    input_files = glob.glob('data/v1_session_*.txt')
    return {
        'actions' : ['python batch_correlation.py %(dependencies)s --save %(targets)s'],
        'file_dep' : input_files,
        'targets' : ['results/v1_pooled_correlations.npz']
        }

def task_lgn_analysis():
    input_files = glob.glob('data/lgn_session_*.txt')
    return {
         'actions' : ['python batch_correlation.py %(dependencies)s --save %(targets)s'],
         'file_dep' : input_files,
         'targets' : ['results/lgn_pooled_correlations.npz']
         }

def task_make_plot():
    return {
         'actions' : ['python plot_corr_coef.py %(dependencies)s --save-fig %(targets)s'],
         'file_dep' : ['results/v1_pooled_correlations.npz',
                       'results/lgn_pooled_correlations.npz'],
         'targets' : ['results/correlation_plot.png']
         }
