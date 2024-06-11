import hashlib

def sha256_hash(data):
    """
    Retourne le hash SHA-256 de la chaîne de caractères donnée.
    :param data: Chaîne de caractères à hasher.
    :return: Hash SHA-256 en hexadécimal.
    """
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()
