import unittest
from providers import Providers

class TestHere(unittest.TestCase):

    def test_google_get_not_found(self):
        p = Providers()
        resp = p.get('Here', 'The Wardrobe, Narnia')
        self.assertEqual(resp.status, 'No Results')
    
    def test_google_get_found(self):
        p = Providers()
        resp = p.get('Here', '301 Front Street West, Toronto')
        self.assertEqual(resp.status, 'OK')
        self.assertAlmostEqual(resp.data['lat'], 43.64, 2)
        self.assertAlmostEqual(resp.data['lng'], -79.39, 2)

if __name__ == '__main__':
    unittest.main()