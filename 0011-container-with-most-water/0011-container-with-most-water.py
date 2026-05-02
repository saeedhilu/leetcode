class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0 
        left , right = 0 , len(height) - 1
        print('lef and right is :', left , right )
        while  right > left :
            print('hey')
            width = right - left
            current = min(height[left], height[right]) * width
            result = max(result, current)
            if height[left] - height[right] < 0:
                left += 1
            else :
                right -= 1
                
        return result 

