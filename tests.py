import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()





