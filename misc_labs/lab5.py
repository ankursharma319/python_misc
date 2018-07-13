# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:03:57 2015

@author: Akhil
"""


def vector_product3(a, b):
    """
    return a list which contains the vector product of 3d-vectors a and b
    """
    # [ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx]
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def seq_mult_scalar(a, s):
    """
    takes a list of numbers a and a scalar (i.e. a number) s.
    For the input a=[a0, a1, a2,.., an] the function returns
    [s * a0, s * a1, s * a2, ..., s * an].
    """
    newS = []
    for element in a:
        newS.append(element*s)
    return newS


def powers(n, k):
    """
    Returns the list [1,n,n^2,n^3,...,n^k] where k is an integer.
    Note that there should be k+1 elements in the list
    """
    l = []
    if (k >= 0):
        for i in range(k+1):
            l.append(n**i)
    else:
        for i in range(abs(k)+1):
            l.append(n**(-i))
    return l


def traffic_light(load):
    """
    Takes a floating point number load. The function returns the string:

        green for values of load below 0.7.
        amber for values of load equal to or greater than
        0.7 but smaller than 0.9
        red for values of load equal to 0.9 or greater than 0.9
    """
    if(load < 0.7):
        return "green"
    elif(load >= 0.7 and load < 0.9):
        return "amber"
    elif(load >= 0.9):
        return "red"
    else:
        return ""
