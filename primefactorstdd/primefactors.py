"""
primefactors.py
:created on: 20160706
__author__ = 'Eliott Dupont'
:License: GPL3
"""


import sys

def factors_of(num):
    """ prime factor decomposition
    :param num: the number to decompose
    :return: a list of the prime factors of num
    """
    factors = []
    if num > 1:
        if num % 2 == 0:
            factors.append(2)
            num = num // 2
        if num > 1:
            factors.append(num)

    return factors


def main(argv):
    pass

if __name__ == '__main__':
    sys.exit(main(sys.argv))