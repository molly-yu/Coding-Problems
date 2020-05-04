# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Solution by Molly Yu

# First Attempt using stack and if-else (works if there are other characters present)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        beginning = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                beginning.append(s[i])
            if s[i] == ')':
                if not beginning or (beginning[len(beginning)-1] != '('):
                    return False
                else:
                    beginning.pop()
            if s[i] == ']':
                if not beginning or (beginning[len(beginning)-1] != '['):
                    return False
                else:
                    beginning.pop()
            if s[i] == '}':
                if not beginning or (beginning[len(beginning)-1] != '{'):
                    return False
                else:
                    beginning.pop()    
        if not beginning:
            # print("true")
            return True

    isValid(1,"[]{}")


    # Using map to keep track (simpler code)
    def isValidImproved(self, s):
        stack = []
        map = {")": "(", "]": "[", "}":"{"} # hash map where key=open brackets, value=closed brackets
        for char in s:
            if char in map: # if closing bracket
                if stack: # non-empty
                    top_elt = stack.pop()
                else:
                    top_elt = '#'
                if map[char] != top_elt: # check if opening bracket top_elt is equal to the mapping of the closed bracket
                    return False
            else:
                stack.append(char) # append open brackets to stack

        return not stack # if empty, returns true
    isValidImproved(1,"[]{}")


    # A Clever Approach
    def isValidClever(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''


