# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def newton(f, x, feps, maxit):
    """
    Takes a function f(x) and an initial guess x
    for the root of the function f(x), an allowed
    tolerance feps and the maximum number of iterations
    that are allowed maxit, and returns the root of f(x)
    """
    iterations = 0
    while abs(f(x)) > feps:
        x = x - (f(x) / fprime(f, x))
        iterations += 1
        if iterations >= maxit:
            raise RuntimeError(
                "Failed after %d iterations" % maxit)
            break
    return x


def fprime(f, x, eps=1e-6):
    """
    which returns a numerical approximation of the first
    derivative of the function f(x) using central differences.
    The value that the function returns is derivative
    """
    return (f(x + eps/2)-f(x - eps/2))/eps


def is_palindrome(s):
    """
    Takes a string s and returns the value True if s
    is a palindrome, and returns False otherwise
    """
    if len(s) < 2:
        return True
    elif len(s) >= 2:
        if(s[0] == s[len(s)-1]):
            if is_palindrome(s[1:len(s)-1]):
                return True
            else:
                return False
        else:
            return False


def is_palindrome2(s):
    """
    Takes a string s and returns the value True if s
    is a palindrome, and returns False otherwise
    """
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
