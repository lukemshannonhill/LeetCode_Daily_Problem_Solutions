# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        
        # This question will be solved using a stack.
        
        # The idea is: a valid push to the stack consists of a left paren (of any type). 
        
        # We will process the string one element at a time, starting from the leftmost element.
        
        # For each element, if that element is a left paren, it is okay to push it onto the stack.
        
        # If that element is a right paren, we must check to see whether the top of the stack is that right paren's left
        # equivalent. If it is, we proceed (and pop the top of the stack). If it isn't, we return false.
        
        # If we reach the end of the list, we ask: Is the stack empty? If it is, we return true. 
        
        # If we ever encounter a right paren with an empty stack, we return false.
        
        stack = []
        
        mirror = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or '}' or ']':
                if stack == []:
                    return False
                elif stack[-1] == mirror[i]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False
