![Koko Eating Bananas](koko-bananas.png)
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left = 1
        right = max(piles)

        while left <= right:
            hours = 0
            mid = (left+right) // 2

            for p in piles:
                hours+=math.ceil(p/mid)

            if hours<=h:
                right = mid - 1
            else:
                left = mid + 1    
        return left            

        
