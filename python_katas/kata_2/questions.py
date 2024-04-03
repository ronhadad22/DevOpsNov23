def valid_parentheses(s):
    """
    3 Kata

    This function gets a string containing just the characters
    '(', ')', '{', '}', '[' and ']',
    and determines if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    e.g.
    s = '[[{()}](){}]'  -> True
    s = ']}'          -> False
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack
pass

def fibonacci_fixme(n):
    """
    2 Kata

    A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8, 13....
    The first two terms are 1 and 1. All other terms are obtained
    by adding the preceding two terms.

    This function should return the n'th element of fibonacci sequence. As following:

    fibonacci_fixme(1) -> 1
    fibonacci_fixme(2) -> 1
    fibonacci_fixme(3) -> 2
    fibonacci_fixme(4) -> 3
    fibonacci_fixme(5) -> 5

    But it doesn't (it has some bad lines in it...)
    You should (1) correct the for statement and (2) swap two lines,
     so that the correct fibonacci element will be returned
    """


    if not isinstance(n, int) or n < 1:
        return "Invalid input. Please provide a positive integer for 'n'."
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    else:
        return 0


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    from collections import Counter

    with open(file_path, 'r') as file:
         names = file.read().splitlines()

    name_counter = Counter(names)
    most_common_name = max(name_counter, key=name_counter.get)

    return most_common_name


def files_backup(dir_path):
    """
    3 Kata

    This function gets a path to a directory and generated a .gz file containing all the files the directory contains
    The backup .gz file name should be in the form:

    'backup_<dir_name>_<yyyy-mm-dd>.tar.gz'

    Where <dir_name> is the directory name (only the directory, not the full path given in dir_path)
    and <yyyy-mm-dd> is the date e.g. 2022-04-10

    You can assume dir_path exists in the file system

    :param dir_path: string - path to a directory
    :return: str - the backup file name
    """
    import os
    import tarfile
    # import gzip dont need it
    from datetime import datetime

    dir_name = os.path.basename(dir_path)


    current_date = datetime.now().strftime('%Y-%m-%d')
    backup_file_name = f'backup_{dir_name}_{current_date}.tar.gz'
    with tarfile.open(backup_file_name, 'w:gz') as tar:
        tar.add(dir_path, arcname=os.path.basename(dir_path))

    return backup_file_name



def replace_in_file(file_path, text, replace_text):
    """
    2 Kata
    This function gets a path of text file, it replaces all occurrences of 'text' by 'replace_text'.
    The function saves the replaces content on the same path (overwrites the file's content)

    You MUST check that file_path exists in the file system before you try to open it

    :param file_path: relative or absolute path to a text file
    :param text: text to search
    :param replace_text: text to replace with
    :return: None
    """

    import os

    if not os.path.exists(file_path):
     print(f"Error: {file_path} does not exist.")
    with open(file_path, 'r') as file:
        file_content = file.read()
    replaced_content = file_content.replace(text, replace_text)

    with open(file_path, 'w') as file:
        file.write(replaced_content)
    return replace_in_file






def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """
    import json

    merged_json = {}


    for json_path in json_paths:

        with open(json_path, 'r') as file:
            json_content = json.load(file)

        merged_json.update(json_content)

    return merged_json



def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        return True

    elif all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        return True
    else:
        return False



def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    if rows is None:
        rows = [0, 1, 2]

    total_sum = 0
    count = 0


    for i in rows:
        for j in range(len(mat[i])):
            total_sum += mat[i][j]
            count += 1


    if count > 0:
        average = total_sum / count
    else:
        average = 0

    return average




def merge_sorted_lists(l1, l2):
    """
    1 Kata

    This function gets two sorted lists (each one of them is sorted)
    and returns a single sorted list combining both of them.

    Try to be as efficient as you can (hint - don't use Python's built in sort() or sorted() functions)

    :param l1: list of integers
    :param l2: list of integers
    :return: list: sorted list combining l1 and l2
    """
    merged_list = []
    i = 0
    j = 0


    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1


    while i < len(l1):
        merged_list.append(l1[i])
        i += 1


    while j < len(l2):
        merged_list.append(l2[j])
        j += 1

    return merged_list


def longest_common_substring(str1, str2):
    """
    4 Kata

    This functions gets two strings and returns their longest common substring

    e.g. for
    str1 = 'Introduced in 1991, The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'
    since it's the longest string contained both in str1 and str2

    :param str1: str
    :param str2: str
    :return: str - the longest common substring
    """
    m = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
                if m[i][j] > max_length:
                    max_length = m[i][j]
                    end_index = i
            else:
                m[i][j] = 0

    common_substring = str1[end_index - max_length: end_index]

    return common_substring


def longest_common_prefix(str1, str2):
    """
    1 Kata

    This functions gets two strings and returns their longest common prefix

    e.g. for
    str1 = 'The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'

    :param str1: str
    :param str2: str
    :return: str - the longest common prefix
    """
    min_length = min(len(str1), len(str2))
    prefix = ""
    for i in range(min_length):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break
    return prefix


def rotate_matrix(mat):
    """
    2 Kata

    This function gets a matrix n*m (list of m lists of length n) and rotate the matrix clockwise
    e.g.
    for [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] which represent the matrix

    1   2   3
    4   5   6
    7   8   9
    10  11  12

    The output should be:
    [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

    10  7   4   1
    11  8   5   2
    12  9   6   3

    :param mat:
    :return: list of lists - rotate matrix
    """
    if not mat:
        return []

    n = len(mat)
    m = len(mat[0])

    transposed_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    rotated_mat = [row[::-1] for row in transposed_mat]

    return rotated_mat


def is_valid_email(mail_str):
    """
    3 Kata

    This function returns True if the given mail is in the form:
    (username)@(domainname)

    Where
    * (username) must start with digit or an English character, and can contains only 0-9 a-z A-Z . or _
    * (domainname) is a real, existed domain - one that resolves to an actual ip address

    Hint: use socket.gethostbyname() to resolve a DNS in Python code

    :param mail_str: mail to check
    :return: bool: True if it's a valid mail (otherwise either False is returned or the program can crash)
    """
    import re
    import socket

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(pattern, mail_str):
            return False

    domain = mail_str.split('@')[1]

    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False


def pascal_triangle(lines):
    """
    3 Kata

    This function gets an integer representing the number of lines to print in a Pascal Triangle
    e.g. For n = 10 then following would be printed

                 1
                1 1
               1 2 1
              1 3 3 1
             1 4 6 4 1
           1 5 10 10 5 1
         1 6 15 20 15 6 1
        1 7 21 35 35 21 7 1
      1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    You are allowed to print the numbers not in a triangle shape:
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    :param lines: int
    :return: None
    """
    if lines <= 0:
        print([])
        return

    triangle = []
    for i in range(lines):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    for row in triangle:
        print(" ".join(map(str, row)))




def list_flatten(lst):
    """
    2 Kata

    This function gets a list of combination of integers or nested lists
    e.g.
    [1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0], [3]]

    The functions should return a flatten list (including all nested lists):
    [1, 1, 2, 4, 0, 5, 6, 5, 4, 34, 0, 3]

    :param lst: list of integers of another list
    :return: flatten list
    """
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(list_flatten(item))
        elif item != []:
            flattened_list.append(item)
    return flattened_list





def str_compression(text):
    """
    2 Kata

    This function gets a text (string) and returns a list representing the compressed form of the text.
    e.g.
    text = 'aaaaabbcaasbbgvccf'

    The output will be:
    ['a', 5, 'b', 2, 'c', 'a', 2, 's', 1, 'b', 2, 'g', 'v', 'c', 2, 'f']

    Since 'a' appears 5 times in consecutively, 'b' 2 times etc...
    Note that sequences of length 1 don't necessarily have the number 1 after the character (like 'c' before 'a')

    :param text: str
    :return: list representing the compressed form of the string
    """
    compressed = []
    current_char = None
    count = 0
    for char in text:
        if char == current_char:
            count += 1
        else:
            if current_char is not None:
                compressed.append(current_char)
                if count > 1:
                    compressed.append(count)
            current_char = char
            count = 1
    if current_char is not None:
        compressed.append(current_char)
        if count > 1:
            compressed.append(count)
    return compressed



def strong_pass(password):
    """
    1 Kata

    A password is considered strong if it satisfies the following criteria:
    1) Its length is at least 6.
    2) It contains at least one digit.
     3) It contains at least one lowercase English character.
    4) It contains at least one uppercase English character.
    5) It contains at least one special character. The special characters are: !@#$%^&*()-+

    This function returns True if the given password is strong enough
    """
    import string
    if len(password) < 6:
        return False

    has_digit = any(char in string.digits for char in password)
    has_lowercase = any(char in string.ascii_lowercase for char in password)
    has_uppercase = any(char in string.ascii_uppercase for char in password)
    has_special = any(char in string.punctuation for char in password)

    return has_digit and has_lowercase and has_uppercase and has_special


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))
    print(valid_parentheses('({)(){9(({[[[)[)'))
    print(valid_parentheses('[[{()'))
    print(valid_parentheses('('))
    print(valid_parentheses(''))


    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(7))
    print(fibonacci_fixme(6))
    print(fibonacci_fixme(5))
    print(fibonacci_fixme(4))
    print(fibonacci_fixme(3))
    print(fibonacci_fixme(2))
    print(fibonacci_fixme(1))
    print(fibonacci_fixme(0))
    print(fibonacci_fixme(-1))


    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))

    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{port: 8080}}', 'port: 9999'))


    print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('default.json', 'local.json'))
    #
    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))
    print(monotonic_array([9, 8, 7, 6]))
    print(monotonic_array([1.1, 1.2, 1.3, 1.4]))
    print(monotonic_array(['a', 'b', 'c', 'd']))
    print(monotonic_array([0, 0, 0, 0]))
    print(monotonic_array([]))
    print(monotonic_array(['c', 'd', 'z', 'k']))
    print(monotonic_array([1.8, 1.6, 1.9]))
    print(monotonic_array([-1, -2, -3, -4]))


    print('\nmatrix_avg:\n--------------------')
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0,1]))
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    #
    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))
    print(merge_sorted_lists([0, 6, 8, 4, -3,-7], [-100, 80, 10, 20]))
    print(merge_sorted_lists(['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']))

    print('\nlongest_common_substring:\n--------------------')
    print(longest_common_substring('abcdefg', 'bgtcdesd'))
    print(longest_common_substring('.ksndknakgnbksjbv', 'wkdcnslknakgnddkd'))
    print(longest_common_substring('', ''))
    print(longest_common_substring('sdjghsjdgh1234sdghnsih', 'djfkslcnrm1234sdghnfxg'))

    print('\nlongest_common_prefix:\n--------------------')
    print(longest_common_prefix('abcd', 'ttty'))
    print(longest_common_prefix('abcd', 'adcd'))
    print(longest_common_prefix('1256', '1234'))
    print(longest_common_prefix('', ''))


    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
    print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))
    print(is_valid_email(''))
    print(is_valid_email('osher@walle.com'))
    print(is_valid_email('oshr@gmail.com'))


    print('\npascal_triangle:\n--------------------')
    print(pascal_triangle(4))
    print(pascal_triangle(5))
    print(pascal_triangle(6))
    print(pascal_triangle(7))
    print(pascal_triangle(11))

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))
    print(str_compression('abbccddddtVeeeeesffffff'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
    print(strong_pass('Aa!2bcD'))
