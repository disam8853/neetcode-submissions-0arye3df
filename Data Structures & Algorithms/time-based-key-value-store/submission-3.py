class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.mp:
            self.mp[key] = []
        self.mp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.mp:
            return ""
        ls = sorted(self.mp[key])
        l = 0
        r = len(ls)
        while l < r:
            mid = l + (r-l)//2
            if ls[mid][0] == timestamp:
                return ls[mid][1]
            elif ls[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
        return ls[l-1][1] if l > 0 else ""

