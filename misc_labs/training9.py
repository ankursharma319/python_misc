"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    # lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    # upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    # space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.

    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print "Code is not reversible:"
        print "keys are   %s", sorted(unique_keys)
        print "values are %s", sorted(unique_vals)
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = \
    "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


# if this file is executed on it's own, check codes given
if __name__ == "__main__":
    test_codes()


def trapez(f, a, b, n):
    """
    Returns integral of function f between x=b and x=a
    using trapezoid formula with n trapeziods
    """
    h = 1.0*(b-a)/n

    def xi(i):
        return a + i*h

    def sigma_f(a, b):
        total = 0
        for i in range(1, b+1):
            total += f(xi(i))
        return total

    return (h/2.0)*(f(a)+f(b)+2*sigma_f(1, n-1))


def encode(code, msg):
    """
    Returns the encoded output string using the code
    """
    encoded_msg = ""
    for i in range(len(msg)):
        if msg[i] in code.keys():
            encoded_msg += code[msg[i]]
        else:
            encoded_msg += msg[i]
    return encoded_msg


def reverse_dic(d):
    """
    Returns a dictionary with values and keys reversed
    """
    n = {}
    for k in d.keys():
        n[d[k]] = k
    return n


def decode(code, encoded_msg):
    """
    Takes a dictionary code that contains the
    mapping dictionary with which the string encoded_msg
    has been encoded. The function decode
    returns the decoded message
    """
    return encode(reverse_dic(code), encoded_msg)
