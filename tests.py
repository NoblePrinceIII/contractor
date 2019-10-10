# tests.py

from unittest import TestCase, main as unittest_main
from app import app

class HoodieTest(TestCase):
    """Flask tests."""

    def test_index(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoodie', result.data)

        def test_new(self):
            """Test the new playlist creation page."""
            result = self.client.get('/red')
            self.assertEqual(result.status, '200 OK')
            self.assertIn(b'New Hoodie', result.data)


    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

if __name__ == '__main__':
    unittest_main()
