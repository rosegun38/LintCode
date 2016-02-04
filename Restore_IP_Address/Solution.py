class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        # Use recursive to solve this.
        Solution.res = []
        self.get_ip('', s, 0)
        return Solution.res

    def get_ip(self, curr_ip, s, curr_index):
        if curr_index == 3:
            if len(s) > 0:
                if str(int(s)) == s and int(s) <= 255:
                    Solution.res.append(curr_ip + s)
            return

        length = len(s)
        for i in range(1, 4):
            if len(s) > i and str(int(s[:i])) == s[:i] and int(s[:i]) <= 255:
                self.get_ip(curr_ip + s[:i] + '.', s[i:], curr_index + 1)
        return
