from operator import sub, mul
HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """

    if pos < 10 and pos != 8:
        return 0
    else:
        if pos % 10 == 8:
            return num_eights(pos//10) + 1
        else:
            return num_eights(pos//10)


def pingpong(n):  # n = index+1
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    # We want to store STARTING points in helper, and check when it reaches the end case we want.
    # use flags(up_or_down, like who in HOG) when you need to keep track of only two states
    def helper(pong_value, i, up_or_down):
        # we want to keep track of: ending value(pong_value), index were on(i), and whether going up or down
        if i == n:
            return pong_value
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(pong_value - up_or_down, i+1, (up_or_down * -1))
        else:
            return helper(pong_value + up_or_down, i+1, up_or_down)

    return helper(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4

    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
"""

# you can do start checking from the last one: so compare last and rest.
#

    if n < 10:
        return 0
    last = n % 10
    rest - n//10
    return max(last-rest % 10 - 1, 0) + missing_digits(rest)


'''
    def helper(rest_of_num, missing_nums, last_dig):
        # rest of num ,count, last digit
        if rest_of_num == 0:  
            return missing_nums
        if (last_dig - rest_of_num % 10) > 1:
            return helper(rest_of_num//10, (last_dig - rest_of_num % 10-1)+missing_nums, rest_of_num % 10)
        else:
            return helper(rest_of_num//10, missing_nums, rest_of_num % 10)

    return helper(n//10, 0, n % 10)  
'''


def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
    # this line is technically None so its gonna return none. so when it errors and says its not callable it means that we are working with a None (look at line 141n142)

    # steps:
    # keep track of hg current coint (need helper func)
    # sum the recursive calls to get hte number of ways
    # if arrive to 0 return 1: base case
    # if arrive to negative value or coin is None, return 0: base case

    # call the helper, immideiently after making it, with the starting parameters :NOTE

    def helper(change, coin):
        if change == 0:
            return 1
        if change < 0 or coin == None:
            return 0
        without_coin = helper(change, ascending_coin(coin))
        with_coin = helper(change - coin, coin)
        return without_coin+with_coin
    return helper(change, 1)


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

    # solution in pictures, from hw recovery


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    # use count partition notes code, change only one of the base cases.


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
