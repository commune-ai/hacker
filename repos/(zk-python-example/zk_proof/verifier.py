
from .utils import mod_exp

class Verifier:
    def __init__(self, p, g, public_key):
        self.p = p
        self.g = g
        self.public_key = public_key

    def generate_challenge(self):
        return random.randint(1, self.p - 1)

    def verify(self, commitment, challenge, response):
        left = mod_exp(self.g, response, self.p)
        right = (commitment * mod_exp(self.public_key, challenge, self.p)) % self.p
        return left == right
