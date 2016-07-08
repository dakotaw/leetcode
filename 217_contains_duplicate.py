# 22nd percentile.

class Solution(object):
    def containsDuplicate(self, nums):
        hash = {}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num] = True
        return False

# 80th percentile

class Solution(object):
    def containsDuplicate(self, nums):
        unique_nums = set(nums)
        if len(unique_nums) == len(nums):
            return False
        return True