def sum_of_element(elements):
    """
    1 Kata

    :param elements: list of integers
    :return: Return int - the sum of all elements.
    """
    # elements=[1,2]
    sum=0

    for moshe in elements:
        print(moshe)
        sum=sum+moshe

    return sum

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
    if len(word) < 3:
        return word
    elif word[-3:] == 'ing':
        return word + 'ly'
    else:
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
    #words = ' '.join(words)

    #return words
    # Filter out empty strings to avoid extra spaces in the result
    filtered_words = [word for word in words if word]
    # Concatenate the filtered words
    concatenated_words = ' '.join(filtered_words)

    return concatenated_words


def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """
    #words = ' '.join(words[::-1])

    #return words
    # Filter out empty strings to avoid extra spaces in the result
    filtered_words = [word for word in words if word]
    # Concatenate the words in reverse order
    reversed_concatenation = ' '.join(filtered_words[::-1])

    return reversed_concatenation


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
    # Use a set to store unique characters
    unique_characters = set()

    # Iterate through each character in the string
    for char in some_str:
        # If the character is already in the set, it's not unique
        if char in unique_characters:
            return False
        # Otherwise, add it to the set
        else:
            unique_characters.add(char)

    # If the loop completes without returning False, all characters are unique

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
    # Check if the input list is empty
    if not elements:
        return []

    # Initialize the result list with None as the first element
    diff_list = [None]

    # Iterate through the elements starting from the second one
    for i in range(1, len(elements)):
        # Calculate the difference between the current and previous elements
        diff = elements[i] - elements[i - 1]
        # Append the calculated difference to the result list
        diff_list.append(diff)
    return diff_list


def prime_number(num):
    """
    1 Kata

    Check if the given number is prime or not.

    hint: use the built-in function "range"
    :param num: the number to check
    :return: bool. True if prime, else False
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
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
    # Check if either of the input dictionaries is empty
    if not men or not women:
        return ()  # Return an empty tuple if one or both dictionaries are empty

    # Initialize variables to store the best match and the minimum age difference
    best_match = None
    min_age_difference = float('inf')

    # Iterate over each combination of names from men and women dictionaries
    for men_name, men_age in men.items():
        for women_name, women_age in women.items():
            # Calculate the absolute age difference between the current pair
            age_difference = abs(men_age - women_age)

            # Update the best match if the current pair has a smaller age difference
            if age_difference < min_age_difference:
                best_match = (men_name, women_name)
                min_age_difference = age_difference

    return best_match


def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
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
    highest_grade = float('-inf')
    highest_grade_student = ""

    for student, grade in grades.items():
        if grade > highest_grade:
            highest_grade = grade
            highest_grade_student = student

    return highest_grade_student


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
    # Start with the table header
    table = "Key     Value\n-------------"
    # Only add a newline if the dictionary is not empty
    if some_dict:
        table += "\n"
    for key, value in some_dict.items():
        # Append each key-value pair to the table string
        table += f"{key:<7} {value}\n"
    # Remove the last newline to match the test case expectations
    if some_dict:
        table = table.rstrip('\n')
    return table


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
    merged_dict = dict1.copy()
    merged_dict.update(dict2)

    return merged_dict


def seven_boom(n):
    """
    1 Kata

    This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n

    e.g. For n = 30
    The return value will be [7, 14, 17, 21, 27, 28]

    :param n: int. The last number for count for a 7-boom play
    :return: list of integers
    """
    # Special case for n == 0
    if n == 0:
        return [0]

    boom_list = []
    if n > 0:  # Handling positive n
        for num in range(1, n + 1):
            if '7' in str(num) or num % 7 == 0:
                boom_list.append(num)
    else:  # Handling negative n
        boom_list.append(0)  # Include 0 as per the negative test case requirements
        for num in range(-1, n - 1, -1):  # Iterate through negative numbers
            if '7' in str(abs(num)) or abs(num) % 7 == 0:
                boom_list.append(num)

    return boom_list


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    result = ""
    for char in str_to_encrypt:
        if char.isalpha():  # Check if the character is an alphabet letter
            shift = 3
            if char.islower():
                # Encrypt lowercase letters
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Encrypt uppercase letters
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Keep spaces as they are
            result += char
    return result


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
    # Initialize the sum to 0
    total_sum = 0

    # Iterate through each character in the input string
    for digit in digits_str:
        # Convert the current character to an integer and add it to the total sum
        total_sum += int(digit)

    # Return the total sum of the digits
    return total_sum


if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2]))
    print(sum_of_element([1, 3]))
    # print(sum_of_element([4, 5, 6]))
    #
    # print('\nverbing:\n--------------------')
    # print(verbing('walk'))
    # print(verbing('swimming'))
    # print(verbing('do'))
    #
    # print('\nwords_concatenation:\n--------------------')
    # print(words_concatenation(['take', 'me', 'home']))
    #
    # print('\nreverse_words_concatenation:\n--------------------')
    # print(reverse_words_concatenation(['take', 'me', 'home']))
    #
    # print('\nis_unique_string:\n--------------------')
    # print(is_unique_string('aasdssdsederd'))
    # print(is_unique_string('12345tgbnh'))
    #
    # print('\nlist_diff:\n--------------------')
    # print(list_diff([1, 2, 3, 8, 77, 0]))
    #
    # print('\nprime_number:\n--------------------')
    # print(prime_number(5))
    # print(prime_number(22))
    #
    # print('\npalindrome_num:\n--------------------')
    # print(palindrome_num(12221))
    # print(palindrome_num(577))
    #
    # print('\npair_match:\n--------------------')
    # print(pair_match(
    #     {
    #         "John": 20,
    #         "Abraham": 45
    #     },
    #     {
    #         "July": 18,
    #         "Kim": 26
    #     }
    # ))
    #
    # print('\nbad_average:\n--------------------')
    # print(bad_average(1, 2, 3))
    #
    # print('\nbest_student:\n--------------------')
    # print(best_student({
    #     "Ben": 78,
    #     "Hen": 88,
    #     "Natan": 99,
    #     "Efraim": 65,
    #     "Rachel": 95
    # }))
    #
    # print('\nprint_dict_as_table:\n--------------------')
    # print(print_dict_as_table({
    #     "Ben": 78,
    #     "Hen": 88,
    #     "Natan": 99,
    #     "Efraim": 65,
    #     "Rachel": 95
    # }))
    #
    # print('\nmerge_dicts:\n--------------------')
    # print(merge_dicts({'a': 1}, {'b': 2}))
    #
    # print('\nseven_boom:\n--------------------')
    # print(seven_boom(30))
    #
    # print('\ncaesar_cipher:\n--------------------')
    # print(caesar_cipher('Fly Me To The Moon'))
    #
    # print('\nsum_of_digits:\n--------------------')
    # print(sum_of_digits('1223432'))

