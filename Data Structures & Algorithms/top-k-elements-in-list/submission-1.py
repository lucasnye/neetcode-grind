class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 0
        
        freq = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return [freq[j][0] for j in range(k)]