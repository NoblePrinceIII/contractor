from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from unittest import TestCase, main as unittest_main
from app import app

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

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the Hoodie homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoodie', result.data)

    def test_new(self):
        """Test the new Hoodie creation page."""
        result = self.client.get('/red')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoodie', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_hoodie(self, mock_find):
        """Test showing a single Hoodie."""
        mock_find.return_value = sample_listing
        result = self.client.get(f'/hoodie/{sample_listing_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Hoodie', result.data)

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_hoodie(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/delete/{sample_listing_id}', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_listing_id})




    # @mock.patch('pymongo.collection.Collection.find_one')
    # def test_edit_hoodie(self, mock_find):
    #     """Test editing a single Hoodie."""
    #     mock_find.return_value = sample_listing
    #     result = self.client.get(f'{sample_listing_id}')
    #     self.assertEqual(result.status, '200 OK')
    #     self.assertIn(b'Hoodie', result.data)



    #     # After submitting, should redirect to that hoodie's page
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_insert.assert_called_with(sample_listing)
    #
    # @mock.patch('pymongo.collection.Collection.update_one')
    # def test_update_hoodie(self, mock_update):
    #     result = self.client.post(f'/{sample_listing_id}', data=sample_form_data)
    #
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_update.assert_called_with({'_id': sample_listing_id}, {'$set': sample_listing})
    #


if __name__ == '__main__':
    unittest_main()
