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
    if len(word) >= 3:
        if word.endswith('ing'):
            result = word + 'ly'
        else:
            result = word + 'ing'
    else:
        result = word

    return result


def words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """
    return ' '.join(filter(None, words))



def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """
    result = ' '.join(reversed(words))
    return ' '.join(result.split())  # Remove extra spaces


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
    seen_characters = set()

    for char in some_str:
        if char in seen_characters:
            return False
        seen_characters.add(char)

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
    if not elements: #check if the input is empty and return '[]' which is the empty list.
        return []

    diff_list = [None]  #This line initializes a new list called diff_list with the first element set to None.
    for i in range(1, len(elements)):  #this is a loop that iterates over the 'indices' of the elements list, starting from index 1. The loop is used to calculate the differences between
        diff_list.append(elements[i] - elements[i - 1]) # Inside the loop, the function calculates the difference between the current element (elements[i]) and its previous element (elements[i-1]). The result is appended to the diff_list.

    return diff_list


def prime_number(num):
    """
    1 Kata

    Check if the given number is prime or not.

    hint: use the built-in function "range"
    :param num: the number to check
    :return: bool. True if prime, else False
    """
    if num < 2:
        return False  # Numbers less than 2 are not prime

        # Check for divisibility from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # The number is divisible, not prime

    return True  # No divisors found, the number is prime


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
    # Convert the number to a string
    num_str = str(num)

    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]


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
    if not men or not women:  # If either of the dictionaries is empty
        return ()  # Return an empty tuple

    min_age_difference = float('inf')
    result_pair = None

    # Iterate through each pair of men and women
    for men_name, men_age in men.items():
        for women_name, women_age in women.items():
            # Calculate absolute age difference
            age_difference = abs(men_age - women_age)

            # Update result_pair if the current pair has a smaller absolute age difference
            if age_difference < min_age_difference:
                min_age_difference = age_difference
                result_pair = (men_name, women_name)

    return result_pair


def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    return (a + b + c) / 3  #added Parenthese because it didnt divide the whole sum by 3 to calculate avg.


def best_student(grades):
    """
    1 Kata

    This function gets a dict of students -> grades mapping, and returns the student with the highest grade

    e.g.
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,:

        "Efraim": 65,
        "Rachel": 95
    }

    will return "Natan"

    :param grades: dict of name -> grade mapping
    :return: str. some key from the dict
    """
    if not grades:
        return ""  # Return None for an empty dictionary

    best_student_name = max(grades, key=grades.get) #This line uses the max function to find the key (student name) with the maximum value (grade) in the dictionary.
    return best_student_name

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
    # Use the update method to merge dict2 into dict1
    dict1.update(dict2)

    # Return the modified dict1
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
    # Initialize an empty list to store "Booms"

    boom_list = list()

    # case n==0: return list with 0
    if n == 0:
        boom_list.append(0)
        return boom_list

    # define function is_boom
    def is_boom(val):
        return val % 7 == 0 or '7' in str(val)

    # support both directions: from 1 to n and from 1 to -n
    step = -1 if n < 0 else 1
    for i in range(1, n, step):
        if is_boom(i):
            boom_list.append(i)
    return boom_list

def caesar_cipher(str_to_encrypt): #important to go through the code
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    # Define the shift value for the caesar cipher
    shift = 3

    # Initialize an empty string to store the encrypted result
    encrypted_str = ""

    # Iterate through each character in the input string
    for char in str_to_encrypt:
        # Check if the character is a letter (a-z or A-Z)
        if char.isalpha():
            # Determine the case (uppercase or lowercase) of the letter
            is_upper = char.isupper()

            # Shift the character by the specified amount
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            # Append the shifted character to the encrypted string
            encrypted_str += shifted_char
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_str += char

    # Return the encrypted string
    return encrypted_str


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
    # Check if the input string is empty
    if not digits_str:
        return 0  # Return 0 for an empty string

    # Initialize a variable to store the sum of digits
    total_sum = 0

    # Iterate through each character in the input string
    for char in digits_str:
        # Convert the character to an integer and add it to the total sum
        total_sum += int(char)

    # Return the sum of digits
    return total_sum

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
        "Ben": 99,
        "Hen": 88,
        "Natan": 78,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 99,
        "Hen": 88,
        "Natan": 78,
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

