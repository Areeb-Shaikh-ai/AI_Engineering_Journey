"""
LeetCode #977: Squares of a Sorted Array
Strategy: Two-Pointer (Optimal O(n) Time)
Key Learning: Filling the result array from largest to smallest 
avoids an expensive sort.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[None]*len(nums)
        left = 0
        right = len(nums) -1 
        pos = len(nums) -1

        while left <= right:
            if nums[left]**2 > nums[right]**2:
                res[pos] = nums[left]**2
                left += 1
            else :
                res[pos] = nums[right]**2
                right -= 1
            pos -= 1
        return res


