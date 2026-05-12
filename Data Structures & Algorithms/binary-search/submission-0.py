class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        # while l <= r:
        #     mid_index = l + (r - l) // 2
        #     mid_value = nums[mid_index]
        #     if target == mid_value:
        #         return mid_index
        #     elif target > mid_value:
        #         l = mid_index + 1
        #     elif target < mid_value:
        #         r = mid_index - 1
        # return -1

        return self.bin_search(l, r, nums, target)
    
    def bin_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.bin_search(mid + 1, r, nums, target)
        else:
            return self.bin_search(l, mid - 1, nums, target)