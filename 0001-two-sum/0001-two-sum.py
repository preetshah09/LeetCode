class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            for j in range (i+1,len(nums)):
                sum1 = nums[i] + nums[j]
                if sum1 == target:
                    return ([i,j])