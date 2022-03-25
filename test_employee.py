import unittest
import sqlite3 as sql

class employee_details(unittest.TestCase):
    def setUp(self):
        self.name = "Leela"
        self.empcode = "01"
        self.connection = sql.connect("employee.db")

    def tearDown(self):
        self.name = ""
        self.empcode = ""
        self.connection.close()

    def test_case1(self):
        result = self.connection.execute("select name from employee  where empcode="+self.empcode)

        for i in result:
            fetchedemployeename=i[0]

        self.assertEqual(self.name, fetchedemployeename)

if __name__ == "__main__":
    unittest.main()