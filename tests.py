import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testMinimum(self):
        response = self.app.get("/min?X=1,2,5,0,100")
        self.assertEqual(b'0 \n', response.data)
