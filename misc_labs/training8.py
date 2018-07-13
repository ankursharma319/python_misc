# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 11:32:39 2015

@author: Akhil
"""
import math


def f1(x):
    """
    accepts an number x as input and returns
    cos(2pi*x)*(e^(-x^2))
    """
    return math.cos(2*math.pi*x)*math.exp(-(x**2))


def f2(x):
    """
    accepts the number x as input and returns
    ln(x+2.2)
    """
    return math.log(x+2.2)


def positive_places(f, xs):
    """
    takes as arguments some function f and a list of numbers xs
    and returns a list of those-and-only-those elements x of xs
    for which f(x) is strictly greater than zero
    """
    return [f(x) for x in xs if f(x) > 0]


def reverse_dic(d):
    """
    takes a dictionary d as the input argument and returns a
    dictionary r. If the dictionary d has a key k and an associated
    value v, then the dictionary r should have a key v and a value k
    """
    n = {}
    for k in d.keys():
        n[d[k]] = k
    return n
