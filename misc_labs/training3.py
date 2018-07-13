# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:46:34 2015

@author: as3g15
"""

import math


def degree(x):
    """Returns x radians converted into degrees"""
    return x*(180.0/math.pi)


def min_max(xs):
    """Returns a tuple consisiting of xmin and xmax
    in the list xs"""
    return min(xs), max(xs)


def geometric_mean(xs):
    """Returns the geomatric mean of numbers in list xs"""
    p = 1.0
    for num in xs:
        p = p * num
    return (p)**(1.0/len(xs))
