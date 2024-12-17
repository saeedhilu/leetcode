class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0 :
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
            
                pre_value = (i == 0 or flowerbed[i - 1] == 0)
                new_value = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if pre_value and new_value :
                    flowerbed[i] = 1
                    n -= 1 
                if n == 0:
                    return True
        return n == 0