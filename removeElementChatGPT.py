class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))
