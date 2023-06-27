
#_ l로 만들기

def solution(myString):
    answer = ''.join(['l' if ord(s)<ord('l') else s for s in myString])
    return answer

## translate() 이용한 풀이 
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

#_ 5명씩
def solution(names):
    answer = [name for idx,name in enumerate(names) if idx%5==0 ]
    return answer
## 슬라이싱 이용 
def solution(names):
    return names[::5]

#_ 0 떼기
def solution(n_str):
    list_str=list(n_str)
    i=0
    while(i<len(list_str)):
        if list_str[i]=='0':
            del(list_str[i])
            i==0 
            continue
        else:
            break
        i+=1
    return ''.join(list_str)

## lstrip : 문자열의 왼쪽(시작 부분)에서 특정 문자들을 제거하는 메서드
def solution(n_str):
    return n_str.lstrip('0')

#_순서 바꾸기
def solution(num_list, n):
    answer= num_list[n:]+num_list[:n]
    return answer

#_부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''.join([s[parts[idx][0]:parts[idx][1]+1] for idx, s in enumerate(my_strings)])
    return answer

## for i, (s, e) in enumerate(parts)
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer

## zip() 
def solution(my_strings, parts):
    for word, (s, e) in zip(my_strings, parts): answer += word[s : e+1]




