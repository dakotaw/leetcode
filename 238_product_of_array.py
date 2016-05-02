# 30th percentile.

class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        output = [1 for i in range(length)]
        
        left_product = 1
        for i in range(length):
            output[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(length - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output