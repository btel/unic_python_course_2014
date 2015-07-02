#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import neo
from quantities import ms

from elephant.spike_train_correlation import corrcoef
from elephant.conversion import BinnedSpikeTrain

data = neo.AsciiSpikeTrainIO(filename='data/v1_session_0.txt')

seg = data.read_segment()
spiketrains = seg.spiketrains

binned = BinnedSpikeTrain(spiketrains, binsize=5 * ms)

corr_matrix = corrcoef(binned)

corr_coefs = np.triu(corr_matrix, 1)
corr_coefs = corr_coefs[corr_coefs != 0]

plt.hist(corr_coefs, 10)
plt.xlabel('correlation coefficient')
plt.ylabel('number of pairs')

plt.show()