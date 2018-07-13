# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:52:24 2015

@author: as3g15
"""


def eval_f(f, xs):
    """
    Takes a function f = f(x) and a list xs of values
    that should be used as arguments for f. The function
    eval_f applies the function f subsequently to
    every value x in xs, and returns a list fs of function values
    """
    l = []
    for x in xs:
        l.append(f(x))
    return l


def sum_f(f, xs):
    """
    Returns the sum of the function values of f evaluated
    at values x0, x1, x2, ..., xn where xs=[x0,x1,x2,...,xn]
    """
    sum = 0
    for x in xs:
        sum += f(x)
    return sum


def box_volume_UPS(a=13, b=11, c=2):
    """
    Returns the volume of a box with edge lengths a, b and c
    Inputs should be provided in inch, and the output is
    expressed in inch^3
    """
    return a * b * c
