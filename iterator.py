class remoteControl():
    def __init__(self):
        self.channels = ["HBO","CNN","Star Sports"]
        self.index = -1
    
    def _iter_(self):
        return self
    
    def _next_(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
            
        return self.channels[self.index]

r = remoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))