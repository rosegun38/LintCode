class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s)):
            pos = ord(s[i]) - ord('a')
            c1[pos] += 1

        for i in range(len(t)):
            pos = ord(t[i]) - ord('a')
            c2[pos] += 1

        j = 0
        stillOK = True
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j += 1
            else:
                stillOK = False

        return stillOK
