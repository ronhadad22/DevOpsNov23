import unittest
from python_katas.kata_2 import questions
from python_katas.utils import unittest_runner

testers = ['ofri','denis','ron']

class TestValidParentheses(unittest.TestCase):
    """
    3 Katas
    """
pass



class TestFibonacciFixme(unittest.TestCase):
    """
    2 Katas
    """
    pass

class TestMostFrequentName(unittest.TestCase):
    pass

class TestFilesBackup(unittest.TestCase):
    """
    3 Katas
    """
    pass


class TestReplaceInFile(unittest.TestCase):
    """
    2 Katas
    """
    pass

class TestJsonConfigsMerge(unittest.TestCase):
    """
    2 Katas
    """
    pass

class TestMonotonicArray(unittest.TestCase):
    """
    1 Katas
        """
    pass


class TestMatrixAvg(unittest.TestCase):
    """
    2 Katas
    """
    pass


class TestMergeSortedLists(unittest.TestCase):
    """
    1 Katas
    """
    pass


class TestLongestCommonSubstring(unittest.TestCase):
    """
    4 Katas
    """
    pass


class TestLongestCommonPrefix(unittest.TestCase):
    """
    1 Katas
    """
    pass

#Shani
class TestRotateMatrix(unittest.TestCase):
    """
    2 Katas
    """
    pass

#Dani
class TestIsValidEmail(unittest.TestCase):
    """
    3 Katas
    """
    pass
class TestPascalTriangle(unittest.TestCase):
    """
     3 Katas
     """
    pass

#Arthur
class TestListFlatten(unittest.TestCase):
    """
    2 Katas
    """
    pass


#Arthur
class TestStrCompression(unittest.TestCase):
    """
    2 Katas
    """
    pass

#Arthur
class TestStrongPass(unittest.TestCase):
    """
    1 Katas
    """
    pass




if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
