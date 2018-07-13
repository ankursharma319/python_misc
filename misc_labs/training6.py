# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def positive_places(f, xs):
    """
    Takes as arguments some function f and a list of numbers
    xs and returns a list of those-and-only-those elements x of xs
    for which f(x) is strictly greater than zero
    """
    l = []
    for x in xs:
        if f(x) > 0:
            l.append(x)
    return l


def eval_f_0123(f):
    """
    that evaluates the function f=f(x) at positions
    x=0, x=1, x=2 and x=3. The function returns
    the list [f(0), f(1), f(2), f(3)]
    """
    return [f(0), f(1), f(2), f(3)]
