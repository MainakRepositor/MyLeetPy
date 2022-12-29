class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words: # Go through all the words
            if i == i[::-1]: #Check if the word is equal to itself reversed (a palindrome)
                return i #If it is, return that word
        return "" #Otherwise return an empty string
