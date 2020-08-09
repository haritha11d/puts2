import unittest
import main


class TestCalculatorWebApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def testAverage(self):
        response = self.app.get("/max?X=1,2,3")
        self.assertEqual(b'3 \n', response.data)

        response = self.app.get("/max?X=1000,2.5,100")
        self.assertEqual(b'1000 \n', response.data)

        response = self.app.get("/max?X=-1.2,-2.5,-100,-9292,-0303,0293/92929")
        self.assertEqual(b'0.003 \n', response.data)


if __name__ == '__main__':
    unittest.main()
