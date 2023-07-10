#_ 나머지 구하기
def solution(num1, num2):
    answer = num1%num2
    return answer
solution(10, 5) 

#_ 두 수의 곱
def solution(num1, num2):
    return num1 * num2

solution(3,4)

#_ 두 수의 나눗셈
def solution(num1, num2):
    return int((num1 / num2) * 1000)
print(solution(3,2))

#_ 두 수의 차
def solution(num1, num2):
    return num1 - num2

print(solution(3,2))

#_ 짝수의 합
def solution(n):
    evens=[]
    for i in range(n+1):
        if i % 2 == 0:
            evens = evens.append(i)
        for j in evens:
            sum(j)          


#_ 몫 구하기
def solution(num1, num2):
    return num1 // num2

solution(10,5)

#_ 문자열 뒤집기
def solution(my_string):
    for i in my_string[::-1]:
        return i
    
solution('jaron')

#_ 배열의 평균 값
def solution(numbers):
    return sum(numbers)/len(numbers)

solution([2, 4, 5])

#_ 숫자 비교하기
def solution(num1, num2):
    if num1 == num2 :
        return 1
    else:
        return -1
    
solution(3,3)



#_ 각도기
def solution(angle):
    if 0 < angle < 90:
        return 1
    if angle == 90:
        return 2
    if 90 < angle < 180 :
        return 3
    if angle == 180:
        return 4

solution(70)

#_ 나이 출력
def solution(age):
    answer = 2022 - age + 1
    
    return answer
print(solution(40))

#TODO 문제 다시 풀이하기 
#_ 양꼬치 
def solution(n, k):
    yang = 12000
    bev = 2000
    if 10 <= n < 20:
        return (yang * n) + (bev * (k-1))
    elif 20 <= n < 30:
        return (yang * n) + (bev * (k-2))
    elif 30 <= n < 40:
        return (yang * n) + (bev * (k-3))
    elif 40 <= n < 50:
        return (yang * n) + (bev * (k-4))
    elif 50 <= n < 60:
        return (yang * n) + (bev * (k-5))
    elif 60 <= n < 70:
        return (yang * n) + (bev * (k-6))
    elif 70 <= n < 80:
        return (yang * n) + (bev * (k-7))
    