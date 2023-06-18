
#_ 약수의 합

def solution(n):
    
    return sum([Divisor for Divisor in range(1, n+1) if (n / Divisor).is_integer()])

#_ 자릿수 더하기

def solution(n):    
    return sum(map(int, list(str(n))))

#_ 짝수와 홀수

def solution(num):
    result = 'Even' if num % 2 == 0  else 'Odd'
    return result

#_ 평균 구하기

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

#_ 나머지가 1이 되는 수 찾기

def solution(n):
    for i in range(1, n+1):
        if n % i == 1:
            return i
        else:
            continue
 
# # 다른 풀이 

def solution(n):
    return [Divisor for Divisor in range(1, n+1) if n % Divisor == 1][0]

#_ X만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer

    #return [x * idx for idx in range(1, n + 1)]
    
#_ 문자열 내 p와 y의 개수

def solution(s):    
    s = s.lower()
    return True if s.count('p') == s.count('y') else False

#_ 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int,list(str(n))))
    return answer[::-1]

#_ 정수 제곱근 판별

import math

def solution(n):
    if math.sqrt(n).is_integer():
        return int((math.sqrt(n) + 1) ** 2)
    
    return -1

#_ 문자열을 정수로 바꾸기

def solution(s):
    answer = int(s)
    return answer

#_ 정수 내림차순으로 배치하기

def solution(n):
    n = sorted(list(str(n)), reverse = True)
    
    return int(''.join(n))

#_ 하샤드 수

def solution(x):
    val = sum(list(map(int, list(str(x)))))
    if x % val == 0:
        return True
    return False

#_ 두 정수 사이의 합

def solution(a, b):
    sum = 0
    
    for i in range(min(a, b), max(a, b) + 1):
        sum += i
    return sum

# # 다른 풀이 

def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2


#_ 스택/큐 - 같은 숫자는 싫어

#* 값을 하나씩 넣고 나서 마지막 값이랑 직전값이랑 비교해서 빼는 방법(스택 : LAST IN FIRST OUT)
def solution(arr):
    value_list = []
    for i in arr:
        value_list.append(i)
        if len(value_list) == 1:
            continue

        if value_list[-1] == value_list[-2]:
            value_list.pop()
    return value_list

# # 다른 풀이 

#* 넣기 전에 마지막 원소랑 넣으려는 원소랑 비교해서 빼는 방법 
def solution(arr):
    value_list = []
    value_list.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == value_list[-1]:
            continue
        else:
            value_list.append(arr[i])
    return value_list

# # 다른 풀이 

#* 원소를 넣기전에 검사하고 중복이면 넣지 않는 방법
def solution(arr):
    answer = []
    
    for word in arr:
        if len(answer) == 0:
            answer.append(word)
        else:
            if answer[-1:] == [word]: continue
            
            answer.append(word)
            
    return answer

#_ 콜라츠 추측

def solution(num):
    cnt = 0
    if num == 1:
        return 0
    
    while True:
        num = num // 2 if num % 2 == 0 else (num * 3) + 1
        cnt += 1
        if num == 1:
            return cnt
        elif cnt == 500:
            return -1
        
    return cnt
    
# # 다른 풀이 

def solution(num):
    cnt = 0
    while num != 1:
        cnt += 1
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

        if cnt == 500:
            return -1
        
    return cnt

#_  핸드폰 번호 가리기

def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer

#_ 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    res = []
    for i in arr:            
        if i % divisor == 0:
            res.append(i)
            res = sorted(res)         
        else:
            continue
        
    if len(res) == 0:
        res.append(-1)
    return res

# # 다른 풀이 

def solution(arr, divisor):
    
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

#_ 서울에서 김서방 찾기

def solution(seoul):
    return '김서방은 ' + str(seoul.index('Kim')) + '에 있다'

#_ 음양 더하기

def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            res = absolutes[i]
            sum += res
        else:
            res = absolutes[i]
            sum += (-res)
    return sum
                   
