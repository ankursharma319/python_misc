# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:36:03 2015

@author: Akhil
"""


def seq_sqrt(xs):
    """Takes a list of numbers,
    and returns a list of the same length
    that contains the square root for each
    number in the list."""
    l = []
    for n in xs:
        l.append(n**0.5)
    return l


def mean(xs):
    """Takes a sequence xs of numbers, and returns the
    (arithmetic) mean (i.e. the average value)."""
    total = 0.0
    number = 0
    for n in xs:
        total = total + n
        number = number + 1
    if number == 0:
        return 0
    else:
        return total/number


def wc(filename):
    """Returns the number of words in file filename"""
    fr = open(filename, "r")
    data = fr.read()
    fr.close()

    wordCount = 0
    lines = data.split("\n")
    for line in lines:
        words = line.split()
        wordCount += len(words)

    return wordCount
