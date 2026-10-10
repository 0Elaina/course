class Stack:
    def __init__(self, elements = None):
        if elements is None:
            self.items = []
        else:
            self.items = list(elements)
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return f"[stack] {self.items}\n[len] {len(self.items)}"
    
if __name__ == '__main__':
    s = Stack([1, 2, 3])
    print(s)
    s.push(4)
    s.push(5)
    s.pop()
    print(s)
    print(s.is_empty())
    