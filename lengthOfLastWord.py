# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        MyListString = s.split()

        return len(MyListString[-1])  # MyListString


Sol = Solution()
print(Sol.lengthOfLastWord("   fly me   to   the moon  "))
