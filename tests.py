import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testMedian(self):
        response = self.app.get("/median?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'0.5 \n', response.data)
