
import random
from .utils import mod_exp

class Prover:
    def __init__(self, p, g, secret):
        self.p = p
        self.g = g
        self.secret = secret

    def generate_commitment(self):
        self.r = random.randint(1, self.p - 1)
        return mod_exp(self.g, self.r, self.p)

    def compute_response(self, challenge):
        return (self.r + challenge * self.secret) % (self.p - 1)
