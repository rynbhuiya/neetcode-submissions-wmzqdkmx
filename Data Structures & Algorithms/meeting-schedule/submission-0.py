"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            for j in range(i + 1, len(intervals)):
                if start >= intervals[j].end or end <= intervals[j].start:
                    continue
                else:
                    return False
        

        return True