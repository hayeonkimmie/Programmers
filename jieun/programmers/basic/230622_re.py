
#_ 두 수의 차
def solution(num1, num2):
    return num1 - num2

#_ 나머지 구하기
def solution(num1, num2):
    return num1 % num2

#_ 두 수의 곱
def solution(num1, num2):
    return num1 * num2

#_ 몫 구하기
def solution(num1, num2):
    return num1 // num2

#_ 숫자 비교하기
#* A if 조건1 else B 
def solution(num1, num2):
    return 1 if num1 == num2 else -1

#_ 나이 출력
def solution(age):
    return 2022 - age + 1

#_ 두 수의 합
def solution(num1, num2):
    return num1 + num2

#_ 두 수의 나눗셈
def solution(num1, num2):
    return int(num1 / num2 * 1000)

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

# # 다른 풀이
def solution(angle):
    answer = 1 if angle < 90 else 2 if angle == 90 else 3 if angle < 180 else 4
    return answer
    
#_ 짝수의 합
def solution(n):
    return sum([i for i in range(n + 1) if i % 2 == 0])

#_ 배열의 평균값
def solution(numbers):
    return sum(numbers) / len(numbers)

#_ 양꼬치
def solution(n, k):
    return n * 12000 + k * 2000 - (n // 10 * 2000)

# # 다른 풀이
def solution(n, k):
    return n * 12000 + (k - (n // 10)) * 2000

#_ 배열 뒤집기
def solution(num_list):
    return num_list[::-1]

#_ 피자 나눠 먹기(1)
def solution(n):
    return n // 7 + 1 if n % 7 != 0 else n // 7

#_ 배열 원소의 길이
def solution(strlist):
    return[len(i) for i in strlist]

# # 다른 풀이
def solution(strlist):
    answer = list(map(lambda x:len(x), strlist))
    return answer

#_ 편지
def solution(message):
    return len(message) * 2

#_ 아이스 아메리카노
def solution(money):
    return [money // 5500, money % 5500]

#_ 짝수 홀수 개수
def solution(num_list):
    res = len([i for i in num_list if i % 2 == 0])
    return [res, len(num_list) - res]

#_ 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    return 4

# # 다른 풀이
#* 2차원 배열 [[0,0],[0,1],[1,0],[1,1]]
#* [([x < 0, y < 0], [x < 0, y > 0]), ([x > 0, y < 0], [x > 0, y > 0])]
#* dot = [2, 4] -> solution(dot) -> quad[True][True] = quad[1][1] 
#* dot = [-2, 4] -> solution(dot) -> quad[False][True] = quad[0][1] 
#* dot = [-3, -2] -> solution(dot) -> quad[False][False] = quad[0][0]
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

#_ 삼각형의 완성 조건(1)
def solution(sides):
    return 1 if max(sides) < sum(sides) - max(sides) else 2

#_ 피자 나눠 먹기(3)
def solution(slice ,n):
    return n // slice + 1 if n % slice != 0 else n // slice
    
#_ 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter, '')

#_ 중복된 숫자 개수
def solution(array, n):
    return array.count(n)

#_ 중앙값 구하기
#* sorted()는 새로운 정렬된 목록을 반환하며, 원래 목록은 영향 받지 않는다.
#* list.sort()는 list를 그 자리에서 정렬하고 목록 인덱스를 변경하고 None을 반환한다.
#* list를 변경하려면 list.sort()를 사용하고, 새로운 정렬된 객체를 원하면 sorted()를 사용한다.
#* list.sort()는 복사본을 만들 필요가 없으므로 sorted()보다 빠르다.
def solution(array):
    array = sorted(array)
    return array[len(array) // 2]

#_ 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1 : num2 +1]

#_ 모음 제거
import re
def solution(my_string):
    return re.sub("['a','i','o','e','u']", '', my_string)

# # 다른 풀이
def solution(my_string):
    return ''.join([i for i in my_string if not (i in 'aeiou')])

#_ 머쓱이보다 키 큰 사람
def solution(array, height):
    return len([i for i in array if i > height])

#_ 배열의 유사도
def solution(s1, s2):
    return len([i for i in s1 if i in s2])

# # 다른 풀이
def solution(s1, s2):
    return len(set(s1).intersection(set(s2)))

# # 다른 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2));

#_ 문자 반복 출력하기
#* '구분자'.join(리스트)
#* join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수
#* ''는 공백
def solution(my_string, n):
    return ''.join([i * n for i in my_string])

#_ 소문자로 바꾸기
def solution(my_string):
    return my_string.lower()

#_ 공배수
def solution(number, n, m):
    return 1 if (number % n == 0) and (number % m == 0) else 0

#_ 길이에 따른 연산
def solution(num_list):
    ans = 1
    if len(num_list) <= 10:
        for i in num_list:
            ans *= i
        return ans
    return sum(num_list)

# # 다른 풀이
#* math.prod 주어진 iterable에 대해서 모든 elements에 대해서 곱셈을 계산해서 반환하는 함수
import math
def solution(num_list):
    return math.prod(num_list) if len(num_list) <= 10 else sum(num_list)
    
#_ 순서쌍의 개수
#* 두 숫자의 곱으로 표현되는 것은 두 숫자중 한 숫자로 나눴을때 나머지가 0 
#* 홀짝수 무관하게 마지막은 n * 1이므로, for문은 n의 절반까지만 돌려줘도 된다.
def solution(n):
    cnt = 0
    for i in range(1, n + 1 // 2):
        if n % i == 0:
            cnt += 1
    return cnt + 1

# # 다른 풀이
#* list.append(x)는 리스트 끝에 x 1개를 그 자체 그대로 추가한다.
#* list.extend(x)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 추가한다.

#! y가 리스트 형인 경우
#* x = ['a', 'b', 'c', 'd', 'e']
#* y = ['ping', 'pong']
#* x.append(y)는 ['a', 'b', 'c', 'd', 'e', ['ping', 'pong']]
#* x.extend(y)는 ['a', 'b', 'c', 'd', 'e', 'ping', 'pong']

#! y가 문자열 형인 경우
#* x = ['a', 'b', 'c', 'd', 'e']
#* y = 'ping'
#* x.append(y)는 ['a', 'b', 'c', 'd', 'e', 'ping']
#* x.extend(y)는 ['a', 'b', 'c', 'd', 'e', 'p', i', 'n', 'g']

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.extend([(i, n // i)])
    return len(answer)

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append((i, n // i))
    return answer

# # 다른 풀이
#* filter(function, iterator), filter(필터링을 적용시킬 함수, 반복 가능한 값)
#* filter 함수는 iterator에 들어온 값들을 하나 하나 function에 넣어서 true인 값을 필터링해서 다시 리스트로 반환하는 함수
#* filter 함수의 반환 값은 객체이므로 반드시 리스트로 형 변환 해야한다. list(filter(function, iterator))
def solution(n):
    return len(list(filter(lambda v : n % (v) == 0, range(1, n + 1))))

#_ 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        price *= 0.8
    elif 300000 <= price < 500000:
        price *= 0.9
    elif 100000 <= price < 300000:
        price *= 0.95
    return int(price)

#_ 대문자로 바꾸기
def solution(myString):
    return myString.upper()

#_ 배열 두배 만들기
def solution(numbers):
    return [i * 2 for i in numbers]

#_ 정수 부분
def solution(flo):
    return int(flo)

#_ 조건에 맞게 수열 반환하기 1
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

#_ 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list

#_ 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

#_ 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)

#_ 자릿수 더하기
def solution(n):
    return sum([int(n) for i in n])

#_ 문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]

#_ 조건에 맞게 수열 변환하기 3
def solution(arr, k):
    answer = []
    for idx in range(len(arr)):
        if k % 2 == 1:
            answer.append(arr[idx] * k)
        else:
            answer.append(arr[idx] + k)
    return answer

#_ 수 조작하기 1
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

# # 다른 풀이
def solution(n, control):
    key = dict((zip(['w','s','d','a'], [1, -1, 10, -10])))
    return n + sum([key[c] for c in control])

#_ n 번째 원소까지
def solution(num_list, n):
    return num_list[0 : n]

#_ 카운트 업
def solution(start, end):
    return [i for i in range(start, end + 1)]

#_ n 번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

#_ 숨어있는 숫자의 덧셈(1)
import re
def solution(my_string):
    pattern = re.findall(r'\d', my_string)
    return sum([int(i) for i in pattern])

#_ 문자열로 반환
def solution(n):
    return str(n)

#_ 정수 찾기
def solution(num_list, n):
    return 1 if n in num_list else 0

#_ 원소들의 곱과 합
def solution(num_list):
    ans = 1
    for i in num_list:
        ans *= i
    return 1 if pow(sum(num_list), 2) > ans else 0

# # 다른 풀이
#* eval(expression), 매개변수로 받은 expression(=식)을 문자열로 받아서 실행하는 함수
#* eval('1+2')는 출력값으로 3을 반환
def solution(num_list):
    s = sum(num_list) ** 2
    m = eval('*'.join([str(n)for n in num_list]))
    return 1 if s > m else 0

#_ 문자 리스트를 문자열로 반환하기
def solution(arr):
    return ''.join(arr)

#_ flag에 따라 다른 값 반환하기
def solution(a, b, flag):
    return a + b if flag else a - b

#_ 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str1 + str2)

#_ n보다 커질때까지 더하기
def solution(numbers, n):
    sum = 0
    for i in numbers:
        if sum > n: continue
        sum += i
    return sum

# # 다른 풀이
#* iterable = 반복가능한
#* 이터레이터(iterator)는 next 함수 호출 시 계속 다음 값을 리턴하는 객체
#* next() : iterator에서 반복자를 입력받아 다음 출력값을 반환하는 함수
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)

#_ 첫 번째로 나오는 음수
def solution(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] < 0: return idx
    return -1

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

#_ 홀짝 구분하기
n = int(input())
if n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')
    
#_ 부분 문자열 인지 확인하기
def solution(my_string, target):
    return 1 if target in my_string else 0

#_ 카운트 다운
#* range(시작 숫자, 종료 숫자, step)
def solution(start, end):
    return [i for i in range(start, end - 1, -1)]

#_ 짝수는 싫어요
def solution(n):
    return [i for i in range(1, n+1) if i % 2 == 1]

#_ 접두사인지 확인하기
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0

# # 다른 사람 풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
    
#_ 문자열 곱하기
def solution(my_string, k):
   return my_string * k

#_ A 강조하기
def solution(myString):
    answer = myString.lower().replace('a', 'A')     
    return answer

#_ rny_string
def solution(rny_string):
    return rny_string.replace('m', 'rn')

#_ 공백으로 구분하기
def solution(my_string):
    return [i for i in my_string.split()]

#_ 문자열 정수의 합
def solution(num_str):
    return sum([int(i) for i in num_str])

#_ 원하는 문자열 찾기
def solution(myString, pat):
    if pat.lower() in myString.lower(): 
        return 1 
    return 0

#_ 주사위 게임 1
def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)
    
#_ 문자열 안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

#_ n개 간격의 원소들
def solution(num_list, n): 
    return [num_list[i] for i in range(0, len(num_list), n)]

#_ 배열 만들기
def solution(n, k):
    return [k * (i + 1) for i in range(n // k)]

#_ 특정한 문자를 대문자로 바꾸기
def solution(my_string, alp):
    try:
        if alp in my_string:
            res = my_string.replace(alp, alp.upper())
        return res
    except:
        return my_string
    
# # 다른 풀이
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

#_ 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    return  [word.lower() if idx % 2 == 0 else word.upper() for idx, word in enumerate(strArr)]

#_ 뒤에서 5등 위로
def solution(num_list):
    return sorted(num_list)[5:]

#_ 꼬리 문자열
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex in i:
            pass
        else:
            answer += i
    return answer 

# # 다른 풀이
def solution(str_list, ex):
    sentence = str("".join([s for s in str_list if ex not in s]))
    return sentence

#_ 부분 문자열
def solution(str1, str2):
    if str1 in str2: 
        return 1
    return 0

#_ 접미사인지 확인하기
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

#_ 제곱수 판별하기
import numpy as np 
def solution(n):
    if int(np.sqrt(n)) ** 2 == n:
        return 1
    return 2

# # 다른 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

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

#_ 개미 군단
def solution(hp):
    res = hp // 5
    res2 = (hp - (res * 5)) // 3
    res3 = (hp - (res * 5) - (res2 * 3))
    return res + res2 + res3

# # 다른 풀이
def solution(hp):
    return hp // 5 + (hp % 5) //3 + (hp % 5) % 3

#_ 암호 해독
def solution(cipher, code):
    return ''.join(list(cipher)[code -1::code])

#_ 공백으로 구분하기 2
def solution(my_string):
    return my_string.split()

#_ 뒤에서 5등까지
def solution(num_list):
    return sorted(num_list)[:5]

#_ 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')

#_ 약수의 합
def solution(n):    
    return sum([Divisor for Divisor in range(1, n+1) if (n / Divisor).is_integer()])

#_ 짝수와 홀수
def solution(num):
    result = 'Even' if num % 2 == 0  else 'Odd'
    return result

#_ 자릿수 더하기
def solution(n):    
    return sum(map(int, list(str(n))))

#_ x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x * idx for idx in range(1, n + 1)]

#_ 나머지가 1이 되는 수 찾기
def solution(n):
    return [Divisor for Divisor in range(1, n+1) if n % Divisor == 1][0]

#_ 문자열 섞기
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += (str1[i] + str2[i])
    return answer

#_ 문자열 내 p와 y의 개수
def solution(s):    
    s = s.lower()
    return True if s.count('p') == s.count('y') else False

#_ 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = list(map(int,list(str(n))))
    return answer[::-1]

# # 다른 풀이
def solution(n):
    return list(map(int, reversed(str(n))))

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

#_ 문자열 돌리기
str = input()
for i in str:
    print(i)
    
#_ 하샤드 수
def solution(x):
    val = sum(list(map(int, list(str(x)))))
    if x % val == 0:
        return True
    return False

#_ 두 수의 연산값 비교하기
def solution(a, b):
    cond1 = int(str(a) + str(b))
    cond2 = 2 * a * b
    return max(cond1, cond2)

#_ 두 정수 사이의 합
def solution(a, b):
    sum = 0
    for i in range(min(a, b), max(a, b) + 1):
        sum += i
    return sum

# # 다른 풀이
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2

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

#_ 서울에서 김서방 찾기
def solution(seoul):
    return '김서방은 ' + str(seoul.index('Kim')) + '에 있다'

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

#_ 핸드폰 번호 가리기
def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer

#_ 없는 숫자 더하기
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

#_ 제일 작은 수 제거 하기
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
    
def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

#_ 가운데 글자 가져오기
def solution(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    
# # 다른 풀이 
#* 짝수 2n -> n - 1, n <br>
#* (len(s)-1)//2: (2n - 1) // 2 = n - 1 <br>
#* len(s)//2 + 1: (2n // 2) + 1 = n + 1 <br>

#* 홀수 2n - 1 -> n - 1 <br>
#* (len(s)-1)//2: (2n - 2) // 2 = n - 1 <br>
#* len(s)//2 + 1: (2n - 1) // 2 + 1 = n <br>
def solution(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]
    
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
#* 금액이 부족하면 양수가 나오고, 금액이 부족하지 않으면 음수가 나오므로,
#! 금액이 부족하지 않으면 음수들을 다 0으로 바꿔야 한다. max(0, x) 사용
def solution(price, money, count):
    return max(0, sum([price*i for i in range(1,count+1)]) - money)

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
#* 약수의 개수가 짝수이면,
#* 13 -> 1 * 13
#* 16 -> 1 * 16

#* 약수의 개수가 홀수이면,
#* 25 -> 1 * 25, 5 * 5
#! 25의 약수는 1, 5, 25, 즉 제곱근의 값이 정수이면 약수의 개수가 홀수
def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num ** 0.5 == int(num ** 0.5):
            answer -= num
        else:
            answer += num    
    return answer

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

#_ 특수문자 출력하기
print("!@#$%^&*(\\'\"<>?:;")

#_ a와 b 출력하기
a, b = map(int, input().strip().split(' '))
print(f'a = {a}')
print(f'b = {b}')

#_ 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    return my_string[:s] + my_string[s:s+len(overwrite_string)].replace(my_string[s:s+len(overwrite_string)], overwrite_string) + my_string[s+len(overwrite_string):]

#_ 대소문자 바꿔서 출력하기
#* swapcase() : 대소문자 상호 전환 메서드
str = input()
print(str.swapcase())

#_ 문자열 출력하기
str = input()
print(str)