# # 다른 풀이 

def solution(absolutes, signs):
    _zip = zip(absolutes, signs)  
    return sum(absolute if sign else -absolute for absolute, sign in _zip)

#_ 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

# # 다른 풀이 

def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

#_  없는 숫자 더하기

def solution(numbers):
    return sum(range(0, 10)) - sum(numbers)

# # 다른 풀이 

def solution(numbers):
    sum = 0
    for i in range(0, 10):
        if i not in numbers:
            sum += i
            
    return sum

# # 다른 풀이 

solution = lambda x: sum(range(10)) - sum(x)

#_ 가운데 글자 가져오기

def solution(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]

# # 다른 풀이 
def solution(s):
     
    return s[(len(s)-1)//2 : len(s)//2 + 1]
    
# 짝수 2n -> n - 1, n <br>
# (len(s)-1)//2: (2n - 1) // 2 = n - 1 <br>
# len(s)//2 + 1: (2n // 2) + 1 = n + 1 <br>

# 홀수 2n - 1 -> n - 1 <br>
# (len(s)-1)//2: (2n - 2) // 2 = n - 1 <br>
# len(s)//2 + 1: (2n - 1) // 2 + 1 = n <br>

#_ 내적

def solution(a,b):
    resList = [(pair[0] * pair[1]) for pair in zip(a, b)]
    res = sum(resList)
    return res

#_ 부족한 금액 계산하기

def solution(price, money, count):
    totalMoney = 0
    for i in range(1, count+1):
        totalMoney += (price * i)
        res = totalMoney - money
    if res > 0:
        return res
    return 0

# # 다른 풀이 

def solution(price, money, count):

    return max(0, sum([price*i for i in range(1,count+1)]) - money)

#* 금액이 부족하면 양수가 나오고, 금액이 부족하지 않으면 음수가 나오므로,
#! 금액이 부족하지 않으면 음수들을 다 0으로 바꿔야 한다. max(0, x) 사용

#_ 문자열 다루기 기본

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    return False

# # 다른 풀이

def solution(s):
    return s.isdigit() and len(s) in [4,6]


#_ 수박수박수박수박수?

def solution(n):
    
    str = ''
    for i in range(1, n+1):
        if i % 2 != 0:            
            str += '수'
        else:
            str += '박'
        
    return str 

# # 다른 풀이

def solution(n):
    answer = '수박' * (n // 2)
    
    if n % 2 == 1:
        answer = answer + '수'
            
    return answer

# # 다른 풀이

def solution(n):
    return '수박' * (n // 2) + '수' * (n % 2)

#_ 배열의 평균값

def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

#_ 짝수의 합

def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

#_ 각도기

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180: 
        return 3
    elif angle == 180:
        return 4
    

#_ 약수의 개수와 덧셈

def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        cnt = 0
        
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1

        if cnt % 2 == 0:
            sum += i
        else:
            sum -= i
                          
    return sum

# # 다른 풀이

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num ** 0.5 == int(num ** 0.5):
            answer -= num
        else:
            answer += num    
    return answer

#* 약수의 개수가 짝수이면,
#* 13 -> 1 * 13
#* 16 -> 1 * 16

#* 약수의 개수가 홀수이면,
#* 25 -> 1 * 25, 5 * 5
#! 25의 약수는 1, 5, 25, 즉 제곱근의 값이 정수이면 약수의 개수가 홀수

#_ 문자열 내림차순으로 배치하기

#* s = "Zbcdefg"
#* sorted(s, reverse=True) 
#* ['g', 'f', 'e', 'd', 'c', 'b', 'Z'] 내림차순
#! sorted는 리스트로 반환
def solution(s):
    #! ''.join(s) -> 리스트 s를 합쳐서 문자열로 바꿔준다.
    return ''.join(sorted(s, reverse=True)) 
#* 'gfedcbZ'

#! ASCII 코드는 대문자의 값이 소문자의 값보다 작다.
#* 'A' : 65 
#* 'a' : 97 

