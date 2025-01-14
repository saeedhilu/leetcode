class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10 :
            return False
        checking_value = 10
        while n >= checking_value:
            n -= checking_value 
            checking_value -= 1
        
        return checking_value % 2 != 0 
            

        