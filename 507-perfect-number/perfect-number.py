class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        print(num ** 0.5)
        result = 1
        if num <= 1:
            return False
            
        for i in range(2,int(num ** 0.5)+1):
            if num % i == 0:
                result += i

                if i != num // i:
                    print('i and num // i',i , num,num // i)
                    result += num // i
                else:
                    print(' else i and num // i',i , num,num // i)
        print(result)
        return result == num


        