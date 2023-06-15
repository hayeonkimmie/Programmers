#나머지 구하기

def solution(num1, num2):
    answer = num1 % num2
    return answer

# 두 수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer

# 몫 구하기
def solution(num1, num2):
    answer = num1//num2
    return answer

# 두 수의 곱
def solution(num1, num2):
    answer = num1*num2
    return answer

# 나이 출력
def solution(age):
    answer = 2023-age 
    return answer

# 숫자 비교하기
def solution(num1, num2):
    return 1 if num1 == num2 else -1 

# 두 수의 합
def solution(num1, num2):
    answer = num1+num2
    return answer

# 두 수의 나눗셈
def solution(num1, num2):
    answer = int((num1 / num2)*1000)
    return answer

# 각도기
def solution(angle):
    answer = 1 if angle < 90  else 2 if angle == 90 else 3 if angle <180 else 4
        
    return answer

# 짝수의 합
def solution(n):
    answer = sum([ i for i in range(2,n+1,2)])
    return answer

# 배열의 평균값
def solution(numbers):
    answer = sum(numbers)/len(numbers)
    return answer

# 양꼬치
def solution(n, k):
    answer = n*12000 + (k-(n//10))*2000
    return answer

# 자릿수 더하기
def solution(n):
    if n/10 == 0:
         return 0
    else:
         return n%10 + solution(n//10)
    

# 평균 구하기
def avg(arr):
     return sum(arr)/len(arr)


# 약수의 합 
def divisor(num):
     sum=0
     for i in range(1,num+1):
          if num%i==0:
               sum+=i         
     return sum  

# print(divisor(12))


#나머지가 1이 되는 수 찾기
def min_num(num):
     for i in range(2,num):
          if (num-1) % i ==0:
               return i
          

# x만큼 간격이 있는 n개의 숫자
def interval(n,cnt):
     return [i*n for i in range(1,abs(cnt)+1)]

# 문자열 내 p와 y의 개수
def searchPY(s):
     # return s.lower().count('p') == s.lower().count('y')
     return s.count('p')+s.count('P') ==  s.count('y')+s.count('Y')


#자연수 뒤집어 배열로 만들기
def reverseList(num):
     #  return list(map(int, reversed(str(n))))]
     return [int(i) for i in str(num)[::-1]]


# 정수 제곱근 판별

"""
틀린 답안 

정확성: 94.4 , 합계: 94.4 / 100.0
def solution(n):
     i=1
     while (n//i>=i):
          if i == n//i:
              return (i+1)**2     
          i+=1
    
     return -1
         
"""


def solution(n):
     i=1
     while (n//i>=i):
          if n == i**2:
              return (i+1)**2     
          i+=1
    
     return -1
         

def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'


# 문자열을 정수로 바꾸기
def solution(n):
    return int(n)

# 정수 내림차순으로 배치하기
"""
참고 풀이

ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

"""

def solution(n):
     num_list =  list(map(int, str(n)))
     for i in range(len(num_list)):
          for j in range(i,len(num_list)):
               if num_list[i]<num_list[j]:
                    tmp=num_list[i]
                    num_list[i]=num_list[j]
                    num_list[j]=tmp

     result = int(''.join(map(str, num_list)))

     return result



# 하샤드 수
"""
참고 풀이 

def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0

"""
def solution(x):
    nums = list(map(int, str(x)))
    return x%sum(nums) == 0 

# 두 정수 사이의 합
def solution(a, b):
    return sum(n for n in range(min(a,b), max(a,b)+1))
# print(sum(range(min(7,10), max(7,10)+1)))


# 콜라츠 추측
"""
참고 풀이
def collatz(num):
    for i in range(501):
        if num == 1:
            return i
        num = num/2 if num%2==0 else num*3+1
    return -1

"""

def solution(num):
     cnt = 0 
     while(num!=1 and cnt <500):
          cnt+=1
          if num%2==0:
            num //= 2
          else:
            num = num*3+1
            print(num)
            
     if cnt == 500:
          cnt = -1
     
     return cnt

# 김서방 찾기
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'


# 나누어 떨어지는 숫자 배열
"""
참고 풀이 

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


"""
def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    
    if len(answer) > 0:
        answer.sort()
    else:
        answer.append(-1)
        
    return answer
        

# 핸드폰 번호 가리기
def solution(phone_number):
    return len(phone_number[:-4])*'*'+phone_number[-4:]

# print(''.join(map(lambda x : '*',phone_number[:-4]))+phone_number[-4:])


#음양 더하기
"""
참고 답안 

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
"""

def solution(absolutes, signs):
    answer = [num if signs[idx] else -1*num for idx, num in enumerate(absolutes)]

    return sum(answer)



# 없는 숫자 더하기
"""
참고 풀이 

def solution(numbers):
    return 45 - sum(numbers)

def solution(numbers):
    return sum(set(range(10)) - set(numbers))

"""
def solution(numbers):
    totals={0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sum(totals-set(numbers))


# 문자열을 정수로 변환하기
def solution(n_str):
    return int(n_str)


#! -------------220518----------------
#* level 0 

# 공배수

def solution(number, n, m):
    
    return 1 if (number % n == 0 and number % m ==0) else 0


