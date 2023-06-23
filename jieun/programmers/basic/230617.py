
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




