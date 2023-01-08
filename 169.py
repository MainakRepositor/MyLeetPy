class Solution:
  def removeAnagrams(self, words: List[str]) -> List[str]:
    res = []
    anagrams = {}

    for i in range(len(words)):
      word = words[i]
      counter = [0]*26
      for c in word:
        counter[ord(c)-ord('a')] += 1

      if tuple(counter) not in anagrams:
        res.append(word)
      else:
        if anagrams[tuple(counter)] != words[i-1]:
          res.append(word)
      anagrams[tuple(counter)] = word
    return res
