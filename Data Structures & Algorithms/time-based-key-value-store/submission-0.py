class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        ary = self.mp[key]
        l = 0
        r = len(ary)
        ans = ""
        while l < r:
            mid = l + (r - l) // 2
            val, ts = ary[mid]
            if ts == timestamp:
                return val
            if ts > timestamp:
                r = mid
            else:
                ans = val
                l = mid + 1
        print(ary, l)
        return ans
