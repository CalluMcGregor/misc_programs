class Solution:
    def isValid(self, s: str) -> bool:
        """return true if valid brackets, false if invalid brackets"""
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            #if open bracket, append to stack
            if char in bracket_pairs.values():
                stack.append(char)
            #if closed bracket
            elif char in bracket_pairs.keys():
                #if stack empty, or the last item in stack is not == the same 
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False

        return not stack

testcase = Solution()
test = testcase.isValid("()[]{}")
print(test)