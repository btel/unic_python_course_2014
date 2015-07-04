
# coding: utf-8

# In[1]:

import numpy as np
from quantities import ms, Hz

from elephant.spike_train_generation import homogeneous_gamma_process


import neo 

def generate_correlated_spike_trains(corr_coef, fr, tmax, n_cells=10, gamma_a=2.):
    mother_spike_train = homogeneous_gamma_process(gamma_a, fr, 0*ms, tmax)
    spiketrains = [homogeneous_gamma_process(gamma_a, fr, 0*ms, tmax)
               for i in range(n_cells)]
    for st in spiketrains:
        n = min(len(mother_spike_train), len(st))
        exchange = np.random.rand(n) < corr_coef
        st[:n][exchange] = mother_spike_train[:n][exchange]
        st.sort()
    return spiketrains

def save_sessions(fname, corr_coef, n_sessions=5):

    for i in range(n_sessions):
        r = neo.AsciiSpikeTrainIO(filename=fname.format(i))
        spiketrains = generate_correlated_spike_trains(corr_coef, 50 * Hz, 1000 * ms, 10)
        seg = neo.Segment()
        seg.spiketrains = spiketrains
        r.write_segment(seg)
        
save_sessions('data/v1_session_{}.txt', 0.2)
save_sessions('data/lgn_session_{}.txt', 0.)
