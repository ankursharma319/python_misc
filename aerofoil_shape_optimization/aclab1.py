# -*- coding: utf-8 -*-
"""
Created on Mon Feb 08 18:17:34 2016

@author: as3g15
"""

import numpy as np
import pylab as pl

def choose(n, k):
    if 0 <= k <= n:
        p = 1
        for t in range(0,min(k, n - k),1):
            p = (p * (n - t)) // (t + 1)
        return p
    else:
        return 0

def b(i, n, t):
    return choose(n, i) * (t**i) * ((1.0-t)**(n-i))


def custom_sum(param_t, control_points):
    n = len(control_points)
    ar = np.zeros([1, 2])
    for i in range(0, n):
        h = control_points[i] * b(i, n-1, param_t)
        ar = ar + h
    return ar

def custom_sum_2(param_t, control_points, weights):
    n = len(control_points)
    ar = np.zeros([1, 2])
    for i in range(0, n):
        h = weights[i]*control_points[i] * b(i, n-1, param_t)
        ar = ar + h
    return ar

def custom_sum_3(param_t, weights):
    n = len(weights)
    ar = 0.0
    for i in range(0, n):
        h = weights[i] * b(i, n-1, param_t)
        ar = ar + h
    return ar

def bezier(points):
    t = np.linspace(0, 1, 101)
    c = np.zeros([101, 2])
    for g in range(0, len(t)):
        c[g, :] = custom_sum(t[g], points)
    pl.plot(points[:, 0], points[:, 1], "ko")
    pl.plot(points[:, 0], points[:, 1], "k-")
    pl.plot(c[:, 0], c[:, 1], "b-")
    return c

def rational_bezier(points, weights):
    t = np.linspace(0, 1, 101)
    c = np.zeros([101, 2])
    for g in range(0, len(t)):
        c[g, :] = custom_sum_2(t[g], points, weights)/custom_sum_3(t[g], weights)
    pl.plot(points[:, 0], points[:, 1], "ko")
    pl.plot(points[:, 0], points[:, 1], "k-")
    pl.plot(c[:, 0], c[:, 1], "-")
    return c

pts = np.array([[0, 0], [1, 0.5], [0.5, 1], [0.5, 2], [0, 1.5]])
wts = np.array([1,10,5,15,1])
#bezier(pts)
rational_bezier(pts, wts)