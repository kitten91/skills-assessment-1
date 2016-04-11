"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    new_odd_list = [item for item in number_list if item % 2]
    print new_odd_list

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    new_even_list = [item for item in number_list if not item % 2]
    print new_even_list

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    for index, item in enumerate(my_list):
        print index, item

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_word_list = []
    for word in word_list:
        if len(word)>4:
            long_word_list.append(word)
        else:
            None
    print long_word_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    n = 100
    sorted_number_list = sorted(number_list)
    for i in sorted_number_list:
        inum = int(i)
        if inum < n:
            n = inum
            print n
        else:
            None


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    n = 0
    sorted_number_list = sorted(number_list)
    for i in sorted_number_list:
        inum = sorted_number_list[-1]
        if inum > n:
            n = inum
            print n
        else:
            None

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    my_int = float(2)
    new_list = [x / my_int for x in number_list]
    print new_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    word_length_numbers = [len(word) for word in word_list]
    print word_length_numbers


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    sum_numbers_total = 0
    for i in range(len(number_list)):
        sum_numbers_total += number_list[i]

    print sum_numbers_total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    mult_numbers_total = 1
    for i in range(len(number_list)):
        mult_numbers_total *= number_list[i]

    print mult_numbers_total


# def join_strings(word_list):
#     """Return a string of all input strings joined together.

#     Python has a built-in method on lists, `join`---but for this exercise, you
#     should not use it.

#         >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
#         'spamspambaconballoonicorn'

#     For an empty list, you should return an empty string:

#         >>> join_strings([])
#         ''

#     """
#     for word in word_list:
#         s = []
#         if word in word_list[0]:
#             s += word
#             print s
#         else:
#             print ''

#     return 

# def average(number_list):
#     """Return the average (mean) of the list of numbers given.

#         >>> average([2, 12, 3])
#         5.666666666666667

#     There is no defined answer if the list given is empty. It's fine if
#     this raises an error when given an empty list.
#     """
#     length = len(number_list)
#     total_sum = 0 
#     for i in range(length): 
#         total_sum += number_list[i]
#     total_sum = sum(number_list)  
#     average = float(total_sum/length)

#     print '{0:.16f}'.format(average)

#     return 0


# def join_strings_with_comma(list_of_words):
#     """Return ['list', 'of', 'words'] like "list, of, words".

#         >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'

#     If there's only one thing in the list, it should return just that
#     thing, of course:

#         >>> join_strings_with_comma(["Pretzel"])
#         'Pretzel'

#     """
#     w = ''
#     for i in range(0,len(list_of_words)):
#         if i > index[0]
#             print w
#         else:
#         ''



##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
