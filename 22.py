import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = dict(zip(string.ascii_lowercase, morse_code))
        d = 'a'.maketrans(d)

        s = set()
        for word in words:
            s.add(word.translate(d))

        return len(s)
