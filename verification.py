import sys
import unittest

def login_verification(username,password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False

class Verification(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith("win"),"require windows os")

    def test_verfication1(self):
        username = "admin"
        password = "12345"
        result=login_verification(username, password)
        self.assertTrue(result)

    @unittest.skip("skipped")
    def test_notverfication1(self):
        username = "admin"
        password = "12453"
        result=login_verification(username, password)
        self.assertFalse(result)

if __name__=="__main__":
    unittest.main()