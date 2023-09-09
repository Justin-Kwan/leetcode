class Solution:
#     # top down with memoization
#     def climbStairs(self, n: int) -> int:
#         # for starting n, how many total ways to get to 0?
#         return self.helper(n, {})

#     def helper(self, n: int, cache: map) -> int:
#         if n < 0:         # not end of valid path
#             return 0
#         if n is 0:        # end of path found
#             return 1
        
#         # check if current n in cache
#         if n in cache:
#             return cache[n]
        
#         # otherwise recurse, then update cache for n
#         cache[n] = self.helper(n - 1, cache) + self.helper(n - 2, cache)
        
#         return cache[n]

    # bottom up dp
    def climbStairs(self, n: int) -> int:
        uniquePathsAtN = [1]    # consider 1 path to get to step 0
        
        # setup list of unique paths up to each step, starting at step 1
        for i in range(1, n + 1):
            
            # unique paths if taking one step down
            paths1StepDown = uniquePathsAtN[i - 1]
            
            paths2StepsDown = 0
            
            # unique paths if taking two steps down
            # if going 2 steps down lands at a valid step
            if i - 2 >= 0:
                paths2StepsDown = uniquePathsAtN[i - 2]
            
            uniquePathsAtN.append(paths1StepDown + paths2StepsDown)
            
        return uniquePathsAtN[n]
