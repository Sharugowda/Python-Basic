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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_list = []
        for i in range(0,len(nums)):
            if i < len(nums)-1:
                if nums[i] + nums[i+1] == target:
                    out_list.append(i)
                    out_list.append(i+1)
        return out_list

easy_1 = easy_1_Solution()
nums = [2,3,4,5,6,7,8,9]
target  = 9
result = easy_1.twoSum(nums,target)
print(f"result: {result}")