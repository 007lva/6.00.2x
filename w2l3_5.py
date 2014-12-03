from files_finger_exercises_intDictTests import *

def sim_colision(numTrials):
    count = 0
    for i in xrange(numTrials):
        if not sim_insertions(365, 250):
            count += 1
    print count * 1.0 / numTrials

#sim_colision(100000)


def factor(n):
    return (365 - n) * 1.0 / 365

def solve():
    n = 0
    p = 1
    while (1 - p) < 0.99:
        p *= factor(n)
        n += 1
    print n

solve()
