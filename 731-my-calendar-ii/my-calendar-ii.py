class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
    def book(self, start: int, end: int) -> bool:
        for a, b in self.bookings:
            if start < b and a < end:
                maxst = max(start,a)
                minend = min( end, b)
                if self.check(maxst, minend):
                    return False
        self.bookings.append((start, end ))
        return True
    
    def check( self, start, end) -> bool:
        count = 0
        for a , b in self.bookings:
            if start < b and a < end:
                count += 1
            if count == 2:
                return True
        return False
            




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)