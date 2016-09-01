#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#-------------
# global cache
#-------------

cache = dict()

# ------------
# collatz_read
# ------------

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    try:
        if i == 0 or j == 0 or i > 1000000 or j > 1000000:
            raise IOError('Invalid Input')
        maxCycles = 0
        if i > j:
            temp = i
            i = j
            j = temp
        if i < (j //2):
            i = j // 2
        for x in range(i, j +1):
            if x in cache:
                cycleCount = cache[x]
                if cycleCount > maxCycles:
                    maxCycles = cycleCount
            t = x
            cycleCount = 1
            while t > 1:
                if t in cache:
                    cycleCount += cache[t] - 1
                    cache[x] = cycleCount
                    break
                if t % 2 == 0:
                    t = t / 2
                else:
                    t = t * 3 + 1
                cycleCount += 1
                
            if cycleCount > maxCycles:
                maxCycles = cycleCount
                cache[x] = cycleCount
        return maxCycles
    except IOError as e:
        return "Invalid Input"
# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(u"" + str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):

    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        # print(str(i) + " " + str(j))
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

