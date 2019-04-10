#stack
 
class stack:
    def __init__(self):
                 
        self.items=[] 
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.items==[]:
            return self.items[-1]
    def push(self,item):
        self.items.append(item)
    def pop(self):
       return self.items.pop()
    def get_list(self):
        return self.items
s=stack()
s.push('a')
s.push('y')
s.push('g')
print(s.get_list())
s.pop()
print(s.get_list())
print(s.is_empty())
