# Lab10 - Ankur Sharma
from __future__ import division
import numpy as np
import scipy.optimize
import scipy
import pylab


def model(t, Ti, Ta, c):
    T = (Ti-Ta)*np.exp(-t/c)+Ta
    return T


def read2coldata(filename):
    """Open a text file with two columns of data
    and assigns the 2 colums of data in two arrays and return
    a tuple containing these arrays"""
    fr = open(filename, 'r')
    data = fr.readlines()
    fr.close()
    column1 = np.array([float(x.split()[0]) for x in data])
    column2 = np.array([float(x.split()[1]) for x in data])
    return column1, column2


def extract_parameters(ts, Ts):
    """A function extract_parameters(ts, Ts) which expects a numpy array ts
    with time values and a numpy array Ts of the same length as ts with
    corresponding temperature values. The function should estimate and return
    a tuple of the three model parameters Ti, Ta and c (in this order) by
    fitting the model function as in equation (1) to the data ts and Ts."""
    p, pcov = scipy.optimize.curve_fit(model, ts, Ts, (100, 30, 500))
    Ti, Ta, c = p
    return p


def plot(ts, Ts, Ti, Ta, c):
    pylab.plot(ts, Ts, 'o', label='data')
    f = model(ts, Ti, Ta, c)
    pylab.plot(ts, f, label='fitted')
    pylab.legend()
    pylab.show()


def sixty_degree_time(Ti, Ta, c):
    """Takes values for initial temperature, ambient temperature
    and time constant and returns the time that it will take for the
    temp to reach 60 C"""
    time_req = -c*np.log((60-Ta)/(Ti-Ta))
    return time_req
