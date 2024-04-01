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
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

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
    You should (1) correct the for statement and (2) swap two lines, so that the correct fibonacci element will be returned
    """
    if n <= 2:
        return 1

    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    name_counts = {}

    # Read names from the file
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            name_counts[name] = name_counts.get(name, 0) + 1

    # Find the most frequent name
    max_count = 0
    most_frequent = None
    for name, count in name_counts.items():
        if count > max_count:
            max_count = count
            most_frequent = name

    return most_frequent


import os
import tarfile
import datetime

def files_backup(dir_path: str) -> str:
    """
    Generates a .gz file containing all the files in the given directory.

    Args:
        dir_path (str): Path to the directory.

    Returns:
        str: The backup file name in the format 'backup_<dir_name>_<yyyy-mm-dd>.tar.gz'.
    """
    # Get the directory name
    dir_name = os.path.basename(dir_path)

    # Get the current date in yyyy-mm-dd format
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Create the backup file name
    backup_file_name = f"backup_{dir_name}_{current_date}.tar.gz"

    # Create a tar.gz file containing all files in the directory
    with tarfile.open(backup_file_name, "w:gz") as tar:
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, dir_path))

    return backup_file_name


def replace_in_file(file_path: str, text: str, replace_text: str) -> None:
    """
    Replaces all occurrences of 'text' with 'replace_text' in the given text file.

    Args:
        file_path (str): Path to the text file.
        text (str): Text to search for.
        replace_text (str): Text to replace with.

    Returns:
        None
    """
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Replace occurrences of 'text' with 'replace_text'
        updated_content = file_content.replace(text, replace_text)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print(f"Replaced '{text}' with '{replace_text}' in {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


import json


def json_configs_merge(*json_paths):
    merged_json = {}  # Initialize an empty dictionary to store the merged JSON data

    # Iterate over each JSON file path
    for path in json_paths:
        # Open the file and load its content as a dictionary
        with open(path, 'r') as file:
            json_data = json.load(file)

        # Merge the loaded JSON data into the merged_json dictionary
        merged_json.update(json_data)

    return merged_json

def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    if len(lst) <= 1:
        return True

    increasing = decreasing = True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        elif lst[i] > lst[i - 1]:
            decreasing = False

    return increasing or decreasing


def matrix_avg(mat, rows=None):
    """
    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    if rows is None:
        rows = range(3)

    total_sum = 0
    total_elements = 0

    for row_index in rows:
       if 0 <= row_index < 3:
            row = mat[row_index]
            total_sum += sum(row)
            total_elements += len(row)
        else:
            print("Invalid row index encountered:", row_index)
            raise IndexError("Invalid row index: {}".format(row_index))

    if total_elements == 0:
        return 0  # Avoid division by zero

    return total_sum / total_elements
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
    i = j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    # Add remaining elements from l1, if any
    merged_list.extend(l1[i:])

    # Add remaining elements from l2, if any
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
    # Initialize a 2D matrix to store the lengths of common substrings
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to keep track of the longest common substring
    max_len = 0
    end_index = 0

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i

    # Extract the longest common substring
    longest_substring = str1[end_index - max_len:end_index]
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
    # Initialize variables
    i = 0
    prefix = ""

    # Iterate through characters in both strings
    while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
        prefix += str1[i]
        i += 1

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
        return mat  # Return the matrix unchanged if it is empty

    rows, cols = len(mat), len(mat[0])
    rotated = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - i - 1] = mat[i][j]

    return rotated


import re
import socket

def is_valid_email(mail_str):
    """
    Returns True if the given mail is in the form:
    (username)@(domainname)

    Where:
    - (username) must start with a digit or an English character and can contain only 0-9, a-z, A-Z, ., or _
    - (domainname) is a real, existing domain that resolves to an actual IP address

    :param mail_str: str - email address to check
    :return: bool - True if it's a valid email, otherwise False
    """
    # Regular expression pattern for valid email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the email matches the pattern
    if re.match(pattern, mail_str):
        try:
            # Extract domain name from the email
            domain = mail_str.split("@")[1]
            # Resolve the domain to an IP address
            socket.gethostbyname(domain)
            return True
        except (socket.gaierror, IndexError):
            # Invalid domain or unable to resolve
            return False
    else:
        return False


def pascal_triangle(lines):
    """
    Generates and prints the Pascal Triangle for the given number of lines.

    :param lines: int - number of lines to print
    :return: None
    """
    triangle = []
    for i in range(lines):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle

def list_flatten(lst):
    """
    Flatten a list of combination of integers or nested lists.
    """
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

    def flatten_helper(sublist):
        """
        Recursive helper function to flatten nested lists.

        :param sublist: list
        :return: list
        """
        result = []
        for item in sublist:
            if isinstance(item, list):
                result.extend(flatten_helper(item))
            else:
                result.append(item)
        return result

    return flatten_helper(lst)


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
    if not text:
        return compressed

    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed.append(current_char)
            if count > 1:
                compressed.append(count)
            current_char = text[i]
            count = 1

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
    if len(password) < 6:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in '!@#$%^&*()-+' for char in password)

    return has_digit and has_lower and has_upper and has_special


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