import unittest

def add(x,y):
    return x+y;

class Myapp1(unittest.TestCase):
    def test_case1(self):
        a=10
        b=20
        result= a+b;
        self.assertEqual(a+b,result)

    def test_case2(self):
        a=1.5
        b=3.5
        result=a+b;
        self.assertEqual(a+b,result)

if __name__=="__main__":
    unittest.main()