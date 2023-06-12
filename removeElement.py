class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        newList = []
        removed = []
        for num in nums:
            if (num != val):
                newList.append(num)
            else:
                removed.append('_')
        print(str(len(newList))+', nums = '+str(newList+removed))


sol = Solution()
sol.removeElement([3, 2, 2, 3], 3)
