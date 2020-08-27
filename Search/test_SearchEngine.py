import unittest
import SearchEngine

import pandas as pd


##############################################

##############################################

class TestSearchEngine(unittest.TestCase):
    # @classmethod will affect all objects of class, modify one object, it modifies all
    # cls. field can be called as self. from any method
    @classmethod
    def setUp(cls) -> None:
        try:
            cls.test_df = pd.read_csv("../TestData/so2_chicago_data.txt")
        except:
            print("Failed to open TestData/so2_chicago_data.txt")

        cls.engine = SearchEngine.searchEngine()

    @classmethod
    def tearDown(cls) -> None:
        pass

    def test_fitData(self):
        """Check if ValueError is raised if non-numeric col is passed."""
        self.test_df["dummy_str"] = ["hi" for i in range(self.test_df.shape[0])]
        self.assertRaises(ValueError, self.engine.fitData, self.test_df)

    def test_makeEngine(self):
        made_engine = SearchEngine.searchEngine.makeEngine(self.test_df)
        self.assertIsInstance(made_engine,SearchEngine.searchEngine)


##############################################

if __name__ == "__main__":
    unittest.main()
