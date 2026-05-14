class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        nums.sort()
        # p1 iterates over every element
        for p1 in range(n - 2):
            # Skip duplicate p1s
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            # p2 and p3 find the negative of p1 s.t. p1 + p2 + p3 == 0
            p2 = p1 + 1
            p3 = n - 1
            while p2 < p3:
                total = nums[p1] + nums[p2] + nums[p3]
                if total == 0:
                    result.append([nums[p1], nums[p2], nums[p3]])
                    # Skip duplicate p2s and p3s
                    while p2 < p3 and nums[p2] == nums[p2 + 1]:
                        p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3 - 1]:
                        p3 -= 1
                    p2 += 1
                    p3 -= 1
                elif total < 0:
                    p2 += 1
                else:
                    p3 -= 1

        return result