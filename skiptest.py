import unittest
import sys

import unittest

def login(usernmae, password):
    if usernmae == "admin" and password == "12345":
        return True
    else:
        return False
class checkLogin(unittest.TestCase):
        @unittest.skipUnless(sys.platform.startswith("win"), "requires NOT windows os")
        def test_case1(self):
            username = "admin"
            password = "12345"
            result = login(username, password)
            self.assertTrue(result)

        @unittest.skipIf(sys.platform.startswith("win"), "requires NOT windows os")
        def test_case2(self):
            username = "admin"
            password = "12345"
            result = login(username, password)
            self.assertTrue(result)

        @unittest.skipIf(sys.platform.startswith("win"), "requires NOT windows os")
        def test_case2(self):
            username = "admin"
            password = "12345"
            result = login(username, password)
            self.assertTrue(result)

        @unittest.skip("code is skipped")
        def test_case3(self):
            username = "admin"
            password = "12345"
            result = login(username, password)
            self.assertTrue(result)

if __name__=="__main__":
    unittest.main()