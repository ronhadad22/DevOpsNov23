import os
import tarfile
from datetime import datetime
import socket
import json
import re


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
    # opensb is keeping open brackets , used ones means it have closure is pop out so if opensb is have value in end it fasle
    opensb = []
    dict = {')':'(','}':'{',']':'['}

    for ch in s :
        if ch in dict.values():
            opensb.append(ch)
        elif ch in dict.keys():
            if not opensb or dict[ch] != opensb.pop():
                return False
        continue

    return not opensb



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


    if n <= 0:
        return 0
    if n <= 2:
        return 1
    las,new = 1,1

    for a in range(3 ,n+1):

        las,new = new,new+las



    return new


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """
    bigst = 0
    most_c_name = ''
    with open(file_path, 'r') as file:
        names = {}
        for line in file:
            word = line.split()
            if word:
                first = word[0].lower()
                names[first] = names.get(first, 0) + 1

        for word, count in names.items():
            if count >= bigst:
                bigst = count
                most_c_name = word

    return most_c_name


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

    if not os.path.isdir(dir_path):
        print(f"Error: {dir_path} is not a valid directory.")
        return None

    folder_name = os.path.basename(dir_path)
    custom_date = datetime(2024, 4, 3)
    formatted_date = custom_date.strftime("%Y-%m-%d")
    output_filename = f"backup_{folder_name}_{formatted_date}.tar.gz"
    output_path = os.path.join(os.getcwd(), output_filename)

    with tarfile.open(output_path, "w:gz") as tar:
        tar.add(dir_path, arcname=folder_name)


    return str(output_filename)



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

    merged_dict = {}

    for path in json_paths:
        if path :
         with open(path, 'r') as file:
            config_dict = json.load(file)
            merged_dict.update(config_dict)

    return merged_dict



def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """
    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


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
    total_sum = 0
    count = 0

    if rows is not None:
        for row in rows:
            total_sum += sum(mat[row])
            count += len(mat[row])
    else:
        for row in mat:
            total_sum += sum(row)
            count += len(row)

    if count == 0:
        return 0.0

    return total_sum / count


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
    i , j = 0,0
    l3=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            l3.append(l1[i])
            i+=1

        elif l2[j]<l1[i]:
            l3.append(l2[j])
            j+=1

    l3.extend(l1[i:])
    l3.extend(l2[j:])
    return l3


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
    # Initialize a matrix to store the lengths of longest common substrings
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length of longest common substring and its ending position
    max_length = 0
    end_position = 0

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    start_position = end_position - max_length
    return str1[start_position:end_position]




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
    prefix = ""

    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            break
        prefix += char1

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

    transposed_mat = list(zip(*mat))

    rotated_mat = [list(row[::-1]) for row in transposed_mat]

    return rotated_mat




    return None


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


    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(pattern, mail_str):
        return False

    username, domainname = mail_str.split('@')

    try:
        ip_address = socket.gethostbyname(domainname)
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
    triangle = [[1]]

    for i in range(1, lines):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    for row in triangle:
        print(" ".join(map(str, row)).center(lines * 2 - 1))
    return None


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
    if not text:
        return []

    compressed = []
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

    has_digit = False
    has_lowercase = False
    has_uppercase = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char in '!@#$%^&*()-+':
            has_special = True

    return has_digit and has_lowercase and has_uppercase and has_special


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses(''))

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(5))

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))

    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

    print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('default.json', 'local.json'))

    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([-1, -2, -3, -6, -8, -9, -10,0]))

    print('\nmatrix_avg:\n--------------------')
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
    print(matrix_avg([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 9, 23]))

    print('\nlongest_common_substring:\n--------------------')
    print(longest_common_substring('abcbeny1defg', 'benybgtcdesdbeny1'))

    print('\nlongest_common_prefix:\n--------------------')
    print(longest_common_prefix('The Linux kernel is an amazing software', 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'))

    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('beny.sdad@gmail.com'))

    print('\npascal_triangle:\n--------------------')
    print(pascal_triangle(10))

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0], [3]]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaaabbcaasbbgvccf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('aasdadA2@'))
