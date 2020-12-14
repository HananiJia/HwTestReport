#!/usr/bin/env python3
# coding=utf-8
import os
import sys
import glob
import json
import unittest
import time
from TestReport import HTMLTestReport


class TestTopbind(unittest.TestCase):
    def testSuccess(self):
        print('success!')
        self.assertFalse(False)

    def testFailed(self):
        print('failed!')
        self.assertFalse(True)

    def testEmpty(self):
        self.assertFalse(False)


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestTopbind)
    suites = unittest.TestSuite()
    suites.addTests(suite1)
    with open('./TestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report, title='topbind test_bindings')
        runner.run(suites)
