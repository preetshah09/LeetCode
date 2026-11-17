class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums): # enumerate -> stores both Index and Value of a List
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

        return []  