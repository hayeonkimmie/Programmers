
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


#_ 기능개발 
#TODO 
#progresses  	            speeds	             return
#[93, 30, 55]	            [1, 30, 5]           [2, 1]
#[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	 [1, 3, 2]

import math 

def solution(progresses, speeds):
    answer = [1]
    day = []
    rest = 1
    
    for i, p in enumerate(progresses):
        day.append(math.ceil((100 - p) / speeds[i]))
        
    for i, d in enumerate(day):
        rest = 1
        if sum(answer) == len(day):
            break
        if len(day) > (i + 1) and d > day[i + 1] :
            rest += 1
            continue
        else:
            rest = 1

        answer.append(rest)
    
    print(day)
    print(answer)


p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

solution(p,s)