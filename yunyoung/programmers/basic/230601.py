# 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

# 문자열로 변환
def solution(n):
    answer = str(n)
    return answer

# 소문자로 바꾸기
def solution(myString):
    return myString.lower()

# n의 배수
def solution(num, n):
    return 1 if num%n==0 else 0

# 배열 두배 만들기
def solution(numbers):
    return list(map((lambda x: x * 2), numbers))

# flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    return a+b if flag else a-b

# 배열 원소의 길이

"""
참고 답안

    answer = [len(i) for i in strlist]
    answer = list(len, strlist))

"""
def solution(strlist):
    answer = list(map(lambda x:len(x), strlist))
    return answer

# 정수 부분 
def solution(flo):
    return int(flo)

#! -------------------- 220518 --------------------
#TODO 정답률 89% 

# 부분 문자열인지 확인하기
def solution(my_string, target):
    return 1 if target in my_string else 0

# 정수 찾기
def solution(num_list, n):
    return 1 if n in num_list else 0

# 피자 나눠 먹기 (1)
def solution(n):
    return  (n+6)//7

#피자 나눠 먹기 (3)
def solution(slice, n):
    return (n+(slice-1))//slice

#원소들의 곱과 합

#TODO 다른 풀이 eval(expression)
"""
 def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0

"""
def solution(num_list):
    multi = 1 
    for n in num_list:
        multi *= n
    return 1 if multi<sum(num_list)**2 else 0

# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    return ''.join(arr)

# 카운트 업
def solution(start, end):
    return [ n for n in range(start,end+1)]

# 대문자로 바꾸기
def solution(myString):
    return myString.upper()

#TODO 다른 풀이 
"""
def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]
"""
#조건에 맞게 수열 변환하기 3
def solution(arr, k):
    return list(map(lambda n : n+k, arr)) if k %2 ==0 else list(map(lambda n : n*k, arr))

# 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

# 편지 
def solution(message):
    return len(message)*2

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,"")


# 문자열 뒤집기
def solution(my_string):
    return my_string[-1::-1]

# 옷가게 할인 받기
#! 정확성: 90.0
def solution(price):
    price = price * 0.8 if price >= 500000 else price * 0.9  if price >=300000 else price * 0.95 if price >= 100000 else price 
    return price

def solution(price):
    discount = 0.8 if price >= 500000 else  0.9 if price >=300000 else 0.95 if price >= 100000 else 1  
    return price * discount

#! 정답
def solution(price):
    if price >= 500000:
        discounted = price * 0.8
    elif price >= 300000:
        discounted = price * 0.9
    elif price >= 100000:
        discounted = price * 0.95
    else:
        discounted = price

    return int(discounted) #int가 없으면 실패 


# 배열의 유사도
def solution(s1, s2):
    if len(s2) > len(s1):
        answer = len(s2) - len(set(s2) - set(s1))
    else:
        answer = len(s1) - len(set(s1) - set(s2))
    return answer

#TODO 다른 풀이 
def solution(s1, s2):
    return len(set(s1)&set(s2));

def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return len(s1.intersection(s2))

# 짝수 홀수 개수
def solution(num_list):
    even = sum(1 for n in num_list if n % 2 == 0)
    odd = sum(1 for n in num_list if n % 2 != 0)
    return [even, odd]

#TODO 다른 풀이 
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

def solution(num_list):
        return [sum(1 for n in num_list if n % 2 == 0), sum(1 for n in num_list if n % 2 != 0)]


#점의 위치 구하기
def solution(dot):
    quad = 0
    if dot[0] < 0 and dot[1] > 0:
        quad = 2
    elif  dot[0] > 0 and dot[1] > 0:
        quad = 1
    elif  dot[0] < 0 and dot[1] < 0:
        quad = 3
    else:
        quad = 4
    
    return quad

#TODO 다른 풀이 
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]


