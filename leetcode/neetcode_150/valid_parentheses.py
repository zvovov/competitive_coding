# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid_(self, s: str) -> bool:
        # requirements
        # 1. Any type of open is allowed after any type of open
        # 2. The latest open must be closed, and in order for remaining currently open
        # 3. If some open is left open at the end of string, return error

        # open-close dict
        get_closed = {'(': ')',
                      '{': '}',
                      '[': ']'}
        
        get_open =  {')': '(',
                     '}': '{',
                     ']': '['}
        
        # maintain a stack
        stack_ = []

        for curr_br in s:
            closed_br = get_closed.get(curr_br)
            open_br = get_open.get(curr_br)
            if closed_br != None: # if any open br, add to stack
                stack_.append(curr_br)
                continue
            else: # if closed br, check rules
                if len(stack_) > 0:
                    latest_ = stack_[-1]
                    if latest_ == open_br:
                        stack_.pop()
                    else:
                        return False
                else: # s starting with close bracket
                    return False
        return len(stack_) == 0


# Intuition:
# Maintain a stack of incoming parenthesis in order

# Approach:
# Iterate string, if opening parenthesis is found, insert in stack and move to next element
# If closing parenthesis is found, pop the stack and match, proceed if match, return false otherwise
# At the end of the string, if stack is empty return true, false otherwise

# Complexity:
# Time: O(n) for one loop on input string
# Space: O(n) for stack

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parenth_stack = deque()
        parenth_pair = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                parenth_stack.append(s[i])
            else:
                if len(parenth_stack) == 0:
                    return False
                if parenth_stack.pop() == parenth_pair[s[i]]:
                    continue
                else: 
                    return False
        return len(parenth_stack) == 0        



solved = Solution()
#print()
print(solved.isValid(s = "()"))
print(solved.isValid(s = "()[]{}"))
print(solved.isValid(s = "(]"))