from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common((1))[0][0]
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow