class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-stone for stone in stones]

        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1, stone2 = -heapq.heappop(stones), -heapq.heappop(stones)
            
            if stone1 > stone2:
                stone1 -= stone2
                heapq.heappush(stones, -stone1)
        
        return -heapq.heappop(stones) if stones else 0