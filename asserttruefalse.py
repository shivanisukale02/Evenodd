import unittest

def divisibleby7(x):
    if x%7==0:
        return True
    else:
        return False

class divisible7(unittest.TestCase):
    def test_divisib7(self):
        x=14
        result=divisibleby7(x)
        self.assertTrue(result)

    def test_notdivisib7(self):
        x=20
        result=divisibleby7(x)
        self.assertFalse(result)

if __name__=="__main__":
    unittest.main