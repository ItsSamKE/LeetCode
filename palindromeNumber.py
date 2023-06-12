# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # use list[<start>:<stop>:<step>]
        xString = str(x)
        NewString = xString[::-1]  # -1 goes to the far end
        if (x == int(NewString)):
            return True

        return False


sol = Solution()
print(sol.isPalindrome(622))
