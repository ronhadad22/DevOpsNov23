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
        return word + 'ly'

    return word + 'ing'


def words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """

    # Remove any empty strings from the list of words
    words = list(filter(lambda word: word != "", words))

    # Join the remaining words using a space as the separator
    # and return the result
    return ' '.join(words)


def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """

    # Remove any empty strings from the list of words
    words = list(filter(lambda word: word != "", words))

    # Reverse the order of words
    words.reverse()

    # Join the remaining words using a space as the separator
    # and return the result
    return ' '.join(words)


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

    # Create an empty set to store encountered characters
    used = set()

    # Iterate through each character in the string
    for c in some_str:
        # If the character is already in the set, it's not unique
        if c in used:
            return False
        else:
            # Otherwise, add it to the set
            used.add(c)

    # All characters are unique
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

    # If the input list is empty, return an empty list
    if len(elements) == 0: return []

    # Initialize the result list with a placeholder value
    result = [None]

    # Iterate through the list to compute differences
    for i in range(0, len(elements) - 1):
        # Compute the difference between adjacent elements
        result.append(elements[i + 1] - elements[i])

    return result


def prime_number(num):
    """
    1 Kata

    Check if the given number is prime or not.

    hint: use the built-in function "range"
    :param num: the number to check
    :return: bool. True if prime, else False
    """

    # Ensure the input is a positive integer
    if num % 1 != 0 or num < 1:
        return False
    # Special case: 1 and 2 are prime
    if num <= 2:
        return True

    # Check divisibility by numbers from 2 to (num-1)
    for n in range(2, num):
        if num % n == 0: return False

    # If no divisors found, the number is prime
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

    # Convert the number to a string for easier comparison.
    num_str = str(num)
    length = len(num_str)

    # Iterate through the first half of the string, and compare it to the other half.
    # int(x / 2) will always floor, which is what we need.
    for i in range(int(length / 2)):
        # Compare characters from both ends of the string
        if num_str[i] != num_str[length - 1 - i]: return False

    # We do not iterate over the character located in the center of the string (if there is one),
    # because it's equal to itself, and thus the numer is palindrome
    return True


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

    match = ()

    # Avoiding iterations when there is no match
    if len(men) == 0 or len(women) == 0: return match

    # Init the difference with infinity so the next smaller number will be assigned
    diff = float('inf')

    # Iterate through all combinations
    for man_name, man_age in men.items():
        for woman_name, woman_age in women.items():
            curr_diff = abs(man_age - woman_age)
            if curr_diff < diff:
                # Update the best pair and minimum age difference
                match = (man_name, woman_name)
                diff = curr_diff

    return match


def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    # The order of operations in pyhon (and most other languages) requires to add parentheses.
    # Otherwise, c / 3 will be calculated before a + b + c would.
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

    # Return an empty string if the grades dictionary is empty
    if not grades: return ''

    # Find the student with the highest grade using the 'max' function
    return max(grades, key=grades.get)


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

    lines = [
        'Key     Value',
        '-------------'
    ]

    # Iterate through each key-value pair in the dictionary
    for key, value in some_dict.items():
        # Calculate the padding needed for alignment (8 characters total)
        padding = " " * (8 - len(key))
        # Append the formatted key and value to the table
        lines.append(f'{key}{padding}{value}')

    # Join the lines using newline characters to create the final table
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

    # Update dict1 with keys and values from dict2
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

    # Determine the direction of counting based on n
    direction = -1 if n < 1 else 1

    # a function that checks if a given number is boom
    def is_boom(val):
        return val % 7 == 0 or '7' in str(val)

    # Generate a list of numbers satisfying the condition
    return list(filter(is_boom, range(1, n + direction, direction)))


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """

    # A function that cipher a single character
    def cipher_char(char):
        # Spaces remain unchanged
        if char == ' ': return ' '

        # Shift by 3 positions and save the character index
        char_val = ord(char) + 3

        # Wrap around for lowercase and uppercase letters
        # so Z will become C, and not out of the A-Z
        if char_val > 122 or (90 < char_val < 97):
            char_val -= 26

        return chr(char_val)

    # Apply the cipher to each character in the input string
    return ''.join([cipher_char(char) for char in str_to_encrypt])


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

    # Initialize the sum
    sum = 0

    # Iterate through each character in the input string
    for char in digits_str:
        # Convert the character to an integer and add it to the sum
        sum += int(char)

    return sum


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
