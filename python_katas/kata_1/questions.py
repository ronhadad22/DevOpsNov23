import math
import sys


def sum_of_element(elements):
    """
    1 Kata

    :param elements: list of integers
    :return: Return int - the sum of all elements.
    """
    s = 0
    for num in elements:
        s = s + num

    return s


def verbing(word):
    """
    1 Kata

    Given a string 'word', if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged.

    e.g.
    teach -> teaching
    do -> do
    swimming -> swimmingly

    :param word: str
    :return: Return the resulting string.
    """
    if len(word) <= 2:
        return word

    if word[-3:] == 'ing':
        word += "ly"
    else:
        word += "ing"
    return word


def words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """
    # given list is empty, then return ''
    if not words:
        return ''

    # filter out empty strings
    filtered_empty = [s for s in words if s]
    # Concatenate the filtered words
    return ' '.join(filtered_empty)


def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """
    # if given an empty list, return an empty string
    if not words:
        return ''
    # filter out empty strings
    filtered_empty = [s for s in words if s]
    # reverse and join to a string
    return ' '.join(reversed(filtered_empty))


def is_unique_string(some_str):
    """
    2 Kata

    Given a string, the function returns True if all characters in the string are unique, False otherwise

    e.g
    'abcd' -> True
    'aaabcd' -> False
    '' -> True      (empty string)

    :param some_str:
    :return: bool
    """
    # empty string always is unique
    if len(some_str) == 0:
        return True

    # safe chars in a set
    my_set = set()
    for char in some_str:
        if char in my_set:
            return False
        my_set.add(char)
    return True


def list_diff(elements):
    """
    1 Kata

    Given a list of integers as an input, return the "diff" list - each element is
    reduces by its previous one. The first element should be None

    e.g.
    [1, 2, 3, 4, 7, 11] -> [None, 1, 1, 1, 3, 4]
    [] -> []
    [1, 5, 0, 4, 1, 1, 1] -> [None, 4, -5, 4, -3, 0, 0]

    :param elements: list of integers
    :return: the diff list
    """
    if len(elements) == 0:
        return []
    list_to_return = [None]
    prev = elements[0]
    # going from element 1 and getting difference between current and previous
    for el in elements[1:]:
        curr = el
        list_to_return.append(curr - prev)
        prev = curr
    return list_to_return


def prime_number(num):
    """
    1 Kata

    Check if the given number is prime or not.

    hint: use the built-in function "range"
    :param num: the number to check
    :return: bool. True if prime, else False
    """
    # number less than 2 isn't considered prime
    if num < 2:
        return False
    # 2 is always prime
    if num == 2:
        return True
    # it's enough to check against sqrt from the num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def palindrome_num(num):
    """
    1 Kata

    Check whether a number is palindrome or not

    e.g.
    1441 -> True
    123 -> False

    :param num: int
    :return: bool. True is palindrome, else False
    """
    if num < 0:
        return False

    # one-digit number is always a palindrom of itself
    if 0 <= num < 10:
        return True

    # convert the number to a string
    str_number = str(num)
    # the string and his reversed version are equal
    return str_number == str_number[::-1]


def pair_match(men, women):
    """
    3 Kata

    This function gets two dictionaries of the type:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age
    The function returns a pair of names (tuple), of from men dict, the other from women dict,
    where their absolute age differences is the minimal

    e.g.
    men = {"John": 20, "Abraham": 45}
    women = {"July": 18, "Kim": 26}

    The returned value should be a tuple ("John", "July") since:

    abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
    abs(John - July) = abs(20 - 18) = abs(2) = 2
    abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
    abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

    :param men: dict mapping name -> age
    :param women: dict mapping name -> age
    :return: tuple (men_name, women_name) such their age absolute difference is the minimal
    """
    if not men or not women:
        return ()

    min_keys = ()
    min_diff = sys.maxsize

    for k1, val1 in men.items():
        for k2, val2 in women.items():
            diff = abs(val1 - val2)
            if diff < min_diff:
                min_diff = diff
                min_keys = (k1, k2)
    return min_keys


def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    # first - operation in (), then /
    return (a + b + c) / 3


