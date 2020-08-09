import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testAverage(self):
        response = self.app.get("/median?X=1,2,3")
        self.assertEqual(b'2 \n', response.data)

        response = self.app.get("/median?X=1000,2.5,100")
        self.assertEqual(b'100 \n', response.data)

        response = self.app.get("/median?X=-1.2,-2.5,-100,-9292,-0303,0293/92929")
        self.assertEqual(b'-51.25 \n', response.data)

        response = self.app.get("/median?X=1,2,5,0,100,-100,-5,-2")
        self.assertEqual(b'0.5 \n', response.data)


if __name__ == '__main__':
    unittest.main()
