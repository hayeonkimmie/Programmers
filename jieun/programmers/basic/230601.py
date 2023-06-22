
#_ 길이에 따른 연산
from functools import reduce
def multiply(x,y):
    return x * y
def add(x,y):
    return x + y
def solution(num_list):
    return reduce(multiply, num_list) if len(num_list) <= 10 else reduce(sum, num_list)

#* reduce 함수는 반복 가능한 객체이다.
#* 각 요소들을 이전 연산 결과들과 누적하여 반환
#! reduce 코드는 일부 테스트에서 런타임 에러남

# # 다른 풀이 
def solution(num_list):
    ans = 1
    if len(num_list) <= 10:
        for i in num_list:
            ans *= i
        return ans
    return sum(num_list)

#_ 원소들의 곱과 합
def solution(num_list):
    ans = 1
    for i in num_list:
        ans *= i
    return 1 if pow(sum(num_list), 2) > ans else 0  

#_ 문자 리스트를 문자열로 변환하기
def solution(arr):
    return ''.join(arr)

#_ 정수 부분
def solution(flo):
    return int(flo)

#_ 소문자로 바꾸기
def solution(myString):
    return myString.lower()

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

#_ 배열 두배 만들기
def solution(numbers):
    return [i * 2 for i in numbers]

#_ 피자 나눠 먹기(1)
def solution(n):
    return (n // 7) + 1 if n % 7 != 0 else n // 7

#_ 배열 뒤집기
def solution(num_list):    
    return num_list[::-1]

# # 다른 풀이 
def solution(num_list):
    return list(reversed(num_list))

#_ 문자열의 뒤의 n글자
def solution(my_string, n):
    return my_string[-n:]

#_ 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1 : num2+1]

#_ n번째 원소까지
def solution(num_list, n):
    return num_list[0 : n]

#_ 삼각형의 완성조건(1)
def solution(sides):
    return 1 if max(sides) < sum(sides) - max(sides) else 2

#_ 문자열 뒤집기
def solution(my_string):
    return my_string[::-1]

#_ 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

#_ 피자 나눠 먹기(3)
def solution(slice, n):
    return (n // slice) + 1 if n % slice != 0 else (n / slice) 

#_ 배열 원소의 길이
def solution(strlist):
    return [len(strlist[i]) for i in range(len(strlist))]

#_ 최댓값 만들기(1)
def solution(numbers):
    numbers = sorted(numbers)
    return numbers[-1] * numbers[-2]

#_ 중복된 숫자 개수
def solution(array, n):
    return array.count(n)

#_ 점의 위치 구하기
def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    return 4

#_ 중앙값 구하기
def solution(array):
    array = sorted(array)
    if len(array) % 2 == 1:
        return array[len(array) // 2]

#_ 순서쌍의 개수
def solution(n):
    cnt = 0
    for i in range(1, n + 1 // 2):
        if n % i == 0:
            cnt += 1
    return cnt + 1

#* 두 숫자의 곱으로 표현되는 것은 두 숫자중 한 숫자로 나눴을때 나머지가 0 
#* 홀짝수 무관하게 마지막은 n * 1이므로, for문은 n의 절반까지만 돌려줌

#_ 짝수 홀수 개수
def solution(num_list):
    return [len([i for i in num_list if i % 2 == 0]), len([i for i in num_list if i % 2 == 1])]

# # 다른 풀이 
def solution(num_list):
    res = len([i for i in num_list if i % 2 == 0])
    return [res, len(num_list) - res]

#_ 모음 제거
import re
def solution(my_string):
    return re.sub("['a','i','o','e','u']", '', my_string)

#_ 문자열 정수의 합
def solution(num_str):
    return sum([int(i) for i in num_str])

#_ 아이스 아메리카노
def solution(money):   
    return [money // 5500, money % 5500]

#_ 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        price *= 0.8
    elif 300000 <= price < 500000:
        price *= 0.9
    elif 100000 <= price < 300000:
        price *= 0.95
    return int(price)

# # 다른 풀이 
def solution(price):
    list_discount = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    
    for discount_price, discount_rate in list_discount.items():
        if price >= discount_price:
            return int(price * discount_rate)

#_ 머쓱이보다 키 큰 사람
def solution(array, height):
    return len([i for i in array if i > height])

# # 다른 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse = True)
    return array.index(height)

#_ 배열의 유사도
def solution(s1, s2):
    return len([i for i in s1 if i in s2])

# # 다른 풀이
def solution(s1, s2):
    return len(set(s1) & set(s2))

#_ 부분 문자열인지 확인하기
def solution(my_string, target):
    return 1 if target in my_string else 0

#_ rny_string
def solution(rny_string):
    return rny_string.replace('m', 'rn')

#_ 카운트 업
def solution(start, end):
    return [i for i in range(start, end + 1)]

#_ 자릿수 더하기
def solution(n):
    return sum([int(i) for i in str(n)])

#_ n보다 커질 때 까지 더하기
def solution(numbers, n):
    sum = 0
    for i in numbers:
        if sum > n: continue
        sum += i
    return sum

#_ 숨어있는 숫자의 덧셈
import re
def solution(my_string):
    pattern = re.findall(r'\d', my_string)
    return sum([int(i) for i in pattern])

#_ 문자 반복 출력하기
def solution(my_string, n):
    str = ''
    return ''.join([i * n for i in my_string])

#_ 카운트 다운
def solution(start, end):
    return [i for i in range(start, end - 1, -1)]
