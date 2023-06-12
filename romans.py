class Solution:
    def romanToInt(self, s: str) -> int:
        theNumber = 0
        RomanList = list(s)
        lasVal = ''
        for i, val in enumerate(RomanList):
            if lasVal == val:
                theNumber += theNumber
            else:
                lasVal = ''
                theNumber = self.getNumber(val)
            lasVal = val
        return theNumber

    def getNumber(self, roman):
        if roman == 'I':
            return 1
        elif roman == 'V':
            return 5
        elif roman == 'X':
            return 10
        elif roman == 'L':
            return 50
        elif roman == 'C':
            return 100
        elif roman == 'D':
            return 500
        elif roman == 'M':
            return 1000
