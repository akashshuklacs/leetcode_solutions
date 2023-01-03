class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        stack= list()        
        for sym in s:
            if sym in "({[":
                stack.append(sym)
            else:
                if len(stack)==0 or sym != brackets[stack.pop()] :
                    return False
        return len(stack)==0