# Two sum problem: Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# Solutions by Molly Yu

class Solution(object):

    # Brute Force Attempt
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        length = len(nums)
        for x in range(0,length-1):
            for y in range(x+1,length):
                sum = nums[x] + nums[y]
                if sum == target and (x!=y):
                    return [x,y]

    twoSum(1,[2,5,5,11],10)

    # Attempt using map (learning how Python dict works)
    def twoSumImproved(self, nums, target):
        map = {x: nums[x] for x in range(len(nums))} # key = x, value =nums[x] (map.keys(), map.values())
        map = {value:key for key, value in map.items()} # swap key and value
        for i in range(len(nums)):
            cmp = target - nums[i]
            if (cmp in map.keys()) and (map.get(cmp)!=i):
                # print(i,map.get(cmp))
                return [i,map.get(cmp)]

    twoSumImproved(1,[2,5,5,11],10)

    # Revised Map
    def twoSumFinal(self, nums, target):
        passed = {}
        for c, v in enumerate(nums): # enumerate: counter, value
            cmp = target - v
            if cmp in passed:
                return [passed[cmp], c] # get value(index) of key(cmp)
            passed[v] = c # key = numerical values, value = index
        return []

    twoSumFinal(1,[2,5,5,11],10)



        
