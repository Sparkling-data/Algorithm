
def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    sum = 0

    for v in range(0, a-1):
        sum += month[v]

    total_d = sum + b

    answer = ''
    answer += (day[(total_d % 7)-1])

    return answer


if __name__ == "__main__":
    solution(5, 24)