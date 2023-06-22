
#_ 조건 문자열
def solution(ineq, eq, n, m):
    if eq == '!':
        answer = eval(str(n) + ineq + str(m))
    else:
        answer = eval(str(n) + ineq + eq + str(m))
    return answer * 1

# # 다른 풀이
def solution(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))

# # 다른 풀이
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1
    return answer

#_ 문자열 바꿔서 찾기
def solution(myString, pat):
    table = myString.maketrans({'A':'B', 'B':'A'})
    value = myString.translate(table)
    return 1 if pat in value else 0

# # 다른 풀이
def solution(myString, pat):
    tmp = ''
    for word in myString:
        if word == "A":
            word = "B"
        else:
            word = "A"
        
        tmp += word
    # tmp.find(pat) >= 0 : tmp 안에 pat이 존재한다.
    # tmp.find(pat) != -1 : tmp 안에 pat이 없지 않다면
    return int(tmp.find(pat) >= 0)

# # 다른 풀이
def solution(myString, pat): 
    tmp = ''.join(["B" if i == "A" else "A" for i in myString])   
    return int(pat in tmp)

#_ 배열의 원소 만큼 추가하기
def solution(arr):
    answer = []
    for num in arr:
        for _ in range(num):
            answer.append(num)
    return answer

# # 다른 풀이
def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer

