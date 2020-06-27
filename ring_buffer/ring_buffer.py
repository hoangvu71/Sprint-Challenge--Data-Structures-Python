class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = 0
        self.storage = []
        self.count = 0

    def append(self, item):
        # if the capacity is not met
        if self.current_capacity < self.capacity:
            self.current_capacity += 1
            self.storage.append(item)
        
        # if the capacity is full
        elif self.current_capacity == self.capacity:
            self.storage.pop(self.count)
            self.storage.insert(self.count, item)
            self.count += 1
            if self.count >= len(self.storage):
                self.count = 0

    def get(self):
        
        # return all the items in storage
        return [num for num in self.storage if num != None]

capacity = 5
buffer = RingBuffer(capacity)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')

print(buffer.get())