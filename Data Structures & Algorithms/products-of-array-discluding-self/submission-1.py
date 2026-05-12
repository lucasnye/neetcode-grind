class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output.append(product)
        # return output

        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result