import math, numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        numpy_piles = np.array(piles)
        if h == n:
            return max(piles)

        upper_bound = max(piles)
        lower_bound = int(np.ceil(sum(piles) / h))

        if int(np.sum(np.ceil(numpy_piles / lower_bound))) <= h:
            return lower_bound

        possible_k = range(lower_bound + 1, upper_bound)
        smallest_k = float('inf')
        left, right = 0, len(possible_k) - 1
        while left < right:
            mid = left + (right - left) // 2
            if int(np.sum(np.ceil(numpy_piles / possible_k[mid]))) > h:
                left = mid + 1
            else:
                right = mid - 1
        return possible_k[left] 