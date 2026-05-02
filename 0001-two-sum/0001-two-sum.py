class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for  index , item in enumerate(nums):
            value = target - item
            if  value in seen:
                return [seen[value], index]
            seen[item] = index
               

            

        