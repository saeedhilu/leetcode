class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print("s.",s.replace(" ",""))
        # pallindromic_value = ""
        # for i in s:
        #     if i not in [',',':',' ']:
               
        #         pallindromic_value += i.lower()
        
        left , right = 0 , len(s) - 1
        is_pallindrome = True
        while left < right:
            if not s[left].isalnum():
                left  += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
          

            if s[left].lower() != s[right].lower():
                is_pallindrome = False
                break
            left += 1
            right-= 1
        return is_pallindrome
            
        