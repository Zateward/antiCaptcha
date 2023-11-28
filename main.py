import unittest
from decoder import captchaDecoder


class TestStringMethods(unittest.TestCase):

    def test_images(self):
        self.assertEqual(captchaDecoder('test.jpg'), '1bda2')
        self.assertEqual(captchaDecoder('test2.jpg'), '7f4ca')

if __name__ == '__main__':
    unittest.main()