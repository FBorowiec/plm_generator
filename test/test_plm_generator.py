import unittest
from unittest.mock import patch
from plm_generator import PLMGenerator


class Test(unittest.TestCase):
    @patch("logger.logger.psycopg2.connect")
    def test_something(self, logger_mock):
        plm_generator = PLMGenerator()
