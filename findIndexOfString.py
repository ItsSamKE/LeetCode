class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Method 1
        # index = haystack.find(needle)
        # return index

        # Method 2
        haystackArray = list(haystack)
        fast = 0
        needleLen = len(needle)
        while fast < len(haystackArray):
            if (haystack[fast:needleLen] == needle):
                return fast
            fast += 1
            needleLen += 1
        return -1


sol = Solution()
print(sol.strStr('dasbutdasad', 'sad'))
