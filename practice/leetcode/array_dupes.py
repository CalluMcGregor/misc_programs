class Solution:
    def ArrayDuplicates(self, array1: list, array2: list) -> list:
        """"""
        # new_array = []
        # for num in array1 + array2:
        #     if num not in new_array:
        #         new_array.append(num)
        # new_array.sort()
        # return new_array
        combined = array1 + array2
        new_array = list(set(combined))
        new_array.sort()
        return new_array



array1 = [1, 4, 8, 1, 2, 4]
array2 = [1, 4, 6, 10, 2, 8]

testcase = Solution()
test = testcase.ArrayDuplicates(array1, array2)
print(test)