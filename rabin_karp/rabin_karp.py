
class RabinKarp(object):
    def __init__(self, base, p):
        self.base = base
        self.p = p
        self.hash_value = 0
        self.base_to_size = 1
        self.inverse_base = pow(self.base, self.p-1, self.p) % self.p

    def append(self, x):
        self.hash_value= (self.hash_value * self.base + new) % p
        self.base_to_size = (self.base_to_size * base) % p

    def skip(self):
        self.hash_value = (self.hash_value - old * magic + p * base ) % p
        self.base_to_size = self.base_to_size * self.inverse_base % p

    def hash_value(self):
        return self.hash_value
