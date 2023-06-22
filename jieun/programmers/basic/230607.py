
#_ 공백으로 구분하기 1
def solution(my_string):
    return [i for i in my_string.split()]

#_ 짝수는 싫어요
def solution(n):
    return [i for i in range(1, n+1) if i % 2 == 1]

#_ 원하는 문자열 찾기
def solution(myString, pat):
    if pat.lower() in myString.lower(): 
        return 1 
    return 0

#_ 부분문자열
def solution(str1, str2):
    if str1 in str2: 
        return 1
    return 0

#_ 첫번째로 나오는 음수
def solution(num_list):
    for i in num_list:
        if i < 0:
            result = num_list.index(i)
            return result
    if i > 0:
        result = -1
        return result

# # 다른 풀이 
def solution(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] < 0: return idx
        
    return -1

#_ 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    result = []
    for i in range(len(strArr)):
        if i % 2 == 1:
            result.append(strArr[i].upper())
        else:
            result.append(strArr[i].lower())
    return result

# # 다른 풀이 
def solution(strArr):
    return [word.lower() if idx % 2 == 0 else word.upper() for idx, word in enumerate(strArr)]

#_ n개 간격의 원소들
def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]

#_ 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1 + str2)

#_제곱수 판별하기
import numpy as np 
def solution(n):
    if int(np.sqrt(n)) ** 2 == n:
        return 1
    return 2

#_배열 만들기1
def solution(n, k):
    return [k * (i + 1) for i in range(n // k)]

#_ 조건에 맞게 수열 변환하기1
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2)
        elif i < 50 and i % 2 == 1:
            answer.append(i * 2)
        else:
            answer.append(i)
    return answer

#_ 이어 붙인 수
def solution(num_list):
    odd = ''
    even = ''
    for i in num_list:
        if i % 2 == 1:
            odd += str(i)
        else:
            even += str(i)
            
    return int(odd) + int(even)

#_ 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

#_ 접두사인지 확인하기
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0

#_ 수 조작하기1
def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        else:
            n -= 10
    return n

#_ 홀짝 구분하기
n = int(input())
if n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')
    
    
#_주사위 게임1
def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)

#_ 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    try:
        if alp in my_string:
            res = my_string.replace(alp, alp.upper())
        return res
    except:
        return my_string

#_ 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list

#_ 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex in i:
            pass
        else:
            answer += i
    return answer 

#_ n번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

#_ 문자열 안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

#_ A 강조하기
def solution(myString):
    return myString.lower().replace('a', 'A')

#_ 뒤에서 5등 위로
def solution(num_list):
    return sorted(num_list)[5:]

#! 접미사인지 확인하기 -> 일부 테스트 에러

#_ 뒤에서 5등 까지
def solution(num_list):
    return sorted(num_list)[:5]

#_공백으로 구분하기
def solution(my_string):
    return my_string.split()

