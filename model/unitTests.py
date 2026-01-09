# Implemented by Filipe
import unittest
import pandas as pd
from dataHandler import validateCSV
from datetime import datetime


class TestAdd(unittest.TestCase):

    def test_empty_csv(self):
        emptydf= pd.DataFrame()
        with self.assertRaises(Exception) as context:
            validateCSV(emptydf)
        self.assertIn("Invalid data", str(context.exception))

    def test_missing_column_csv(self):
        validDf = pd.read_csv("./test_movies.csv")
        noOverviewDf = validDf.drop(columns=['overview'])
        with self.assertRaises(Exception) as context:
            validateCSV(noOverviewDf)
        self.assertIn("Invalid data", str(context.exception))

    def test_valid_csv(self):
        validDf = pd.read_csv("./test_movies.csv")
        result = validateCSV(validDf)

        required_cols = set([
            "id", "title", "release_date", "score", "overview", 
            "crew", "original_language", "poster_url", "genres"
        ])

        self.assertTrue(required_cols.issubset(result.columns))


        self.assertFalse(result['id'].isnull().any())
        self.assertFalse(result['title'].isnull().any())

        self.assertFalse(result['release_date'].isnull().any())
        for date in result['release_date']:
            try:
                # Try parsing with the exact format
                datetime.strptime(date, '%m/%d/%Y')
            except ValueError:
                self.fail(f"Invalid date format: {date}")

        for score in result['score']:
            if pd.notna(score):
                self.assertTrue(0 <= float(score) <= 100)

        self.assertFalse(result['overview'].isnull().any())
        for ov in result['overview']:
            self.assertNotEqual(ov, "We don't have an overview translated in English.")

        self.assertFalse(result['genres'].isnull().any())

if __name__ == "__main__":
    unittest.main()
