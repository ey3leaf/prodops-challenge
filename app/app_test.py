import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def testRoot(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def testHealth(self):
        result = self.app.get('/health')
        self.assertEqual(result.status_code, 200)
