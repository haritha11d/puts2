import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testMaximum(self):
        response = self.app.get("/max?X=1,2,5,0,100")
        self.assertEqual(b'100 \n', response.data)
