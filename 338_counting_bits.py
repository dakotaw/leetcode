class Solution(object):
    def countBits(self, num):
        counts = []
        for i in range(num + 1):
            counts.append(sum([int(x) for x in str(bin(i)[2:])]))
        return counts