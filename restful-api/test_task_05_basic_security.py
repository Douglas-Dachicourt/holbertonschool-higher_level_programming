import unittest
import json
from task_05_basic_security import app


class BasicSecurityTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_basic_protected_route(self):
        response = self.app.get('/basic-protected')
        self.assertEqual(response.status_code, 401)

        headers = {'Authorization': 'Basic dXNlcjE6cGFzc3dvcmQ='}
        response = self.app.get('/basic-protected', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Basic Auth: Access Granted')

    def test_login_route(self):
        response = self.app.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {
                         "error": "Username and password are required"})

        data = {'username': 'user1', 'password': 'password'}
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

        data = {'username': 'user1', 'password': 'wrong_password'}
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {
                         "error": "Unauthorized response"})

    def test_jwt_protected_route(self):
        response = self.app.get('/jwt-protected')
        self.assertEqual(response.status_code, 401)

        headers = {'Authorization': 'Bearer invalid_token'}
        response = self.app.get('/jwt-protected', headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"error": "Invalid token"})

        headers = {'Authorization': 'Bearer valid_token'}
        response = self.app.get('/jwt-protected', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'JWT Auth: Access Granted')

    def test_admin_only_route(self):
        response = self.app.get('/admin-only')
        self.assertEqual(response.status_code, 401)

        headers = {'Authorization': 'Bearer valid_token'}
        response = self.app.get('/admin-only', headers=headers)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data), {"error": "Access denied"})

        headers = {'Authorization': 'Bearer admin_token'}
        response = self.app.get('/admin-only', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Admin Access: Granted')


if __name__ == '__main__':
    unittest.main()
