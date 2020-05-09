# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Solution by Molly Yu

class Solution(object):
    # Solution using hashmap, works even if numbers come up >2 times
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for num in nums:
            map[num] = map.get(num, 0)+1 # or max(0, map.get)+1
        for key, val in map.items():
            if val == 1:
                return key

    # Solution using XOR, without extra memory
    def singleNumber2(self, nums):
        for i in range(1,len(nums)):
            nums[0] ^= nums[i] # anything XOR itself will be 0, so we end up with the non-duplicate number
        return nums[0]


    # Solution using List (append if not already in array, remove if already in array), pretty bad time complexity
    def singleNumber3(self, nums):
        newlist = []
        for i in nums:
            if i not in newlist:
                newlist.append(i)
            else:
                newlist.remove(i)
        return newlist.pop() # remove the last element and return it (non-duplicate value)


    # Mathematical Solution : 2 * (a + b + c) - (a + a + b + b + c) = c
     def singleNumber4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums) # set is all unique elements
