class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        0000
        1000 0100 0010 0001 9000 0900 0090 0009
        1100 1010 1001 2000
        '''
        deadends = set(deadends)
        q = deque(['0000'])
        lvl = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == target:
                    return lvl
                if current in visited or current in deadends:
                    continue
                visited.add(current)
                for i in range(4):
                    newValue = list(current)
                    newValue[i] = str((int(current[i]) + 1) if int(current[i]) < 9 else 0)
                    newStr = ''.join(newValue)
                    q.append(newStr)
                    newValue[i] = str((int(current[i]) - 1) if int(current[i]) > 0 else 9)
                    newStr = ''.join(newValue)
                    q.append(newStr)
            lvl += 1
        return -1



