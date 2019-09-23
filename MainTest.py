import unittest
import pytest
from Main import isValid, githubAccountWithName


class TestMain(unittest.TestCase):
    def testIsValidWithName(self):
        self.assertEqual(isValid("rpatel1291"), True, "rpatel1291 is a correct username")
    def testIsValidNoName(self):
        self.assertEqual(isValid(""), False, "No name was given")
    def testGithubAccountWithName(self):
        self.assertEqual(githubAccountWithName("rpatel1291"), "Assessments", "Assessments is a repo in rpatel1291 ")


if __name__ == '__main__':
    unittest.main()
