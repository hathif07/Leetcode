class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}

        l = s.split()

        if len(pattern) != len(l):
            return False

        for i in range(len(pattern)):

            if pattern[i] in d1:
                if d1[pattern[i]] != l[i]:
                    return False

            if l[i] in d2:
                if d2[l[i]] != pattern[i]:
                    return False

            d1[pattern[i]] = l[i]
            d2[l[i]] = pattern[i]

        return True

