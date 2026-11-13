class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right: #if I write left<=right it shows Time limit Exceeded Error
            mid = (left+right)//2

            hours = 0
            for pile in piles:
                hours+= (pile + mid-1)//mid # it's -1 because Python uses Ceil Value and we need Floor Value

            if hours <= h:
                right = mid
            else:
                left = mid+1

        return left