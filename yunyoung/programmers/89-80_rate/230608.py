
#! 정답률 %89
# rny_string
def solution(rny_string):
    return rny_string.replace('m', 'rn')

# n개 간격의 원소들
def solution(num_list, n):
    return num_list[::n]

# TODO any 함수 사용 - iterable 한 자료형을 입력 받았을때 하나라도 조건에 만족하면 TRUE 반환 
# 접두사인지 확인하기
def solution(my_string, is_prefix):
    answer = 1 if any(is_prefix == my_string[:n]  for n in range(len(my_string))) or is_prefix == my_string else 0
    return answer

#? 다른 사람 풀이  startswith
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

#! 풀이 궁금 
# 주사위 게임 1
def solution(a, b):
    if a*b % 2 ==1:
        answer = a*a + b*b
    elif (a+b) % 2 == 1:
        answer = 2*(a+b)
    else :
        answer = abs(a - b)
    return answer

# 문자열안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2
 
# 배열의 원소만큼 추가하기
def solution(arr):
    answer = []
    for a in arr:
        for n in range(a):
            answer.append(a)
        
    return answer

#? 다른 풀이
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer

def solution(arr):
    return [i for i in arr for j in range(i)]


# 제곱수 판별하기
import math
def solution(n):
    return 1 if math.sqrt(n)%1==0 else 2

#? 다른 풀이 
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 문자열 곱하기
def solution(my_string, k):
    return my_string * k

# 접미사인지 확인하기
def solution(my_string, is_suffix):
        return int(my_string.endswith(is_suffix))

# A강조하기
def solution(myString):
    return myString.lower().replace('a', 'A')

# 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

# 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    if len(arr) % 2 == 1:
        answer = [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]
    else:
        answer = [arr[i] + n if i % 2 == 1 else arr[i] for i in range(len(arr))]


#? 다른 풀이
def solution(arr, n):
    return [x+n if (len(arr)+i)%2!=0 else x for i, x in enumerate(arr)]


#! 정답률 88% 

# 개미 군단
def solution(hp):
    return hp//5 + (hp%5)//3 + (hp%5)%3

# 공백으로 구분하기 2
def solution(my_string):
    return my_string.split()

# 더 크게 합치기
a = 9
b = 91

if str(a)[0] > str(b)[0]:
    print(str(a)+str(b))
elif str(a)[0] == str(b)[0]:
    print(str(b)+str(a))


