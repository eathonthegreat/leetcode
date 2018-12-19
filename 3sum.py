class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        no = len(nums)
        solution = []
        for i in range(len(nums)):
            left = i
            middle = i + 1
            right = no - 1
            while left < middle and middle < right:
                if nums[left] + nums[middle] + nums[right] > 0:
                    right = right - 1
                elif nums[left] + nums[middle] + nums[right] < 0:
                    middle = middle + 1
                else:
                    a = [nums[left],nums[middle],nums[right]]
                    if middle < right:
                        middle = middle + 1
                    if a in solution:
                        None
                    else:
                        solution.append(a)
                        print a