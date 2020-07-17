import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testEmptyPage(self):
        """Test the page with an empty route"""

        response = self.app.get("/")
        self.assertEqual(b'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n', response.data)




