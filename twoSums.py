class Solution:
    def twoSum(self, nums, target):

        # theIndex = 0
        # theOtherNumber = 0
        for i in range(len(nums)):

            # theIndex = i
            theOtherNumber = target - nums[i]  # Gives the number

            # del nums[i]
            # return nums
            if theOtherNumber > 0 and theOtherNumber in nums:
                indexOfTheNumber = nums.index(theOtherNumber)
                print(i, indexOfTheNumber)
                # return

    def twoSumChat(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


theList = [3, 2, 4]
d = Solution()
print(d.twoSumChat(theList, 6))
