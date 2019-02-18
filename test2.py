#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:09:52 2019

@author: asanka
"""

from emvincelib import stat
import numpy as np

###############################################################################

#x = [2,4,6,8,10,12,13,15]
#y = [1,2,3,4,6,7,8,9]

#r = stat.getCorrelationCoefficient(x, y)
#print(r)

#mean, confidence90 = stat.getMeasurement90Confidence(x)
#print("%d +/- %f (90%% confidence interval)" % (mean, confidence90))
#mean, confidence90 = stat.getRepeatedMeasurements90Confidence(x)
#print("Mean: %d +/- %f (90%% confidence interval)" % (mean, confidence90))
#mean, confidence95 = stat.getMeasurement95Confidence(x)
#print("%d +/- %f (95%% confidence interval)" % (mean, confidence95))
#mean, confidence95 = stat.getRepeatedMeasurements95Confidence(x)
#print("Mean: %d +/- %f (95%% confidence interval)" % (mean, confidence95))
#mean, confidence99 = stat.getMeasurement99Confidence(x)
#print("%d +/- %f (99%% confidence interval)" % (mean, confidence99))
#mean, confidence99 = stat.getRepeatedMeasurements99Confidence(x)
#print("Mean: %d +/- %f (99%% confidence interval)" % (mean, confidence99))

###############################################################################
#a = [0.9, 1.0, 1.1, 1.2]
#b = [0.8, 0.9, 1.0, 1.1]
#c = [4.9, 5.0, 5.1, 5.2]

#pValue = stat.getPvalue_twoSampledTtest(a, b)
#print("p-value (between a and b) = %f" % pValue)

#pValue = stat.getPvalue_twoSampledTtest(a, c)
#print("p-value (between a and c) = %f" % pValue)

#pValue = stat.getPvalue_twoSampledTtest(b, c)
#print("p-value (between b and c) = %f" % pValue)

###############################################################################

sampleData = np.random.normal(loc=8.0, scale=2.0, size=20)
sampleData = sampleData.tolist()
expectedPopulationMean = 8.0
pValue = stat.getPvalue_oneSampledTtest(sampleData, expectedPopulationMean)
print("p-value = %f" % pValue)

