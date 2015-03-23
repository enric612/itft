import unittest
from app import create_app, db
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.client = self.app.test_client(use_coockies=True)
        db.create_all()
        User.register('john', 'cat')

    def tearDown(self):
        db.drop_All()
        self.app_ctx.pop()

    def test_login(self):
        r = self.client.get('/login')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('<h1>Login</h1>' in r.get_data(as_text=True))
        r = self.client.post('/login',
                             data={'username': 'john', 'password': 'cat'},
                             follow_redirects=True)
        self.assertEqual(r.status_code, 200)
        self.assertTrue('<h1>Home page</h1>' in r.get_data(as_text=True))
        r = self.client.get('/protected')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('<h1>Protected page</h1>' in r.get_data(as_text=True))
