class Solution(object):
    def stringMatching(self, words):
        result = []
        index = 0
        while index < len(words):
            word = words[index]
            for i in range(len(words)):
                if i == index:
                    continue
                if word in words[i]:
                    if word not in result:
                        result.append(word)
            index += 1
        
        return result
