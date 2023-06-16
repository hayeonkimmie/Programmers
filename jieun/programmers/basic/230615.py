
#_  암호해독
def solution(cipher, code):
    return ''.join(list(cipher)[code - 1::code])

#_ 개미군단
def solution(hp):
    res = hp // 5
    res2 = (hp - (res * 5)) // 3
    res3 = (hp - (res * 5) - (res2 * 3))
    return res + res2 + res3

#_ 접미사인지 확인하기
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

#_  더 크게 합치기
def solution(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))

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
