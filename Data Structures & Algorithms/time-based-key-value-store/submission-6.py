class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.db:
            self.db[key].append([value, timestamp])
        else:
            self.db[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
            
        vals = self.db[key]
        l, r = 0, len(vals) - 1
        res = None
        while l <= r:
            mid = (l + r) // 2
            
            # check most recent
            if vals[mid][1] > timestamp:
                r = mid - 1
            else:
                # Update most recent res
                res = [vals[mid][0], vals[mid][1]]
                l = mid + 1
        
        return res[0] if res else ""
