# coding:utf-8

import numpy as np

from collections import defaultdict


class KnnAlgo(object):
    """
    @sample_file, feat1, feat2, feat3, label
    """
    def __init__(self, sample_file, sep=','):
        self.sample_file = sample_file
        self.sep = sep

        self.__read_sample()
        
    def __read_sample(self):
        with open(self.sample_file, "rb") as fid:
            self.sample = np.fromfile(fid, sep=self.sep)

    def dist_euclid(self):
        pass
    
    def dist_jaccard(self):
        pass

    def dist_consine(self):
        pass  

    def knn(self, K):
        pass

