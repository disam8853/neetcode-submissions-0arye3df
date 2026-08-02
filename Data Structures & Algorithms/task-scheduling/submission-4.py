class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        q = deque() # (time, num)
        hq = [] # (-frequency)
        for f in freq:
            heapq.heappush(hq, (-f))
        curTime = 0
        while hq or q:
            curTime += 1
            if q and q[0][0] <= curTime:
                _, remain = q.popleft()   
                heapq.heappush(hq, remain)
            if not hq:
                curTime = q[0][0] - 1
                continue
            f = heapq.heappop(hq)
            if f < -1:
                q.append((curTime + n + 1, f + 1))

        return curTime