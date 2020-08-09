import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testAverage(self):
        response = self.app.get("/mean?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/avg?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/average?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/average?X=1000,2.5,100")
        self.assertEqual(b'367.5 \n', response.data)

        response = self.app.get("/avg?X=1000,2.5,100")
        self.assertEqual(b'367.5 \n', response.data)

        response = self.app.get("/mean?X=1000,2.5,100")
        self.assertEqual(b'367.5 \n', response.data)

        """ Edge Case Testing """

        response = self.app.get("/mean?X=x")
        self.assertEqual(b'Something wrong! --> input should consist of a vector of real numbers.\n',
                         response.data)


if __name__ == '__main__':
    unittest.main()
