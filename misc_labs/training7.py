# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:19:31 2015

@author: as3g15
"""


def count_chars(s):
    """
    Takes a string s and returns a dictionary.
    The dictionary's keys are the set of characters
    that occur in string s. The value for each key is
    the number of times that this character occurs in
    the string s
    """
    dic = {}
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic


def derivative(f, x, eps=1e-6):
    """
    which computes a numerical approximation of the first
    derivative of the function f(x) using central differences.
    The value that the function returns is derivative
    """
    return (f(x + eps/2)-f(x - eps/2))/eps


def f(x):
    return x**2
