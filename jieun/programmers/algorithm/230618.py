
#TODO 스택 / 큐

#_  같은 숫자는 싫어

#* 새로운 원소를 넣기 전에 검사
def solution(arr):
    answer = []
    
    for idx_arr in range(len(arr)):
        if idx_arr == 0:
            answer.append(arr[idx_arr])
            tmp = arr[idx_arr]
        else:
            if arr[idx_arr] != tmp:
                answer.append(arr[idx_arr])
            tmp = arr[idx_arr]
    return answer


# # 다른 풀이 

#* 새로운 원소를 일단 넣고 전이랑 같은지 검사
def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        
        if len(answer) == 1:continue
        else:
            if answer[-2] == answer[-1]: 
                answer.pop()
    
    return answer


# # 다른 풀이 

#* 함수
def solution(arr):
    answer = []
    answer.append(arr[0])
    for val in arr[1:]:
        if answer[-1] == val:continue
        answer.append(val)
    return answer
        
#_  기능개발

from math import ceil

#* 코드는 실행되나 일부 테스트에서 런타임 에러
def solution(progresses, speeds):
    dayLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1 #* 각 날마다 배포될 프로세스 수를 저장
    publishList = [] #* 함수의 출력 (각 날마다 배포되는 프로세스 수를 담은 리스트)
    for idx in range(len(dayLeft)):
        try:
            if dayLeft[idx] < dayLeft[idx + 1]: 
                publishList.append(count)
                count = 1 #* 초기화
            else:
                dayLeft[idx + 1] = dayLeft[idx] 
                count += 1
        except IndexError:
            publishList.append(count)
    return publishList


# # 다른 풀이 

#* 스택

from math import ceil
def solution(progresses, speeds):
    answer = []
    dayLeft = list(map(lambda x : (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    for idx in range(len(dayLeft)):
        if idx == 0:
            answer.append(1)
        else:
            if max(dayLeft[:idx]) >= dayLeft[idx]:
                answer[-1] += 1
            else:
                answer.append(1)
    return answer

#_  올바른 괄호

#* 스택
def solution(s):
    stack = []
    
    for word in list(s):
        if word == ('('):
            stack.append(word)
        else:
            try:
                stack.pop() #* 닫힌 괄호 차례이면, 닫힌 괄호 넣지 않고, 열린 괄호 빼버림
            except IndexError:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False


#_ 프로세스

priorities = [2, 1, 3, 2]
location = 2

#* priorities 숫자가 클수록 우선순위가 높다.

#* process = [A, B, C, D]
#* location (인덱스를 의미)

#* 1. 큐에서 A를 꺼낸다 -> 우선순위를 체크 -> C의 우선순위가 더 높음 -> A를 큐에 맨 뒤로 집어넣음. 큐: [B, C, D, A]
#* 2. 큐에서 B를 꺼낸다 -> 우선순위를 체크 -> C의 우선순위가 더 높음 -> B를 큐에 맨 뒤로 집어넣음. 큐: [C, D, A, B]
#* 3. 큐에서 C를 꺼낸다 -> 우선순위를 체크 -> C를 그대로 실행. 큐: [D, A, B], 실행: [C]
#* 4. 큐에서 D를 꺼낸다 -> 우선순위를 체크 -> (D도 우선순위가 2고, A도 2이므로) D를 그대로 실행. 큐: [A, B], 실행: [C, D]
#* 5. 큐에서 A를 꺼낸다 -> 우선순위를 체크 -> (A는 우선순위가 2고, B는 1이므로) A를 그대로 실행. 큐: [B], 실행: [C, D, A]
#* 6. 큐에서 B를 꺼낸다 -> 우선순위를 체크 -> B를 그대로 실행. 큐: [], 실행: [C, D, A, B]

def solution(priorities, location):
    #* 위치와 우선순위를 저장한 큐를 생성
    myQueue = [(idx, priorities) for idx, priorities in enumerate(priorities)]
    #* answer : 몇 번째 실행인지 저장하는 변수
    answer = 0
    while True:
        #* 큐에서 맨 앞에 요소를 빼내고
        current = myQueue.pop(0)
        
        #* any : 안에 조건 중 하나라도 있으면,
        #* myQueue 안에 (인덱스, 우선순위) 튜플 중 우선순위 값들을 비교
        if any(current[1] < q[1] for q in myQueue):
            myQueue.append(current)
        else:
            #* current 현재 우선순위가 제일 높은 상황
            #* answer : 몇 번째 실행인지 저장하는 변수
            answer += 1
            if current[0] == location:
                return answer
