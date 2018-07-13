# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:21:31 2015

@author: Ankur Sharma
"""


def box_volume(a, b, c):
    """Returns volume of cuboid with side lengths a, b and c"""
    return a*b*c


def fall_time(h):
    """Returns time needed for an object to fall height h (no resistance)"""
    return ((h*2)/(9.81))**0.5


def interval_point(a, b, x):
    """Returns how far to go towards b, starting at a, with x as the
    fraction between 0 and 1 showing the weightage towards b"""
    return a + (b-a)*x


def impact_velocity(h):
    """returns the velocity (in metre per second) with which an object falling
    from a height of h meters will hit the ground"""
    return fall_time(h)*9.81


def signum(x):
    """returns 1 if arguement x>0, -1 id x<0 and 0 if x=0"""
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1
