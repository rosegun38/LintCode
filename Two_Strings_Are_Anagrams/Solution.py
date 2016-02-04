class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    # Time: is equal to sorted O(nlogn)
    # Space: O(1)

    def anagram(self, s, t):
        # write your code here
        s = sorted(s)
        t = sorted(t)

        return s == t
