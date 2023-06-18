
# _ 스택/큐 

#_ 같은 숫자는 싫어 

class Stack:
    def __init__(self, items = []):
        self.items = items

    def pop(self):
        if not self.isEmpty():
              return self.items.pop()

    def push(self, item):
         self.items.append(item)

    def peek(self):
        if not self.isEmpty():
             return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
         return self.size() == 0
    
    def getItems(self):
         return self.items
    
    
#TODO Stack 이용 
#TODO 효율성 하락 

stack = Stack()
def solution(arr):
    for num in arr:
        if stack.isEmpty() or num != stack.peek():
             stack.push(num)   
    return stack.getItems()

#TODO 답 
def solution(arr):
    answer=[]
    for num in arr:
        if len(answer)==0 or num != answer[-1]:
             answer.append(num) 

    return answer



