class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        n, lst = len(words), set()
        if n == 1:
            return 1
        d = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        for i in words:
            s = ''
            for j in i:
                s += d[j]
            lst.add(s)
        return len(lst)

        
        