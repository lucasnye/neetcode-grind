class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idk = {}
        
        # for index, integer in enumerate(nums):
        #     if integer in idk:
        #         idk[integer].append(index)
        #     else:
        #        idk[integer] = [index]
        
        # for integer in idk:
        #     if integer * 2 == target and len(idk[integer]) == 2:
        #         return [idk[integer][0], idk[integer][1]]
        #     elif (target - integer) in idk and idk[integer] != idk[target - integer]:
        #         smaller, bigger = min(idk[integer][0], idk[target - integer][0]), max(idk[integer][0], idk[target - integer][0])
        #         return [smaller, bigger]

        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index