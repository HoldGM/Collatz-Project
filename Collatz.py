#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#-------------
# global cache
#-------------

w, h = 2000, 2
cache = [[0 for x in range(w)] for y in range(h)]

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

def buildCache():
        #start building cache
        counter = 0
        while counter < 1000000:
            global cache
            index = counter / 500
            # print (int(index))
            cache[0][int(index)] = counter
            cache[1][int(index)] = collatz_eval(counter, counter)
            counter += 500
            index += 1


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    if i == 0 and j == 0:
        return 0
    maxCycles = 0
    if i > j:
        temp = i
        i = j
        j = temp
    for x in range(i, j+1):
        cycleCount = 1
        if x % 500 == 0:
            global cache
            finish = cache[1][int(x/500)]
            maxCycles += finish

        while x > 1:
            if x%2 == 0:
                x = x / 2
            else:
                x = x * 3 + 1
            cycleCount += 1
        if cycleCount > maxCycles:
            maxCycles = cycleCount
    return maxCycles

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

    buildCache()

    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

