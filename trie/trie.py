
class TrieNode(object):
    def __init__(self, key=None):
        self.key = key
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = None

    def add_word(self, word):
        '''Insert a new word into the trie'''
        if self.root is None:
            self.root = TrieNode('')
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]

    def count_prefix(self, prefix):
        '''Count number of words that have prefix'''
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                break
            node = node.children[letter]
        if node.key != prefix[-1]:
            return 0
        return len(node.children)

    def delete_word(self, word):
        '''Delete word from trie'''
        node = self.root
        bp = node
        bp_letter = word[0]
        f = None
        for letter in word:
            if letter not in node.children:
                return
            if f is not None and len(node.children) > 1:
                f = None
            if f is None and len(node.children) == 1:
                f = bp
                f_letter = bp_letter
            bp = node
            bp_letter = letter
            node = node.children[letter]
        if len(node.children) > 1:
            return
        del(f.children[f_letter])

