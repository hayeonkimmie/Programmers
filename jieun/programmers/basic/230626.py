
#_ 홀수 vs 짝수
def solution(num_list):
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
    return max(odd_sum, even_sum)

# # 다른 풀이
def solution(num_list):
    odd_sum = sum(num_list[0::2])
    even_sum = sum(num_list[1::2])
    return max(odd_sum, even_sum)

#_ 배열의 길이에 따라 다른 연산하기
def solution(arr, n):
    if len(arr) % 2 == 1:
        for idx in range(len(arr)):
            if idx % 2 == 0:
                arr[idx] = arr[idx] + n
    else:
        for idx in range(len(arr)):
            if idx % 2 == 1:
                arr[idx] = arr[idx] + n
    return arr

#_ 배열 비교하기
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr2) > len(arr1):
            return -1
        return 1
    elif len(arr1) == len(arr2):
        if sum(arr2) > sum(arr1):
            return -1
        elif sum(arr2) < sum(arr1):
            return 1
        else:
            return 0
        
# # 다른 풀이
def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len (arr1) > len(arr2):
        return 1
    elif sum(arr1) > sum(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1
    else:
        return 0
    
#_ l로 만들기
def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < ord('l'):
            answer += 'l'
        else:
            answer += i
    return answer

# # 다른 풀이
def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)

#_ 세균 증식
def solution(n, t):
    answer = n * 2 **(t) # 초기에 있던 n마리(n)가 시간당 2배씩 증가 (2**t)
    return answer

#_ 가위 바위 보
def solution(rsp):
    answer = ''
    for i in rsp:
        if int(i) == 2:
            answer += '0'
        elif int(i) == 0:
            answer += '5'
        elif int(i) == 5:
            answer += '2'
    return answer

# # 다른 풀이
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(list(d[i] for i in rsp))

# # 다른 풀이
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
