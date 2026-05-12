class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        # Naive O(n^3) approach
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = [nums[i], nums[j], nums[k]]
        #                 triplet.sort()
        #                 if triplet not in result:
        #                     result.append(triplet)
        
        # O(n^2) approach
        # First sort the array
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