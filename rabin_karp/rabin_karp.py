
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
        self.hash_value = (self.hash_value - old * self.base_to_size + self.p * self.base ) % self.p
        self.base_to_size = (self.base_to_size * self.inverse_base) % self.p

    def hash_value(self):
        return self.hash_value


def test():
    doc = 'abcdefgh'
    to_find = 'bc'
    h_find = RabinKarp(256, 23)
    h_doc = RabinKarp(256, 23) 
    for letter in to_find:
        print('appending: ', letter)
        h_find.append(ord(letter))
    print('bulding h_doct')
    for letter in doc[:len(to_find)]:
        print('appending : ', letter)
        h_doc.append(ord(letter))
    
    old = 0
    for i in range(len(to_find), len(doc)):
        print('hf: ', h_find.hash_value, 'hdoc: ', h_doc.hash_value)
        if h_find.hash_value == h_doc.hash_value:
            print('found match')
        h_doc.append(ord(doc[i]))
        h_doc.skip(ord(doc[old]))
        print('appending: ', doc[i])
        print('skipping: ', doc[old], old)
        print('hf: ', h_find.hash_value, 'hdoc: ', h_doc.hash_value)
        old += 1
    else:
        print("no match")

if __name__ == '__main__':
    test()
    
