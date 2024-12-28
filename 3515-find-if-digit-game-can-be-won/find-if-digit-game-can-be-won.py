class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for n in nums:
            if n < 10 :
                count += n

        return count != sum(nums) // 2 or sum(nums)  % 2 != 0