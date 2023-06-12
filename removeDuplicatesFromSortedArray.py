class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        checkNumber = None
        newNumList = []
        for num in nums:
            if (checkNumber != num):
                newNumList.append(num)
            checkNumber = num
        print(newNumList)


sol = Solution()
sol.removeDuplicates([1, 1, 3, 3, 5, 6, 7, 7])
