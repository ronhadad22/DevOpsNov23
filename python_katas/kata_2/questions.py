import os
from datetime import datetime
import tarfile
import json
import re
import socket
from math import sqrt


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

    closers_dict = {')': '(', '}': '{', ']': '['}

    opened = []

    def handle_char(c):
        if c == '(' or c == '{' or c == '[':
            opened.append(c)
            return True
        if c == ')' or c == '}' or c == ']':
            if len(opened) > 0 and opened[-1] == closers_dict[c]:
                opened.pop()
                return True
        return False

    for char in s:
        if not handle_char(char):
            return False
    return True


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

    # Based on this thread: https://stackoverflow.com/questions/6037472/can-a-fibonacci-function-be-written-to-execute-in-o1-time

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

    appearance_record = {}

    def handle_name(name):
        if name in appearance_record:
            appearance_record[name] += 1
        else:
            appearance_record[name] = 1

    with open(file_path) as file:
        # Using splitlines as it removes \n from the lines
        for name in file.read().splitlines():
            handle_name(name)

    return max(appearance_record, key=appearance_record.get)


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

    if len(os.listdir(dir_path)) < 0:
        return None

    tar_file_name = f'backup_{os.path.basename(dir_path)}_{datetime.today().date().isoformat()}.tar.gz'

    with tarfile.open(tar_file_name, "w:gz") as tar:
        tar.add(dir_path, arcname=os.path.basename(dir_path))

    return tar_file_name
    # Ask Ron where to save the compressed file
    # Ask compress empty directory
    # Ask to compess the dir or it's content

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

    try:
        with open(file_path, 'r+') as file:
            content = file.read()
            file.seek(0)
            file.truncate()
            file.write(content.replace(text, replace_text))

    except:
        return None
    

def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """

    def read_json_file(file_path):
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    result = {}
    for file_path in json_paths:
        result.update(read_json_file(file_path))

    return result

    # Ask Ron who overrided whom


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """

    direction = 0

    if not lst: return True

    for i in range(1, len(lst)):
        if direction == 0:
            if lst[i] > lst[i - 1]:
                direction = 1
            elif lst[i] < lst[i - 1]:
                direction = -1
        else:
            if direction < 0 and lst[i] > lst[i - 1]:
                return False
            if direction > 0 and lst[i] < lst[i - 1]:
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

    if not rows: rows = [0, 1, 2]

    def list_avg(lst):
        return sum(lst) / len(lst)

    avgs = []

    for rowIndex in rows:
        avgs.append(list_avg(mat[rowIndex]))

    return list_avg(avgs)
#     Ask Ron if default is all or nothing?

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

    last_index = 0
    for item2 in l2:
        while len(l1) > last_index and item2 > l1[last_index]:
            last_index += 1
        l1.insert(last_index, item2)

    return l1

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
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Initialize variables to keep track of the maximum length and ending position
    max_length = 0
    end_position = 0

    # Fill in the matrix
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    end_position = i

    # Extract the longest common substring
    return str1[end_position - max_length:end_position]


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

    return os.path.commonprefix([str1, str2])




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

    if not mat: return []

    rows, cols = len(mat), len(mat[0])
    rotated_mat = [[0] * rows for _ in range(cols)]  # Create a new matrix

    for i in range(rows):
        for j in range(cols):
            rotated_mat[j][rows - 1 - i] = mat[i][j]

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

    rx_patt = r"^[a-zA-Z0-9._]+@(\S+)"
    match = re.search(rx_patt, mail_str)

    if not match: return False

    try:
        ip = socket.gethostbyname(match.group(1))
        if ip: return True
        return False
    except:
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

    # Based on https://www.geeksforgeeks.org/pascal-triangle/

    # See https://www.geeksforgeeks.org/space-and-time-efficient-binomial-coefficient/
    # for details of this function

    def binomialCoeff(n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(0, k):
            res = res * (n - i)
            res = res // (i + 1)

        return res


    # Iterate through every line
    # and print entries in it
    for line in range(lines):
        line_list = []
        # Every line has number of
        # integers equal to line
        # number
        for i in range(line + 1):
            line_list.append(str(binomialCoeff(line, i)))
        print(' '.join(line_list))


def list_flatten(lst, flat_lst = None):
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

    if flat_lst is None:
        flat_lst = []

    for item in lst:
        if isinstance(item, list):
            list_flatten(item, flat_lst)
        else:
            flat_lst.append(item)

    return flat_lst


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
    
    if not text: return []

    output = []

    def get_last_char_pair():
        if not output: return None

        if isinstance(output[-1], int):
            return (output[-2], output[-1])
        return (output[-1], 1)

    for char in text:
        last_char_pair = get_last_char_pair()
        if not output or last_char_pair[0] != char:
            output.append(char)
        elif last_char_pair[1] == 1:
            output.append(2)
        else:
            output[-1] += 1

    return output


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
    if not password: return False
    
    re_pattern = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()\-+]).{6,}$' 

    if re.search(re_pattern, password):
        return True
    return False

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
    print(pascal_triangle(1))

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
    print(strong_pass('sdv'))
    print(strong_pass(None))
