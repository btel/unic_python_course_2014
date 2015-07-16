#!/usr/bin/env python
#coding=utf-8

import glob
import os

lgn_sessions = ['data/lgn_session_{}.txt'.format(i) for i in range(5)]
v1_sessions = ['data/v1_session_{}.txt'.format(i) for i in range(5)]

data_files = lgn_sessions + v1_sessions

lgn_results = [os.path.join('results', os.path.split(p)[-1]) + '.npz' 
               for p in lgn_sessions]

v1_results = [os.path.join('results', os.path.split(p)[-1]) + '.npz' 
               for p in v1_sessions]

correlation_files = lgn_results + v1_results

def task_analysis():

    for inp, out in zip(data_files, correlation_files):
        yield {
            'actions' : ['python calculate_correlations.py {} --save {}'.format(inp, out)],
            'file_dep' : [inp, 'calculate_correlations.py'],
            'targets' : [out],
            'name' :  inp
            }

def task_merge_lgn_data():
    return {
         'actions' : ['python merge_correlations.py {} --save %(targets)s'.format(' '.join(lgn_results))],
         'file_dep' : ['merge_correlations.py'] + lgn_results,
         'targets' : ['results/lgn_pooled_correlations.npz']
         }

def task_merge_v1_data():
    return {
         'actions' : ['python merge_correlations.py {} --save %(targets)s'.format(' '.join(v1_results))],
         'file_dep' : ['merge_correlations.py'] + v1_results,
         'targets' : ['results/v1_pooled_correlations.npz']
         }

def task_make_plot():
    return {
         'actions' : ['python plot_corr_coef.py %(dependencies)s --save-fig %(targets)s'],
         'file_dep' : ['results/v1_pooled_correlations.npz',
                       'results/lgn_pooled_correlations.npz'],
         'targets' : ['figures/correlation_plot.svg']
        }
