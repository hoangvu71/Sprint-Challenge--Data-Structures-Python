class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = 0
        self.storage = []
        self.count = 0
    def append(self, item):
        # If size of current_capacity less than capacity
        if self.current_capacity < self.capacity:
            self.storage.append(item)
            self.current_capacity += 1

        # If size of current_capacity is equal to capacity
        elif self.current_capacity == self.capacity:
            self.storage.pop(self.count)
            self.storage.insert(self.count, item)
            self.count += 1
            if self.count >= self.capacity:
                self.count = 0


    def get(self):
        return self.storage




