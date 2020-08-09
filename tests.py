import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testEmptyPage(self):
        """Test the page with an empty route"""

        response = self.app.get("/")
        self.assertEqual(b'Usage: \n<Operation>?A=<Value1, Value2, ..., ValueN>', response.data)

    def testMinimum(self):
        response = self.app.get("/min?X=1,2,3")
        self.assertEqual(b'1 \n', response.data)

        response = self.app.get("/min?X=-1.2,-2.5,-100,-9292,-0303,0293/92929")
        self.assertEqual(b'-9292 \n', response.data)

        response = self.app.get("/min?X=1000,2.5,100")
        self.assertEqual(b'2.5 \n', response.data)

    def testAverage(self):
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

    def testMaximum(self):
        response = self.app.get("/max?X=1,2,3")
        self.assertEqual(b'3 \n', response.data)

        response = self.app.get("/max?X=1000,2.5,100")
        self.assertEqual(b'1000 \n', response.data)

        response = self.app.get("/max?X=-1.2,-2.5,-100,-9292,-0303,0293/92929")
        self.assertEqual(b'0.003 \n', response.data)


if __name__ == '__main__':
    unittest.main()
