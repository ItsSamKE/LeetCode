# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        if target in nums:
            for i, val in enumerate(nums):
                if (val == target):
                    return i
                elif (val > target):
                    return i
        else:
            return len(nums)


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 7))
