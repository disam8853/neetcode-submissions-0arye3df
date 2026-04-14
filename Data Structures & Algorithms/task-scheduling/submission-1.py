class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        pq = [-val for val in cnt.values()]
        heapq.heapify(pq)
        rest = deque()
        curTime = 0
        while pq or rest:
            curTime += 1
            while rest and rest[0][0] <= curTime:
                newVal = rest.popleft()[1]
                heapq.heappush(pq, newVal)
            if not pq:
                continue
            top = heapq.heappop(pq)
            # print(curTime, top, pq, rest)
            if top + 1 < 0:
                rest.append([curTime + n + 1, top + 1])
            # print(rest)
        return curTime