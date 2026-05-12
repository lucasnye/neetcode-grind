class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initiate slow and fast pointers
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
        # Phase 1: Detect whether or not there is a cycle. If it exists, slow == fast eventually
        # Phase 2: Find the start of the cycle (that element would be the duplicate)