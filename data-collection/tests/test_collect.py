import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from src.collect_data import fetch_news_data

class TestDataCollection(unittest.TestCase):

    def test_fetch_news_data(self):
        news = fetch_news_data()
        self.assertTrue(len(news) > 0)
        self.assertIn("title", news[0])
        self.assertIn("source", news[0])

if __name__ == "__main__":
    unittest.main()
