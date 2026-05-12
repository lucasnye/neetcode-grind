class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            timestamps, values = zip(*self.timemap[key])
            result = self.bs(timestamps, timestamp)
            return values[result] if result != -1 else ""
        else:
            return ""

    def bs(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target >= nums[mid]:
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        return result