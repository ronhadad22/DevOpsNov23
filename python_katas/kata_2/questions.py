def valid_parentheses(s):
    """
    3 Kata

    This function gets a string containing just the characters '(', ')', '{', '}', '[' and ']',
    and determines if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    e.g.
    s = '[[{()}](){}]'  -> True
    s = ']}'          -> False
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False

    return len(stack) == 0
    pass


def fibonacci_fixme(n):
    """
    2 Kata

    A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8, 13....
    The first two terms are 1 and 1. All other terms are obtained by adding the preceding two terms.

    This function should return the n'th element of fibonacci sequence. As following:

    fibonacci_fixme(1) -> 1
    fibonacci_fixme(2) -> 1
    fibonacci_fixme(3) -> 2
    fibonacci_fixme(4) -> 3
    fibonacci_fixme(5) -> 5

    But it doesn't (it has some bad lines in it...)
    You should (1) correct the for statement and (2) swap two lines, so that the correct fibonacci element will be returned
    """
    # Initialize the first two elements of the Fibonacci sequence
    fib_1, fib_2 = 1, 1

    # Check if n is 1 or 2, return 1 for these cases
    if n == 1 or n == 2:
        return 1

    # Iterate from the 3rd element to the n'th element
    for _ in range(3, n + 1):
        # Calculate the next Fibonacci number by adding the previous two numbers
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    # Return the n'th element of the Fibonacci sequence
    return fib_2
    pass


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    # Dictionary to store the count of each name
    name_counts = {}

    # Open the file and read names line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespaces and convert name to lowercase
            name = line.strip()
            # Increment count for the name in the dictionary
            name_counts[name] = name_counts.get(name, 0) + 1

    # Check if the file was empty
    if not name_counts:
        return None

    # Find the name with the highest count
    most_frequent_name = max(name_counts, key=name_counts.get)

    return most_frequent_name




import os
import tarfile
from datetime import datetime
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
    # Extract the directory name from the given path
    dir_name = os.path.basename(os.path.normpath(dir_path))

    # Generate the current date in yyyy-mm-dd format
    date_str = datetime.now().strftime('%Y-%m-%d')

    # Create the backup file name
    backup_file_name = f'backup_{dir_name}_{date_str}.tar.gz'

    # Create the full path for the backup file to be stored
    backup_file_path = os.path.join(os.path.dirname(dir_path), backup_file_name)

    # Creating a tar.gz archive
    with tarfile.open(backup_file_path, "w:gz") as tar:
        tar.add(dir_path, arcname=dir_name)

    # Return the name of the backup file
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
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace the specified text
    modified_content = content.replace(text, replace_text)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

import json
import os
def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """
    merged_data = {}
    for json_path in json_paths:
        with open(json_path, 'r') as file:
            data = json.load(file)
            merged_data.update(data)
    return merged_data
# Define full paths to the JSON files
default_json_path = r'C:\Users\ronel\DevOps_katas2\python_katas\kata_2\default.json'
local_json_path = r'C:\Users\ronel\DevOps_katas2\python_katas\kata_2\local.json'


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    # Check if the list is monotonically increasing
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    # Check if the list is monotonically decreasing
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    # Return True if either increasing or decreasing
    return increasing or decreasing


def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    total = 0  # Sum of the elements
    count = 0  # Count of elements included

    # If 'rows' is not specified, calculate the average of all elements
    if rows is None:
        for row in mat:
            for elem in row:
                total += elem
                count += 1
    else:
        # Include only the specified rows in the average calculation
        for row_index in rows:
            for elem in mat[row_index]:
                total += elem
                count += 1

    # Calculate the average and return as an integer
    avg = total / count
    return avg


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
    i, j = 0, 0

    # Iterate through both lists until one is exhausted
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    # Append remaining elements from the non-empty list
    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])

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
    # Initialize variables to store the length of the longest common substring
    max_length = 0
    ending_index = 0

    # Initialize a matrix to store the lengths of the longest common substrings
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Iterate over each character in the strings
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    ending_index = i
            else:
                matrix[i][j] = 0

    # Construct the longest common substring
    longest_substring = str1[ending_index - max_length: ending_index]

    return longest_substring


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
    # Initialize an empty string to store the longest common prefix
    prefix = ""

    # Iterate over the characters of both strings simultaneously
    for char1, char2 in zip(str1, str2):
        # If the characters match, append the character to the prefix
        if char1 == char2:
            prefix += char1
        # If the characters don't match, break the loop
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
    # First, transpose the matrix.
    # Transposition means converting rows into columns.
    transposed = list(zip(*mat))

    # Then, reverse each row of the transposed matrix to get a clockwise rotation.
    rotated = [list(row[::-1]) for row in transposed]

    return rotated


import re
import socket
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
    # Split the email into username and domain parts
    parts = mail_str.split('@')
    if len(parts) != 2:
        return False

    username, domain = parts

    # Validate username
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9._]*$', username):
        return False

    # Validate domain name
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return False

    return True


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
    triangle = []

    for n in range(lines):
        # Create a new row
        row = []
        for k in range(n + 1):
            # Calculate the binomial coefficient
            coefficient = factorial(n) // (factorial(k) * factorial(n - k))
            row.append(coefficient)
        triangle.append(row)

    # Print the Pascal's triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(lines * 3))

# Helper function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


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
        else:
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
    # Initialize an empty list to hold the compressed form
    compressed = []

    # Initialize a counter to 1; this will count consecutive characters
    count = 1

    # Loop through the text by index
    for i in range(len(text)):
        # Check if we are not at the last character and the current character is the same as the next one
        if i + 1 < len(text) and text[i] == text[i + 1]:
            # If so, increment the counter
            count += 1
        else:
            # If the current character is not the same as the next one or we're at the last character,
            # append the current character to the compressed list
            compressed.append(text[i])

            # If the count is greater than 1, also append the count
            if count > 1:
                compressed.append(count)

            # Reset the counter to 1 for the next character sequence
            count = 1

    # Return the compressed list
    return compressed


import re
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
    # Check the length of the password
    if len(password) < 6:
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()\-\+]', password):
        return False

    # If all conditions are met, return True
    return True



if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(6))

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))

    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{REGISTRY_URL}}', 'mnist-pred:0.0.1'))

    print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('default.json', 'local.json'))

    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))

    print('\nmatrix_avg:\n--------------------')
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))

    print('\nlongest_common_substring:\n--------------------')
    print(longest_common_substring('abcdefg', 'bgtcdesd'))

    print('\nlongest_common_prefix:\n--------------------')
    print(longest_common_prefix('abcd', 'abcdefghi'))

    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))

    print('\npascal_triangle:\n--------------------')
    pascal_triangle(10)

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))