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
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to hold matching pairs
    brackets = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the string
    for char in s:
        # If the character is an opening bracket
        if char in brackets.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets:
            # If the corresponding opening bracket is not on top of the stack or stack is empty
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()

    # If the stack is empty, all the brackets are balanced
    return not stack


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
    You should (1) correct the for statement and (2) swap two lines, so that the correct
    fibonacci element will be returned
    """
    # Base cases for the first two elements of the sequence
    if n == 1 or n == 2:
        return 1

    # Initialize the first two elements
    prev, curr = 1, 1

    # Calculate the n'th element
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


from collections import Counter
def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    with open(file_path, 'r') as file:
        # Read all lines and strip any leading/trailing whitespace
        names = [line.strip() for line in file]

    # Use Counter to count the frequency of each name
    name_counts = Counter(names)

    # Find the name(s) with the highest frequency
    max_frequency = max(name_counts.values())
    most_frequent_names = [name for name, count in name_counts.items() if count == max_frequency]

    # Return one of the most frequent names
    return most_frequent_names[0] if most_frequent_names else None


import tarfile
from datetime import datetime
import os
def files_backup(dir_path):
    """
    Creates a .gz file containing all the files in the given directory.
    The backup file name is in the format 'backup_<dir_name>_<yyyy-mm-dd>.tar.gz'.

    :param dir_path: string - path to a directory
    :return: str - the backup file name
    """
    # Extract the directory name from the given path
    dir_name = os.path.basename(os.path.normpath(dir_path))
    # Get the current date in yyyy-mm-dd format
    date_str = datetime.now().strftime('%Y-%m-%d')
    # Create the backup file name
    backup_file_name = f'backup_{dir_name}_{date_str}.tar.gz'

    # Create a tarball and compress it into a .gz file
    with tarfile.open(backup_file_name, 'w:gz') as tar:
        tar.add(dir_path, arcname=dir_name)

    return backup_file_name


import json
def json_configs_merge(*json_paths):
    """
    Reads multiple JSON files and merges them into a single dictionary.
    Files are merged in the order they are provided.

    :param json_paths: tuple - paths to JSON files
    :return: dict - the merged JSON configurations
    """
    merged_config = {}
    for path in json_paths:
        with open(path, 'r') as json_file:
            # Load the JSON file content into a dictionary
            config = json.load(json_file)
            # Update the merged configuration with the current file's content
            merged_config.update(config)

    return merged_config


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    # Check if the list is empty or has one element
    if len(lst) < 2:
        return True

    # Determine if the list is increasing or decreasing based on the first two elements
    increasing = lst[1] > lst[0]
    decreasing = lst[1] < lst[0]

    # Check the rest of the list
    for i in range(1, len(lst)):
        if increasing and lst[i] < lst[i - 1]:
            return False
        if decreasing and lst[i] > lst[i - 1]:
            return False

    return True


def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    if rows is not None:
        mat = [mat[row] for row in rows]

    # Flatten the matrix and calculate the average
    flat_list = [item for sublist in mat for item in sublist]
    return sum(flat_list) / len(flat_list)


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
    # Initialize pointers for both lists
    i, j = 0, 0
    merged_list = []

    # Loop until one list is exhausted
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    # Append any remaining elements from l1 or l2
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
    # Create a matrix to store lengths of longest common suffixes
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    longest = 0  # Length of the longest common substring
    lcs_end = 0  # End index of the longest common substring in str1

    # Build the matrix in a bottom-up manner
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    lcs_end = i
            else:
                dp[i][j] = 0

    # Return the longest common substring
    return str1[lcs_end - longest: lcs_end]


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
    # Initialize the index for the shortest length
    min_length = min(len(str1), len(str2))
    # Initialize the longest common prefix variable
    lcp = ""

    # Iterate over the strings up to the length of the shortest one
    for i in range(min_length):
        if str1[i] == str2[i]:
            lcp += str1[i]
        else:
            break

    return lcp


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
    # Transpose the matrix
    transposed = [list(row) for row in zip(*mat)]
    # Reverse each row to get the clockwise rotation
    rotated = [row[::-1] for row in transposed]
    return rotated


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
    # Regex pattern for validating the email format
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if not re.match(pattern, mail_str):
        return False

    # Extract the domain name from the email
    domain = mail_str.split('@')[1]

    try:
        # Attempt to resolve the domain name to an IP address
        socket.gethostbyname(domain)
        return True
    except socket.error:
        # If the domain does not resolve, return False
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
    triangle = [[1]]

    for _ in range(1, lines):
        # Start with 1
        row = [1]
        # Calculate the in-between values as the sum of two numbers above it
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        # End with 1
        row.append(1)
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(' '.join(map(str, row)))


# Example usage:
pascal_triangle(10)


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
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            # If the item is a list, extend flat_list with the flattened item
            flat_list.extend(list_flatten(item))
        else:
            # If the item is an integer, append it to flat_list
            flat_list.append(item)
    return flat_list


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
    # Initialize an empty list to store the compressed form
    compressed = []
    # Initialize a count variable
    count = 1

    # Iterate over the text using enumerate to get index and character
    for i, char in enumerate(text):
        # Check if we are not at the last character and if the current character is the same as the next one
        if i + 1 < len(text) and char == text[i + 1]:
            # If so, increment the count
            count += 1
        else:
            # If the character sequence ends, append the character and its count if count is more than 1
            compressed.append(char)
            if count > 1:
                compressed.append(count)
            # Reset the count
            count = 1

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

    # Check for the presence of at least one digit
    if not re.search(r"\d", password):
        return False

    # Check for the presence of at least one lowercase English character
    if not re.search(r"[a-z]", password):
        return False

    # Check for the presence of at least one uppercase English character
    if not re.search(r"[A-Z]", password):
        return False

    # Check for the presence of at least one special character
    if not re.search(r"[!@#$%^&*()\-\+]", password):
        return False

    # If all conditions are met, return True
    return True

def replace_in_file(file_name, placeholder, replacement):
    # Read the content of the file
    with open(file_name, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(placeholder, replacement)

    # Write the file out again
    with open(file_name, 'w') as file:
        file.write(filedata)

    return f"The placeholder {placeholder} has been replaced with {replacement} in {file_name}."

# Example usage:
print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

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
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

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
    print(longest_common_prefix('abcd', 'ttty'))

    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))

    print('\npascal_triangle:\n--------------------')
    print(pascal_triangle(4))

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
