# https://neetcode.io/problems/last-stone-weight?list=neetcode150

from typing import List
import heapq

# # Intuition:
# Maintain a heap, get 2 largest elements in constant time

# Approach:
# repeat the iterations
#   do operations -> remove 2, add new element
# after every iteration
#   if 1 element remains, return the element or return 0 if no element remains
#   skip return and move to next iteration

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = list(map(lambda x: -1 * x, stones))
        heapq.heapify(stones_neg)

        while len(stones_neg):
            if len(stones_neg) == 1:
                return -1 * stones_neg[0]
            elif len(stones_neg) >= 2:
                # delete both
                first = heapq.heappop(stones_neg)
                second = heapq.heappop(stones_neg)
                after_smash = abs(first-second)
                if after_smash != 0: # add after_smash
                    heapq.heappush(stones_neg, -1 * after_smash)
        return 0 # if len == 0
    
solved = Solution()
print(solved.lastStoneWeight([2,7,4,1,8,1]))
