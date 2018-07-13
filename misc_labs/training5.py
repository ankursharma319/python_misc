# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:22:02 2015

@author: Akhil
"""

import os.path


def count_sub_in_file(filename, s):
    """
    Returns the number of occurrences of s in the
    file given through filename
    """
    if(os.path.exists(filename)):
        fr = open(filename, "r")
        data = fr.read()
        fr.close()
        return data.count(s)
    else:
        return -1


def count_vowels(s):
    """
    Returns the number of letters 'a', 'e', 'i', 'o',
    'u', 'A', 'E', 'I', 'O', 'U' in a given string s
    """
    count = 0
    vowelList = ['a', 'e', 'i', 'o',
                 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowelList:
        count += s.count(vowel)
    return count
