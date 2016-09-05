#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_read_3(self):
        str = ["1 10\n", "100 200\n", "201 210\n", "900 1000\n"]

        for s in str:
            a = s.split()
            i, j = collatz_read(s)
            self.assertEqual(i, int(a[0]))
            self.assertEqual(j, int(a[1]))

    def test_read_4(self):
        s = "3\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)



    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(100, 50)
        self.assertEqual(v, 119)

    def test_eval_6(self):
        v = collatz_eval(0, 50)
        self.assertEqual(v, "Invalid Input")

    def test_eval_7(self):
        v = collatz_eval(0, 0)
        self.assertEqual(v, "Invalid Input")

    def test_eval_8(self):
        v = collatz_eval(5, 0)
        self.assertEqual(v, "Invalid Input")

    def test_eval_9(self):
        v = collatz_eval(10, 1000)
        self.assertEqual(v, 179)

    def test_eval_10(self):
        v = collatz_eval(10, 1100)
        self.assertEqual(v, 179)

    def test_eval_11(self):
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)

    def test_eval_12(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
        
    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")


    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO(u"1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO(u"10 1\n200 100\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n1000 900 174\n")

    def test_solve_3(self):
        r = StringIO(u"")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "");

    def test_solve_4(self):
        r = StringIO(u"3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
