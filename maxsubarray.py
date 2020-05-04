# Given an integer array nums, find the continuous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# Solution by Molly Yu


class Solution(object):
    # First Solution
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1): # Kadane's Algorithm: if sum of subarray is positive, add. 
            if nums[i] > 0:
                nums[i+1] += nums[i]
        return max(nums)

    maxSubArray(1, [-2,1,-3,4,-1,2,1,-5,4])

    #Alternative approach (very similar)
    def maxSubArray2(self, nums):
        currentSum = nums[0] # set current sum, max sum to first element
        maxSum = nums[0]
        for i in nums[1:]:
            currentSum = max(i, currentSum+i) # to add or not to add current element to sum?
            maxSum = max(currentSum, maxSum) # is current sum larger than max sum?
        return maxSum

    maxSubArray2(1,  [-2,1,-3,4,-1,2,1,-5,4])
            