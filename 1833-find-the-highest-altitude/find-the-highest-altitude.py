class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        new_list = [0]
        for g in gain:
            value = new_list[-1] + g
            new_list.append(value)
        return max(new_list)
        