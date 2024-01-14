class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            replaced = haystack.replace(needle, "1")
            my_list = []
            for char in replaced:
                my_list.append(char)
            return my_list.index("1")
        else:
            return -1
        
testcase = Solution()
print(testcase.strStr("waterboatwater", "boat"))