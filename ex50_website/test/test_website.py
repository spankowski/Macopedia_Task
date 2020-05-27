import unittest
from app import app

class TestStringMethods(unittest.TestCase):

    def test_index(self):
        # example test
        app.config['TESTING'] = True
        web = app.test_client()
        rv = web.get('/hell', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)
        self.assertIn(b"The requested URL was not found on the server",rv.data)
        
    def test_hello(self):
        # flask API for processing requests:
        app.config['TESTING'] = True
        web = app.test_client()
        data = {'name': 'Zed', 'greet': 'Hola'}
        rv = web.post('/hello', follow_redirects=True, data=data)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"Zed", rv.data)
        self.assertIn(b"Hola", rv.data)

if __name__ == '__main__':
    unittest.main()
