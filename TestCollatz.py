#!/usr/bin/env python3
"""This file contains the unit tests for Collatz Project"""
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
    """Class for Collatz Unit Tests"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Read function test 1"""
        string = "1 10\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 1)
        self.assertEqual(jth, 10)

    def test_read_2(self):
        """Read function test 2"""
        string = "201 210\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 201)
        self.assertEqual(jth, 210)

    def test_read_3(self):
        """Read function test 3"""
        string = ["1 10\n", "100 200\n", "201 210\n", "900 1000\n"]

        for pair in string:
            temp = pair.split()
            ith, jth = collatz_read(pair)
            self.assertEqual(ith, int(temp[0]))
            self.assertEqual(jth, int(temp[1]))

    def test_read_4(self):
        """Read function test 4"""
        string = "3\n"
        ith, jth = collatz_read(string)
        self.assertEqual(ith, 0)
        self.assertEqual(jth, 0)



    # ----
    # eval
    # ----

    def test_eval_1(self):
        """collatz_ eval function test 1"""
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """collatz_ eval function test 2"""
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """collatz_ eval function test 3"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """collatz_ eval function test 4"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """collatz_ eval function test 5"""
        value = collatz_eval(100, 50)
        self.assertEqual(value, 119)

    def test_eval_6(self):
        """collatz_ eval function test 6"""
        value = collatz_eval(0, 50)
        self.assertEqual(value, "Invalid Input")

    def test_eval_7(self):
        """collatz_ eval function test 7"""
        value = collatz_eval(0, 0)
        self.assertEqual(value, "Invalid Input")

    def test_eval_8(self):
        """collatz_ eval function test 8"""
        value = collatz_eval(5, 0)
        self.assertEqual(value, "Invalid Input")

    def test_eval_9(self):
        """collatz_ eval function test 9"""
        value = collatz_eval(10, 1000)
        self.assertEqual(value, 179)

    def test_eval_10(self):
        """collatz_ eval function test 10"""
        value = collatz_eval(10, 1100)
        self.assertEqual(value, 179)

    def test_eval_11(self):
        """collatz_ eval function test 11"""
        value = collatz_eval(1, 1000000)
        self.assertEqual(value, 525)

    def test_eval_12(self):
        """collatz_ eval function test 12"""
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    # -----
    # print
    # -----

    def test_print_1(self):
        """collatz_print funciton test 1"""
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """collatz_print funciton test 2"""
        write = StringIO()
        collatz_print(write, 100, 200, 125)
        self.assertEqual(write.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """collatz_print funciton test 3"""
        write = StringIO()
        collatz_print(write, 201, 210, 89)
        self.assertEqual(write.getvalue(), "201 210 89\n")


    # -----
    # solve
    # -----

    def test_solve_1(self):
        """collatz_solve function test 1"""
        read = StringIO(u"1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """collatz_solve function test 2"""
        read = StringIO(u"10 1\n200 100\n1000 900\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "10 1 20\n200 100 125\n1000 900 174\n")

    def test_solve_3(self):
        """collatz_solve function test 3"""
        read = StringIO(u"")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "")

    def test_solve_4(self):
        """collatz_solve function test 4"""
        read = StringIO(u"3\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "")

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
