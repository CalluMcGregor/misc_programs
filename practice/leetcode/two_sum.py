from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #use enumerate to get the index and value of each number in the list
        for index, number in enumerate(nums):
            # if the target minus the current number is in seen, then we know it is the answer, return the index
            if target - number in seen:
                return ([seen[target - number], index])
            #if the number is not in seen, add the number to the dictionary with index as the value
            elif number not in seen: 
                seen[number] = index

test = Solution()
calc = test.twoSum(nums=[1,2,3,4,5], target=9)

print(calc)