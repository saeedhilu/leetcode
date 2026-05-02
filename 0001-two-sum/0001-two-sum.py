class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for  index , item in enumerate(nums):
            print("item is :", item , index)
            value = target - item
            if  value in seen:
                return [seen[value], index]

            seen[item] = index
               

            

        