def best_student(grades):
    """
    1 Kata

    This function gets a dict of students -> grades mapping, and returns the student with the highest grade

    e.g.
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    will return "Natan"

    :param grades: dict of name -> grade mapping
    :return: str. some key from the dict
    """
    # if grades is empty then return ''
    if len(grades) == 0:
        return ""

    # min integer
    max_grade = -sys.maxsize - 1

    best_one = ""
    for key, value in grades.items():
        # safe at side value and key if the value is bigger then current max_grade
        if value > max_grade:
            max_grade = value
            best_one = key
    return best_one


def print_dict_as_table(some_dict):
    """
    1 Kata

    Prints dictionary keys and values as the following format. For:
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    The output will be:

    Key     Value
    -------------
    Ben     78
    Hen     88
    Natan   99
    Efraim  65
    Rachel  95

    :param some_dict:
    :return:
"""
    header = "Key     Value\n-------------"

    if not some_dict:
        return header

    # number of spaces from 1st position to "Value"
    spaces = 8
    lines = [header]

    for key, value in some_dict.items():
        space_string = " " * (spaces - len(key))
        lines.append(f'{key}{space_string}{value}')
    return '\n'.join(lines)


def merge_dicts(dict1, dict2):
    """
    1 Kata

    This functions merges dict2's keys and values into dict1, and returns dict1

    e.g.
    dict1 = {'a': 1}
    dict2 = {'b': 2}

    The results will by
    dict1 = {'a': 1, 'b': 2}

    :param dict1:
    :param dict2:
    :return:
    """
    # checking edge cases when one or both given dicts
    # are empty
    if len(dict1) == 0 and len(dict2) == 0:
        return {}
    if len(dict1) == 0 and len(dict2) != 0:
        return dict2
    if len(dict1) != 0 and len(dict2) == 0:
        return dict1

    # standard Python function for merge two dicts
    dict1.update(dict2)
    return dict1


def seven_boom(n):
    """
    1 Kata

    This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n

    e.g. For n = 30
    The return value will be [7, 14, 17, 21, 27, 28]

    :param n: int. The last number for count for a 7-boom play
    :return: list of integers
    """
    # define an empty list
    list_to_ret = list()

    # case n==0: return list with 0
    if n == 0:
        list_to_ret.append(0)
        return list_to_ret

    # define function is_boom
    def is_boom(val):
        return val % 7 == 0 or '7' in str(val)

    # support both directions: from 1 to n and from 1 to -n
    step = -1 if n < 0 else 1
    for i in range(1, n, step):
        if is_boom(i):
            list_to_ret.append(i)
    return list_to_ret


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    if len(str_to_encrypt) == 0:
        return ''

    def encrypt_char(char, shift):
        if char.isalpha():
            ascii_code = ord(char)
            if char.isupper():
                # Apply the shift to uppercase letters
                shifted_code = (ascii_code - 65 + shift) % 26 + 65
            else:
                # Apply the shift to lowercase letters
                shifted_code = (ascii_code - 97 + shift) % 26 + 97
            # Convert the shifted ASCII code back to a character
            return chr(shifted_code)
        else:
            return char

    # shift==3 was defined ia a kata
    shift = 3
    chars = list()
    for char in str_to_encrypt:
        chars.append(encrypt_char(char, shift))
    return ''.join(chars)


def sum_of_digits(digits_str):
    """
    1 Kata

    Calculates the sum of digits in a string (you can assume the input is a string containing numeric digits only)

    e.g.
    '2524' -> 13
    '' -> 0
    '00232' -> 7


    :param digits_str: str of numerical digits only
    :return: int representing the sum of digits
    """
    if len(digits_str) == 0:
        return 0

    sum_to_return = 0
    # iterate on each element in the string
    for ch in digits_str:
        # convert current char to int and add it to current sum
        sum_to_return += int(ch)
    return sum_to_return


if __name__ == '__main__':
    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2, 3, 4, 5, 6]))

    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))

    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', 'me', 'home']))

    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))

    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))

    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))

    print('\nprime_number:\n--------------------')
    print(prime_number(5))
    print(prime_number(22))

    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(12221))
    print(palindrome_num(577))

    print('\npair_match:\n--------------------')
    print(pair_match(
        {
            "John": 20,
            "Abraham": 45
        },
        {
            "July": 18,
            "Kim": 26
        }
    ))

    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))

    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))

    print('\nseven_boom:\n--------------------')
    print(seven_boom(30))

    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))

    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('1223432'))
