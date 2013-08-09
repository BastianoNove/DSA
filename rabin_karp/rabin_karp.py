
class RabinKarp(object):
    def __init__(self, base, p):
        self.base = base
        self.p = p
        self.hash_value = 0
        self.base_to_size = 1
        self.inverse_base = pow(self.base, self.p-2, self.p) % self.p

    def append(self, x):
        self.hash_value= (self.hash_value * self.base + x) % self.p
        self.base_to_size = (self.base_to_size * self.base) % self.p

    def skip(self, old):
        self.base_to_size = (self.base_to_size * self.inverse_base) % self.p
        self.hash_value = (self.hash_value - old * self.base_to_size + self.p * self.base ) % self.p

def test():
    doc = 'abcdefgh'
    to_find = 'ydef'
    h_find = RabinKarp(256, 23)
    h_doc = RabinKarp(256, 23)
    for letter in to_find:
        h_find.append(ord(letter))
    for letter in doc[:len(to_find)]:
        h_doc.append(ord(letter))
    if h_find.hash_value == h_doc.hash_value:
        print('match found')
    for i in range(len(to_find), len(doc)):
        old = doc[i-len(to_find)]
        h_doc.skip(ord(old))
        h_doc.append(ord(doc[i]))
        if h_find.hash_value == h_doc.hash_value:
            print('found match')
            break
    else:
        print("no match")

if __name__ == '__main__':
    test()

