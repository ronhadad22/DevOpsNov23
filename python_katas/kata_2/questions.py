from math import sqrt
import tarfile
import os
from datetime import datetime
import json
import re
import socket

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
    mapping = {')' : '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not  stack or mapping[char] != stack.pop():
                return False
        else:
            continue

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
    # fib_seq = [0, 1]
    # for i in range(2, n):
    #     fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    # return fib_seq[:n]
    # n = n - 1
    # if n <= 1:
    #     return 1
    # else:
    #     return fibonacci_fixme(n - 1) + fibonacci_fixme(n - 2)

    PHI = (1 + sqrt(5)) / 2
    return int(PHI ** n / sqrt(5) + 0.5)

def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    names_appears = {}

    def handle_name(name):
       #if name appears in dict, add value of 1
       if name in names_appears:
           names_appears[name] += 1
        #if not, creates with value 1
       else:
           names_appears[name] = 1


    with open(file_path ,"r") as file:
        names_in_file = file.read().splitlines()

    for name in names_in_file:
        handle_name(name)


    return max(names_appears, key=names_appears.get)


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
    # Get the directory name from the dir_path
    dir_name = os.path.basename(dir_path)

    # Generate the backup file name with the format specified
    date_today = datetime.today().strftime('%Y-%m-%d')
    backup_file_name = f'backup_{dir_name}_{date_today}.tar.gz'

    # Create a tar.gz file for backup
    with tarfile.open(backup_file_name, 'w:gz') as tar:
        # Add all files and directories in the given directory to the archive
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
    #Check if the file exists
    if os.path.exists(file_path):
        print(f"Changing text in file {file_path}")
        #Opening the file to read it's content
        with open(file_path, 'r') as file:
            file_text = file.read()
        #Modifying the text
        modified_text = file_text.replace(text, replace_text)
        with open(file_path, 'w') as file:
            file.write(modified_text)
        return "Text changed"
    else:
        return "File not found"



    

def json_configs_merge(*json_path):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """
    merged_data = {}

    # Iterate over the provided JSON file paths
    for path in json_path:
        # Read the content of each JSON file and parse it as a dictionary
        with open(path, 'r') as file:
            data = json.load(file)

        # Merge the data from the current file into the merged_data dictionary
        merged_data.update(data)

    return merged_data


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    if isinstance(lst, list):
        increasing = decreasing = True
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                increasing = False
            if lst[i] > lst[i-1]:
                decreasing = False
        return increasing or decreasing
    elif isinstance(lst, str):
        return "Not an integar"
    else:
        return "Not a list"


def matrix_avg(mat, rows=[0, 1, 2]):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """
    if not mat:
        return None

    total_sum = 0
    count = 0

    for row_index in rows:
        for element in mat[row_index]:
            total_sum += element
            count += 1

    # Calculate the average
    average = total_sum / count
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
    i = 0  # Index for l1
    j = 0  # Index for l2

    # Merge the lists until reaching the end of either list
    while i < len(l1) and j < len(l2):
        # Compare the elements at the current indices of l1 and l2
        if l1[i] <= l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1

    # Append the remaining elements of l1, if any
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1

    # Append the remaining elements of l2, if any
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
    # Initialize a table to store lengths of longest common suffixes
    # of substrings. Initialize all values to 0.
    table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    # Initialize the variable to store the length of the longest common substring
    longest_length = 0
    # Initialize the variable to store the ending index of the longest common substring
    ending_index = 0
    # Iterate over the characters of str1
    for i in range(1, len(str1) + 1):
        # Iterate over the characters of str2
        for j in range(1, len(str2) + 1):
            # If the characters match
            if str1[i - 1] == str2[j - 1]:
                # The value in the table is 1 plus the value in the previous diagonal cell
                table[i][j] = table[i - 1][j - 1] + 1
                # If the length of the current common substring is longer than the longest
                # common substring found so far
                if table[i][j] > longest_length:
                    # Update the length of the longest common substring
                    longest_length = table[i][j]
                    # Update the ending index of the longest common substring
                    ending_index = i
            else:
                # If the characters don't match, the value in the table is 0
                table[i][j] = 0
    # Return the longest common substring
    return str1[ending_index - longest_length:ending_index]


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
    # Find the minimum length among the two input strings
    min_length = min(len(str1), len(str2))

    # Initialize an empty string to store the longest common prefix
    longest_prefix = ""

    # Iterate over the characters of the strings until the minimum length
    for i in range(min_length):
        # If the characters at the same index in both strings are equal
        if str1[i] == str2[i]:
            # Add the character to the longest prefix
            longest_prefix += str1[i]
        else:
            # If the characters are not equal, break the loop
            break

    # Return the longest common prefix found
    return longest_prefix


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
    #Transpose the Matrix
    transposed_mat = list(zip(*mat))
    # Reverse each row of the transposed matrix
    rotated_mat = [list(reversed(row)) for row in transposed_mat]
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
    # Define the regular expression pattern for the email format
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the email matches the pattern
    if re.match(pattern, mail_str):
        # Extract the domain name from the email
        domain = mail_str.split('@')[1]
        try:
            # Try to resolve the domain name to an IP address
            ip_address = socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            # If the domain name cannot be resolved, return False
            return False
    else:
        # If the email does not match the pattern, return False
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

    # Iterate over each line
    for i in range(lines):
        # Calculate the number of spaces to print before the numbers
        num_spaces = 2 * (lines - i - 1)
        # Print the leading spaces
        print(" " * num_spaces, end="")

        # Initialize the first value in the row to 1
        coef = 1

        # Iterate over each element in the current row
        for j in range(0, i + 1):
            # Print the coefficient value and add leading spaces
            print("{:4d}".format(coef), end="")

            # Calculate the next coefficient value using the previous one
            coef = coef * (i - j) // (j + 1)

        # Move to the next line after printing all elements in the current row
        print()


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
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(list_flatten(item))
        else:
            flattened.append(item)
    return flattened



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
    count = 1

    # Iterate through the characters of the text starting from the second character
    for i in range(1, len(text)):
        # If the current character is the same as the previous character, increment the count
        if text[i] == text[i - 1]:
            count += 1
        else:
            # If the current character is different from the previous character, add the previous character
            # and its count to the compressed list
            compressed.append(text[i - 1])
            # If the count is greater than 1, add it to the compressed list
            if count > 1:
                compressed.append(count)
            # Reset the count for the new character
            count = 1

    # Add the last character and its count to the compressed list
    if text:
        compressed.append(text[-1])
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
    # Define regex patterns for each of the criteria
    length_regex = r'.{6,}'
    digit_regex = r'\d'
    lowercase_regex = r'[a-z]'
    uppercase_regex = r'[A-Z]'
    special_regex = r'[!@#$%^&*()-+]'

    # Check if the password satisfies all criteria using regex
    if (re.search(length_regex, password) and
            re.search(digit_regex, password) and
            re.search(lowercase_regex, password) and
            re.search(uppercase_regex, password) and
            re.search(special_regex, password)):
        return True
    else:
        return False


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))
    print(valid_parentheses('[[[[]'))
    print(valid_parentheses('[]]][{}}}}{))((()'))

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(0))
    print(fibonacci_fixme(1))
    print(fibonacci_fixme(2))
    print(fibonacci_fixme(3))
    print(fibonacci_fixme(4))

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))


    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

    print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('default.json', 'local.json', 'default_local.json'))


    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))
    print(monotonic_array([1, 2, 3, 4, 5, 6, 7]))
    print(monotonic_array([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(monotonic_array(["Hummus", "Tahini"]))


    print('\nmatrix_avg:\n--------------------')
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(matrix_avg([[2, 2, 2], [6, 6, 6], [4, 4, 4]]))

    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))

    print('\nlongest_common_substring:\n--------------------')
    print(longest_common_substring('abcdefg', 'bgtcdesd'))

    print('\nlongest_common_prefix:\n--------------------')
    print(longest_common_prefix('abcd', 'ttty'))
    print(longest_common_prefix('12345', '12345'))

    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))
    print(is_valid_email('israel.aharoni@yandex.ru'))
    print(is_valid_email('israel.aharoni@timapple.ive'))

    print('\npascal_triangle:\n--------------------')
    pascal_triangle(4)

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
