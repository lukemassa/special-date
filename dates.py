#!/usr/bin/env python3

import unittest
from datetime import datetime, timedelta

def is_date_special(date):
    return date.day * date.month == date.year % 100


def run_tests():

    class Tester(unittest.TestCase):

        def one_test(self, date, expected_special):
            """
            Runs a single test with input and asserts expected output
            """
            self.assertEqual(is_date_special(date), expected_special)

        def test_base(self):
            self.one_test(datetime(year=2010, month=2, day=5), True)
            self.one_test(datetime(year=2010, month=5, day=2), True)
            self.one_test(datetime(year=2010, month=3, day=5), False)
            self.one_test(datetime(year=2050, month=3, day=5), False)

    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(Tester))

def get_percentage():
    total_days = 0
    special_days = 0
    date = datetime(year=2000, month=1, day=1)
    enddate = datetime(year=2100, month=1, day=1)
    while date < enddate:
        date = date + timedelta(days=1)
        if is_date_special(date):
            special_days+=1
        total_days+=1
    return (float(special_days) / float(total_days)) * 100

#run_tests()
print("Percentage special days: %.2f%%" % (get_percentage()))
