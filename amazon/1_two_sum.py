"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


    def twoSum1(self, nums, target):
        r={}
        for i in range(len(nums)):
            r[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in r and i!=r[diff]:
                return [i, r[diff]]


    def twoSum1(self, nums, target):
        r={}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in r:
                return [r[diff], i]

            r[nums[i]] = i


