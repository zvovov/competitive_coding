# https://leetcode.com/problems/top-k-frequent-elements/

# Intuition:
# Hashmap and sorting. Reverse-sort the frequency hashmap on values(frequencies) and slice top K

# Approach:
# Use ordered dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = OrderedDict()
        for i in nums:
            freq[i] = freq.get(i) + 1 if freq.get(i) else 1
        return (list(OrderedDict(sorted(freq.items(), key=lambda x: x[1], reverse=True)).keys())[:k])