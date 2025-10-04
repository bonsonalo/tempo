class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self): # we don't need item here because it already knowwn what it is(it is the last one to be put in the stack)
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0