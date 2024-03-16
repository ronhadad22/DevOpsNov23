import math



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
    if (len(word) == 0):
        return word
    leng = len(word)
    if leng >=3 :
        s_index = len(word)-3
        substring = word[s_index:]
        if substring == 'ing':
            return word+'ly'
        else : return word+'ing'
    else :
        return word

def words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """
    if len(words) == 0:
        return ''

    res = ''
    for w in words:
        if w == '':
            res = res
        elif w == ' ':
            res = res
        else:
            res += w+' '

    if res[len(res) - 1] == ' ':
        res = res.rstrip(res[len(res) - 1])
    if res[0] == ' ':
        res = res.rstrip(res[0])
    return res


def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.

    """
    if len(words) == 0 :
        return words

    res =''
    leng = len(words)
    while leng :
       if words[leng-1] == '':
           res=res
       elif words[leng-1] == ' ':
           res=res
       else : res = res+words[leng-1]+' '
       leng-=1
    if res[len(res) - 1] == ' ':
        res = res.rstrip(res[len(res) - 1])
    if res[0] == ' ':
        res = res.rstrip(res[0])
    return res


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
    been = set()
    if len(some_str) == 0 :
        return True
    for each in some_str:
        if each in been:
            return False
        else:been.add(each)

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
    i=0
    res=[]
    if len(elements) == 0 :
        return elements
    else :
        for each in elements :
            if i == 0:
                res.append(None)
                i+=1
            else :
                res.append(elements[i]-elements[i-1])
                i+=1
    return res



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
    if num == 2 :
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
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
    if num < 0 :
        return False
    num_str = str(num)
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    if reversed_num == num:

        return True
    else:
        return False



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

    listmen = list(men.items())
    listwomen = list(women.items())
    matchp = ()

    if len(listmen) == 0 or len(listwomen) == 0:
        return matchp
    smalldif = abs(listmen[0][1] - listwomen[0][1])
    for mens in listmen :
        for womens in listwomen:
            if smalldif > abs(mens[1] - womens[1]) :
                smalldif = abs(mens[1] - womens[1])
                matchp=(mens[0],womens[0])
            elif smalldif == abs(mens[1] - womens[1]) :
                matchp = (mens[0], womens[0])+matchp


    return matchp


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

    stname = ''
    hgrade = 0
    listgrades = list(grades.items())
    for student in listgrades:
            if hgrade == 0:
                hgrade = student[1]
            if student[1] > hgrade:
                hgrade = student[1]
                stname = student[0]
            elif student[1] == hgrade:
                stname += ' ' + student[0]  # Concatenate student names with a space
    return stname

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
    dictoprint = list(some_dict.items())

    if words_concatenation!=None:
        print("Key".ljust(10) + "Value")
        print("-------------")

        for eachname in dictoprint:
            formatted_name = eachname[0].ljust(10)
            print(f"{formatted_name}{eachname[0]}")

    else:
        print("Key".ljust(10) + "Value")
        print("-------------")

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
    dict1 = {**dict1,**dict2}
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

    num = 7
    listnum = []
    mark =1
    if n==0 :
        return [0]
    if abs(n)<7:
        return listnum
    if n<0 :
        mark = -1
    if mark == -1:
        listnum.append(0)
    while num<=abs(n):

        if num%7==0:
          listnum.append(num*mark)
        elif num %10 == 7:
          listnum.append(num*mark)
        elif int(num/10) ==7:
          listnum.append(num*mark)
        num+=1




    return listnum


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    encrypted_text = ''
    for char in str_to_encrypt:
        if char.isalpha():
            if char.islower():
                offset = ord('a')
            else:
                offset = ord('A')
            # Apply the Caesar cipher shift
            encrypted_char = chr(((ord(char) - offset) + 3) % 26 + offset)
        else:
            encrypted_char = char  # Spaces remain unchanged
        encrypted_text += encrypted_char
    return encrypted_text


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
    num=0
    if len(digits_str)==0:
        return 0
    else:
        for ch in digits_str:
            num+=int(ch)

    return num


if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2, 3, 4, 5, 6]))

    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))

    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', '', 'home']))

    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))

    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))
    print(is_unique_string(''))
    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))

    print('\nprime_number:\n--------------------')
    print(prime_number(87))
    print(prime_number(17))

    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(-1))
    print(palindrome_num(577))

    print('\npair_match:\n--------------------')
    print(pair_match(
        {
            "John": 20,
            "Abraham": 45
        },
        {
            "July": 18,
            "Kim": 20
        }
    ))



    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))

    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 0,
        "Hen": 0,
        "Natan": 0,
        "Efraim": 0,
        "Rachel": 0
    }))

    print('\nprint_dict_as_table:\n--------------------')
    print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    })

    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))

    print('\nseven_boom:\n--------------------')
    print(seven_boom(77))

    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))

    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('10101001'))

