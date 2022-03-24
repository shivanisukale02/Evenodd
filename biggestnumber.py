import unittest

def biggest(x,y):
    if x>y:
        return "first"
    else:
        return "second"

class Biggestone(unittest.TestCase):
    def test_bigge(self):
        x=6
        y=5
        result=biggest(x,y)
        self.assertEqual("first",result)
    def test_bigger1(self):
        x=2
        y=3
        result=biggest(x,y)
        self.assertEqual("second",result)

if __name__=="__main__":
    unittest.main()

