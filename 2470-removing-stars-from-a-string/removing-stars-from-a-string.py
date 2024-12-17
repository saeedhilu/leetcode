class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result) 