# 아이스 아메리카노
def solution(money):
    return [money // 5500, money % 5500]


# 공백으로 구분하기 1
def solution(my_string):
    return my_string.split(' ')


#뒤에서 5등 위로
def solution(num_list):
    num_list.sort()
    return num_list[5:]

# 첫 번째로 나오는 음수
def solution(num_list):
    for idx, n in enumerate(num_list) : 
        if n < 0:
            return idx
    
    return -1


# 모음 제거
def solution(my_string):
    v = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([w for w in my_string if w.lower() not in v])
    return result

#TODO 다른풀이
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])


# 삼각형의 완성조건 (1)
def solution(sides):
    max_val = max(sides)
    return 1 if sum(sides) - max_val > max_val else 2


# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array)//2]


# 중복된 숫자 개수
def solution(array, n):
    cnt = [ 0 for i in range(max(array)+1)]
    for i in array: cnt[i]+=1
    return cnt[n]

#TODO 다른 사람 풀이
def solution(array, n):
    return array.count(n)

# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    sentence = ''.join([my_string[idx] for idx in index_list])

    return sentence

import math

#순서쌍의 개수
def solution(n):
    nums = [i for i in range(1, n+1)]
    divisors = [i for i in nums if n % i == 0]
    return len(divisors)


#문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

# 최댓값 만들기 (1)
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]


# 머쓱이보다 키 큰 사람
def solution(array, height):
    count = 0
    for h in array:
        if h > height:
            count += 1

    return count

# 자릿수 더하기 
def solution(n):
    return sum(int(num) for num in str(n))

# 문자 반복 출력하기
def solution(my_string, n):
    return "".join([w*n for w in my_string ])

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    return sum([int(n) for n in my_string if n.isdigit()])

# 짝수는 싫어요
def solution(num):
    odd_list = [n for n in range(1,num+1) if n%2==1]
    odd_list.sort()
    return odd_list

# TODO 다른 사람 풀이 
def solution(n):
    return [i for i in range(1, n+1, 2)]


# 문자열 정수의 합
def solution(num_str):
    return sum(int(n) for n in num_str)

# 카운트 다운
def solution(start, end):
    answer = [n for n in range(start , end-1, -1)]
    return answer

# 수 조작하기 1
def solution(n, control):
    results = n
    controls_num = {'w' : 1 , 's' : -1,  'd' : 10, 'a' : -10 }
    for w in control: results+=controls_num[w]

    return results

# TODO 다른 사람 풀이 
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])

# 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    answer = [ w.lower() if idx%2==0 else w.upper() for idx, w in enumerate(strArr)  ] 
    return answer

# n보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for num in numbers:  
        answer += num 
        if answer >n: 
            return answer

# TODO  next() 함수는 이터레이터(iterator)에서 다음 요소를 반환하는 함수입니다
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1+str2)

# 이어 붙인 수
def solution(num_list):
    even = int("".join([str(n) for n in num_list if n%2==0]))
    odd = int("".join([str(n) for n in num_list if n%2==1]))

    return even+odd

#꼬리 문자열
def solution(str_list, ex):
    sentence = str("".join([s for s in str_list if ex not in s]))
    return sentence

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    answer = [n // 2 if (n >= 50) and (n % 2 == 0) else n * 2 if (n < 50) and (n % 2 == 1) else n for n in arr]

    return answer

# n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

#길이에 따른 연산
import math
def solution(num_list):
    result = sum(num_list) if len(num_list)>=11 else math.prod(num_list)
    return result

# 배열 만들기 1
def solution(n, k):
        answer = [num for num in range(1,n+1) if num%k==0 ]
        return answer

# 원하는 문자열 찾기
def solution(myString, pat):    
    return int(pat.lower() in myString.lower()
)

# 마지막 두 원소
def solution(num_list):
    num_list.append(num_list[-1]-num_list[-2]) if num_list[-1]>num_list[-2] else num_list.append(num_list[-1]*2)
    return num_list

# 부분 문자열
def solution(str1, str2):
    return int(str1 in str2)
