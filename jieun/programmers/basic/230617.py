
#_ 문자열 출력하기

str = input()
print(str)

#_ a와 b 출력하기

a, b = map(int, input().strip().split(' '))
print(f'a = {a}')
print(f'b = {b}')

#_ 문자열 반복해서 출력하기

a, b = input().strip().split(' ')
b = int(b)
print(a * b)

#_ 대소문자 바꿔서 출력하기

str = input()
print(str.swapcase())

#_ 덧셈식 출력하기

a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')


# _ 특수문자 출력하기
#? 헷갈림

print("!@#$%^&*(\\'\"<>?:;")

# _ 문자열 돌리기

str = input()
for i in str:
    print(i)
    
#_ 문자열 겹쳐쓰기

#! return 값이 너무 길어서 효율적인지 의문
def solution(my_string, overwrite_string, s):
    return my_string[:s] + my_string[s:s+len(overwrite_string)].replace(my_string[s:s+len(overwrite_string)], overwrite_string) + my_string[s+len(overwrite_string):]

#_ 문자열 섞기

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += (str1[i] + str2[i])
    return answer

#_ 두 수의 연산값 비교하기

def solution(a, b):
    cond1 = int(str(a) + str(b))
    cond2 = 2 * a * b
    return max(cond1, cond2)

#_ 홀짝에 따라 다른 값 반환하기

def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1, n+1):
            if i % 2 == 1:
                answer += i
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += (i * i)
    return answer

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



