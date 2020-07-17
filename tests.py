import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self) -> None:
        main.app.testing = True
        self.app = main.app.test_client()

    def testAverage(self):
        response = self.app.get("/mean?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/avg?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/average?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)
