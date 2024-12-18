class Solution(object):
    def fib(self, n):
        """
        # :type n: int
        # :rtype: int
        # """
        # fab = [0,1]
        # if n == 2:
        #     return 1
        # for i in range(n):
        #     fab_new_value = fab[i] + fab[i+1]
        #     # print(fab_new_value)
        #     fab.append(fab_new_value)
        
        # return fab[n]       
        pre, curr = 0,1
        if n == 0 :
            return 0
        if n == 1:
            return 1
        for _ in range(2,n+1):
            pre, curr = curr, pre + curr
        return curr