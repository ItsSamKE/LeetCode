class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in range(len(s)):
            # If length is odd then it means there is a parenthesis that wont pair
            if (len(s) % 2 == 0):
                # I only want to evaluate at the even index
                if (i % 2 == 0):
                    # print(i)
                    RequiredString = parenthesis.get(s[i], 0)
                    # print(str(i)+' Current ' +
                    #       str(s[i])+' coming '+str(s[i+1])+' Requires '+RequiredString)
                    if (s[i+1] != RequiredString):
                        return False
            else:
                return False
        return True


paran = Solution()
print(paran.isValid('())}[]'))
