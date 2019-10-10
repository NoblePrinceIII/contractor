# tests.py

from unittest import TestCase, main as unittest_main
from app import app
from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId


sample_listing_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_listing = {
    'title': 'Red Hoodie',
    'price': '100',
    'image': 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQnpUskOPTmPAPOXNYDaBpZsgdogqXKqCtiqq_V5Hqxq6WBFcBY62z6aOKPHP4crqEJz8nX9a3IIMgj3789RNhVPRtSwxqeNSz6PG4U7HRNSgViqzd_DwkTMg&usqp=CAY'
}
sample_form_data = {
    'title': sample_listing['title'],
    'price': sample_listing['price'],
    'image': sample_listing['image']
}


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
