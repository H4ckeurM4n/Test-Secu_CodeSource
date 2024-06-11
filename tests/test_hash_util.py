import unittest
from src.hash_util import sha256_hash

class TestHashUtil(unittest.TestCase):

    def test_sha256_hash(self):
        # Test de hash pour une chaîne vide
        self.assertEqual(sha256_hash(''), 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')
        # Test de hash pour une chaîne de caractères spécifique
        self.assertEqual(sha256_hash('test'), '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08')
        # Test de hash pour une autre chaîne de caractères
        self.assertEqual(sha256_hash('hello'), '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')

if __name__ == '__main__':
    unittest.main()
