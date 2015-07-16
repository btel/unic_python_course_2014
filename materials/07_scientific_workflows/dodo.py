#!/usr/bin/env python
#coding=utf-8

import glob
import os

data_files = glob.glob('data/*.txt')

def task_analysis():
    targets = [os.path.join('results', os.path.splitext(os.path.split(f)[1])[0]+'.npz')
               for f in data_files]

    for inp, out in zip(data_files, targets):
        yield {
            'actions' : ['python calculate_correlations.py {} --save {}'.format(inp, out)],
            'file_dep' : [inp],
            'targets' : [out],
            'name' : 'analysis_' + inp
            }

def task_merge_lgn_data():
    input_file = ['results/lgn_session_{}.npz'.format(i) for i in range(5)]
    return {
         'actions' : ['python merge_correlations.py %(dependencies)s --save %(targets)s'],
         'file_dep' : input_file,
         'targets' : ['results/lgn_pooled_correlations.npz']
         }

def task_merge_v1_data():
    input_file = ['results/v1_session_{}.npz'.format(i) for i in range(5)]
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
         
