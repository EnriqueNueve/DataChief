"""
Test script for Augment/Linear.py

Made by Enrique Nueve
Date: 08/12/2020
Email: enriquenueve9@gmail.com

TO-DO
* None

Python Assert Methods: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

To Run:  python3 -m unittest test_Linear.py or python3 test_Linear.py
"""

##############################################

import unittest
import Linear

import pandas as pd


##############################################

class TestAugmentLinear(unittest.TestCase):
    # @classmethod will affect all objects of class, modify one object, it modifies all
    # cls. field can be called as self. from any method
    @classmethod
    def setUp(cls) -> None:
        try:
            cls.test_df = pd.read_csv("../TestData/so2_chicago_data.txt")
        except:
            print("Failed to open TestData/so2_chicago_data.txt")

    @classmethod
    def tearDown(cls) -> None:
        pass

    def test_testLinear(self):
        """ Check if Augment/Linear.py is being imported."""
        Linear.testLinear()

    def test_circularEncode(self):
        """Check if ValueError is raised if non-numeric col is passed."""
        self.test_df["dummy_str"] = ["hi" for i in range(self.test_df.shape[0])]
        self.assertRaises(ValueError, Linear.circularEncode, "dummy_str", self.test_df, 12, 12)

    def test_turkeyLadder(self):
        """Check if ValueError is raised if non-numeric col is passed."""
        self.test_df["dummy_str"] = ["hi" for i in range(self.test_df.shape[0])]
        self.assertRaises(ValueError, Linear.turkeyLadder, "dummy_str", self.test_df, 12, 12)


##############################################

if __name__ == "__main__":
    unittest.main()
