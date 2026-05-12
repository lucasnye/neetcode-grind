from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        count = Counter(tasks)
        
        # Max heap (negate counts for Python's min heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        queue = []  # stores (count, idle_time)
        
        while maxHeap or queue:
            time += 1
            
            if maxHeap:
                # Process most frequent task
                cnt = heapq.heappop(maxHeap) + 1  # +1 because negative
                if cnt != 0:  # Still has remaining tasks
                    # Add back to queue with cooldown
                    queue.append((cnt, time + n))
            
            # Check if any task's cooldown is over
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.pop(0)[0])
        
        return time
        