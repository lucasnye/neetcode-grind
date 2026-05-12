class Solution:
    import heapq, math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.euclidean_distance(p, [0, 0]), p) for p in points]
        heapq.heapify(distances)
        return [heapq.heappop(distances)[1] for _ in range(k)]
    
    def euclidean_distance(self, p1: List[int], p2: List[int]) -> float:
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)