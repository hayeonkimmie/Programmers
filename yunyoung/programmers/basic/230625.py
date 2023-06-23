
#_ 문자열 겹쳐쓰기 
def solution(my_string, overwrite_string, s):
    return my_string[:s]+overwrite_string+my_string[len(overwrite_string)+s:]

#! next() 사용 
#_ 문자열 섞기 
def solution(str1, str2):
    str_iter1 = iter(str1)
    str_iter2 = iter(str2)
    answer = ''.join([next(str_iter1) if i % 2 == 0 else next(str_iter2) for i in range(len(str1 + str2))])
    return answer

## 다른 풀이 
def solution(str1, str2):
    return ''.join(''.join((a, b)) for a, b in zip(str1,str2))


#_ 두 수의 연산값 비교하기
def solution(a, b):
    answer = int(str(a)+str(b)) if int(str(a)+str(b)) > 2*a*b else 2*a*b
    return answer

## 다른풀이 
#TODO max 사용 
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
def solution(a, b):
    answer = max(int(f'{a}{b}'), 2*a*b)
    return int(answer)

#_ 조건 문자열
def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
        
    answer = eval(f'{n}{ineq+eq}{m}')
    return int(answer)

#_코드 처리하기

