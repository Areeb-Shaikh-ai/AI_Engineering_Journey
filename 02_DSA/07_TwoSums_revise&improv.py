'''
The Algoithm is as follows:
Take an input list, and target
create a dictionary seen
Loop through the list
remember the no. in the dictionary, and keep the 
target in the variable, try if th value can be target, 
if target is there in the list You output, both nums and 
their index
'''
#Leetcode #1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
