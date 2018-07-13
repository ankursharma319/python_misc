# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:32:48 2015

@author: as3g15
"""

import math


def swing_time(L):
    """returns the time T [in seconds] needed for an idealized pendulum
    of length L [in meters] to complete a single oscillation"""
    return 2.0 * math.pi * ((L / 9.81) ** 0.5)


def range_squared(n):
    """Takes an non-negative integer value n and
    returns that returns the list
    [0, 1, 4, 9, 16, 25, ..., (n-1)^2"""
    l = []
    for i in range(n):
        l.append(i**2)
    return l


def count(element, seq):
    """counts how often the given element element occurs in the
    given sequence seq, and returns this integer value"""
    c = 0
    for e in seq:
        if e == element:
            c = c + 1
    return c
