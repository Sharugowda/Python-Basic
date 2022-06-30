from typing import List

class easy_1_Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    def twoSum_Good(self, nums: List[int], target: int) -> List[int]:

        seen_nums = {}
        
        for i, num in enumerate(nums):
            if target - num in seen_nums:
                return([seen_nums[target - num], i])
            elif num not in seen_nums:
                seen_nums[num] = i

easy_1 = easy_1_Solution()
nums = [2,3,4,5,6,7,8,9]
target  = 9
result = easy_1.twoSum_Good(nums,target)
print(f"result: {result}")
