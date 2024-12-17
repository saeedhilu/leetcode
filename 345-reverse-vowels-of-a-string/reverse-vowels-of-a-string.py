class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left , right = 0 , len(s)-1
        while left < right :
            while left < right and s[left] not in vowels:
                left +=1
            while left < right and s[right] not in vowels:
                right-=1
            if left < right:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left+=1
                right-=1
        return ''.join(s_list)        