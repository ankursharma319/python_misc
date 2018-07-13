# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:46:25 2015

@author: Akhil
"""


def seconds2days(n):
    """accepts a number of seconds (either as int or float) and returns the
    number of days in those seconds as float"""
    secondsin1day = 24*60*60.0
    return n/secondsin1day


def box_surface(a, b, c):
    """computes and returns the surface area of a box (i.e. cuboid)
    with edge lengths a, b, and c"""
    return 2*((a*b)+(a*c)+(b*c))


def triangle_area(a, b, c):
    """ returns the area of a triangle with lengths a, b and c"""
    s = (a + b + c) / 2
    Asquared = s*(s-a)*(s-b)*(s-c)
    return Asquared**0.5
