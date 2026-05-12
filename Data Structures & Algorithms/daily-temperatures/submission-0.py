class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not s:
                s.append((i, temp))
                continue
            while s and temp > s[-1][1]:
                data = s.pop()
                result[data[0]] = i - data[0]
            s.append((i, temp))
        
        while s:
            data = s.pop()
            result[data[0]] = 0

        return result