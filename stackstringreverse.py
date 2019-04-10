
#reversing the string using stack dont use string[::-1] or string.reverse()
 
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
def reverse_string(inputstr,s): #calling a class object inside a function
#loops through the string and push content
#character by character in the stack
     
     for i in range(len(inputstr)):
         s.push(inputStr[i])
         reverse=''
     while not s.is_empty():
         reverse+=s.pop()
        
     return reverse
inputstr ='hello'
print(reverse_string(inputstr,s))
