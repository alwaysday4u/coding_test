'''
https://school.programmers.co.kr/learn/courses/30/lessons/147354
'''

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin-1, row_end):
        s = 0
        for j in data[i]:
            s+=j%(i+1)
        answer^=s
    return answer
