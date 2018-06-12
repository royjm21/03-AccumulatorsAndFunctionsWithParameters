"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jeremy Roy.
"""  # TODOne: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_powers()
    # run_test_sum_powers_in_range()


def run_test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # TODOne: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    print(' ')
    print('Test 1:')
    expected = 4425
    actual = sum_powers(5, 5)
    print('expected:', expected)
    print('actual:', actual)

    print(' ')
    print('Test 2:')
    expected = 20.74089637
    actual = sum_powers(7, 0.8)
    print('expected:', expected)
    print('actual:', actual)

    print(' ')
    print('Test 3:')
    expected = 1.19931717
    actual = sum_powers(13, -3)
    print('expected:', expected)
    print('actual:', actual)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # TODOne: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    x = 0
    for k in range(n+1):
        x = x + ((k+1)**p)

    return x - (n+1)**p


def run_test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # TODO: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    print(' ')
    print('Test 1:')
    actual = sum_powers_in_range(5, 10, 4)
    expected = 24979
    print('expected:', expected)
    print('actual:', actual)

    print(' ')
    print('Test 2:')
    actual = sum_powers_in_range(4, 17, .75)
    expected = 80.45130787
    print('expected:', expected)
    print('actual:', actual)

    print(' ')
    print('Test 3:')
    actual = sum_powers_in_range(2, 25, -5)
    expected = 0.0366071646
    print('expected:', expected)
    print('actual:', actual)

def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
