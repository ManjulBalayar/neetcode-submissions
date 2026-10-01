import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list = []
        prefix = 1

        # left / prefix products
        for i in range(len(nums)):
            pre_list.append(prefix)
            prefix *= nums[i]

        post_list = [1] * len(nums)
        postfix = 1

        # right / postfix products
        for i in range(len(nums) - 1, -1, -1):
            post_list[i] = postfix
            postfix *= nums[i]

        result = [x * y for x, y in zip(pre_list, post_list)]

        return result
        
        
        