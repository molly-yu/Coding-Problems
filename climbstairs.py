# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Solution by Molly Yu


class Solution(object):
    # First recursive solution, slow
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(0,n)
    
    def helper(self, i, n): # i = steps taken, n = total steps
        if i > n:
            return 0
        if i == n:
            return 1 # everytime we find a combination, add 1 to count
        return (self.helper(i+1, n) + self.helper(i+2, n)) # try taking 1 or 2 steps every time



    # Similar approach, but with memoization
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = []
        return self.helper2(0,n, memo)
    
    def helper2(self, i, n, memo): # i = steps taken, n = total steps
        if i > n:
            return 0
        if i == n:
            return 1 # everytime we find a combination, add 1 to count
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.helper2(i+1, n, memo) + self.helper2(i+2, n, memo)
        print(memo[i])
        return memo[i] # try taking 1 or 2 steps every time



    # Alternative Solution
    def climbStairs3(self, n):
        
        a, b = 1, 1
        for i in range(n):
            tmp = b
            b = a + b
            a = tmp
            
        return a

# climbstairs2 = Solution()
# climbstairs2.climbStairs2(3)
        