# 9th percentile.

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        return Counter(nums).most_common()[0][0]

# 26th percentile.

class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        max_count = 0
        max_num = None
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
            if counter[num] > max_count:
                max_count = counter[num]
                max_num = num
        return max_num