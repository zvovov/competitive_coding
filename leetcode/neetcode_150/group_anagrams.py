# https://leetcode.com/problems/group-anagrams/

# Intuition:
# Sort the characters of the word and store as key in the hashmap, value is the list of original strings that form the same sorted characters ~ are anagrams

# Approach:
# Iterate through the list to see if any other word has the same sorted key. Final answer is the values of this hashmap

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in range(len(strs)):
            # sort the string before storing as key
            curr_key = ''.join(sorted(strs[i]))
            if hm.get(curr_key):
                hm[curr_key].append(strs[i])
            else:
                hm[curr_key] = [strs[i]]
        anagram_groups = []
        for v in hm.values():
            anagram_groups.append(v)
        return anagram_groups