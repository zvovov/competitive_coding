# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution_brute_force:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)-1, -1, -1):
            for j in range(0, i):
                print(prices[i], prices[j])
                curr_profit = prices[i] - prices[j]
                maximum = curr_profit if curr_profit > maximum else maximum
        return maximum

class Solution_so_far:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_so_far = 1e5
        for i in prices:
            lowest_so_far = i if i < lowest_so_far else lowest_so_far
            curr_profit = i - lowest_so_far
            max_profit = curr_profit if curr_profit > max_profit else max_profit

        return max_profit


class Solution_kadane:
    def maxProfit(self, prices: List[int]) -> int:
        curr_sum = 0
        max_profit = 0
        for i in range(len(prices)-1):
            curr_sum += prices[i+1] - prices[i]
            if curr_sum < 0:
                curr_sum = 0
            max_profit = max(curr_sum, max_profit)
        return max_profit


solve = Solution_kadane()
print(solve.maxProfit(prices=[1,2,3,4,5]))
print(solve.maxProfit(prices=[7,1,5,3,6,4]))
print(solve.maxProfit(prices=[7,6,4,3,1]))


