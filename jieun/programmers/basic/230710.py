
#_ 5명씩
def solution(names):
    return names[0::5]

# # 다른 풀이
def solution(names):
    return [names[idx] for idx in range(len(names)) if idx % 5 == 0]

#_ 대문자와 소문자
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])

# # 다른 풀이
def solution(my_string):
    return my_string.swapcase()


#_ 부분 문자열 이어 붙어 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for idx in range(len(parts)):
        answer += my_strings[idx][parts[idx][0]:parts[idx][1] + 1]
    return answer

# # 다른 풀이
def solution(my_strings, parts):
    answer = ''
    for idx, (start, end) in enumerate(parts):
        answer += my_strings[idx][start:end + 1]
    return answer

#_ 순서 바꾸기
def solution(num_list, n):
    answer = num_list[n:] + num_list[:n]
    return answer

#_ 0떼기
def solution(n_str):
    return str(int(n_str))

#_ 행렬의 덧셈
def solution(arr1, arr2):
    for idx_row in range(len(arr1)):
        for idx_col in range(len(arr1[0])):
            arr1[idx_row][idx_col] += arr2[idx_row][idx_col]
    return arr1

#_ 최댓값과 최솟값
def solution(s):
    tmp = list(map(int, s.split()))
    return ' '.join([str(min(tmp)), str(max(tmp))])

# # 다른 풀이
def solution(s):
    mylist = list(map(int, s.split(' ')))
    return str(min(mylist)) + ' ' + str(max(mylist))

#_ JadenCase 문자열 만들기
#! 정확성 44.4 / 100.0
def solution(s):
    answer = []
    for idx in range(len(s.split())):
        answer.append(s.split()[idx].capitalize())
    return ' '.join(answer)

# # 다른 풀이
def solution(s):
    mylist = []
    s = s.split(' ')
    for word in s:
        if word:
            mylist.append(word[0].upper() + word[1:].lower())
        else:
            mylist.append(word)
    return ' '.join(mylist)

#_ 최대공약수와 최소공배수
#* A, B의 최소공배수를 구하고자 할 때 
#* A = a(미지수) x G(최대공약수) 
#* B = b(미지수) x G(최대공약수) 
#* 최소공배수 L = a x b x G
#* A x B = a x b x G x G = L x G 
#* L = A x B // G
from math import gcd
def solution(n, m):
    g = gcd(n, m)
    l = (n * m) // g
    return [g, l]

# # 다른 풀이
#* 유클리드 호제법
def solution(n, m):
    gcd = lambda a, b : b if not a % b else gcd(b, a % b)
    lcm = lambda a, b : a * b // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]