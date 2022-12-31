class Solution(object):
    def maximumValue(self, strs):
        max_ = 0
        for ch in strs:
            if ch.isdigit(): max_ = max(max_, int(ch))
            else: max_ = max(max_, len(ch))
        return max_
