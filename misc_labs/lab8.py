# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 11:32:15 2015

@author: Ankur
"""


import math
import pylab
from scipy.optimize import brentq


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


def f1minusf2(x):
    return f1(x)-f2(x)


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


def create_plot_data(f, xmin, xmax, n):
    """
    Returns a tuple (xs, ys) where xs and ys are two sequences,
    each containing n numbers
    """
    if n >= 2:
        def xi(i):
            return xmin + i*(xmax-xmin)/(n-1.0)
        xs = [xi(i) for i in range(n)]
        ys = [f(x) for x in xs]
        return (xs, ys)
    else:
        return "n less than 2"


def myplot():
    """
    computes f1(x) and plots f1(x) using 1001 points for
    x ranging from -2 to +2. The function returns None.
    """
    plotData = create_plot_data(f1, -2, 2, 1001)
    pylab.plot(plotData[0], plotData[1], label="f1")
    plotData = create_plot_data(f2, -2, 2, 1001)
    pylab.plot(plotData[0], plotData[1], label="f2")
    pylab.xlabel('x')
    pylab.ylabel('y(x)')
    pylab.legend(loc="upper left")
    pylab.savefig("plot.png")
    pylab.savefig("plot.pdf")
    pylab.show()
    return None


def find_cross():
    """
    Returns the value x (approximately) for which
    f1(x) = cos(2 * pi * x) * exp(-x * x) and f2(x) = log(x + 2.2)
    have the same value.
    We are only interested in the solution where x > 0
    """
    return brentq(f1minusf2, a=0, b=0.5)
