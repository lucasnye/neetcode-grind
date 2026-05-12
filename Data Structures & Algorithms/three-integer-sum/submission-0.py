class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        # Naive O(n^3) approach
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)
        return result