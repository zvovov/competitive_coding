# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            max_profit = max(currentProfit, max_profit)
            if prices[left] > prices[right]:
                left = right
            right += 1
        
        return max_profit


    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            curr_profit += prices[i] - prices[i-1]
            curr_profit = max(0, curr_profit)
            max_profit = max(max_profit, curr_profit)

        return max_profit

solved = Solution()
 
print(solved.maxProfitBruteForce(prices = [7,1,5,3,6,4])) 
print(solved.maxProfitBruteForce(prices = [7,6,4,3,5,1]))
print(solved.maxProfitBruteForce(prices = [17,35,51,30,61,84]))

print(solved.maxProfit(prices = [7,1,5,3,6,4])) 
print(solved.maxProfit(prices = [7,6,4,3,5,1]))
print(solved.maxProfit(prices = [17,35,51,30,61,84]))