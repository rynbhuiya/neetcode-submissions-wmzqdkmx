class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap
        heapq.heapify(self.left)
        heapq.heapify(self.right) 

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        # rebalance array
        if len(self.left) > len(self.right) + 1:
            temp = heapq.heappop(self.left)
            heapq.heappush(self.right, -temp)
        if len(self.right) > len(self.left) + 1:
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -temp)

    def findMedian(self) -> float:
        # check total length
        sumLength = len(self.left) + len(self.right)
        
        if sumLength % 2 == 0:
            # even length
            num1 = -self.left[0]
            num2 = self.right[0]
            return (num1 + num2) / 2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()