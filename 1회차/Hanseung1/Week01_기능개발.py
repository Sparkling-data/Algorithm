"""
- 코딩테스트 연습 - 스택/큐 - 기능개발
- URL: https://programmers.co.kr/learn/courses/30/lessons/42586

- 문제해석
기능별 개발 속도가 다르고, 뒤에 기능이 먼저 개발되도 앞에 기능이 배포될 때
같이 배포되기 때문에 QUEUE 접근
"""
pro1 = [93, 30, 55]
spd1 = [1, 30, 5]

pro2 = [95, 90, 99, 99, 80, 99]
spd2 = [1, 1, 1, 1, 1, 1]

def solution3(progresses, speeds):
    answer = [] # 결과값 리스트 선언

    while progresses:
        cnt = 0     # 카운트 변수 선언
        progresses = [x+y for x,y in zip(progresses, speeds)] # 진행상황에 속도 더함

        while progresses:
            if progresses[0] >= 100:    # 첫 idx가 진행상황 100 넘길때
                cnt += 1                # 갯수를 더하고
                progresses.pop(0)       # pop으로 추출
                speeds.pop(0)
            elif cnt > 0:               # idx 0이 100이 안넘고 갯수가 있는 경우 append
                answer.append(cnt)      
                break
            else:                       # idx 0이 100을 안넘고 갯수도 없는 경우 loop문 나옴
                break
            
    answer.append(cnt)                  # loop문 종료 후, 마지막 cnt는 진행중인 프로그램이 없어서
                                        # 하지못한 append를 마지막으로 실행
    return answer

print(solution3(pro1,spd1)) # [2,1]
print(solution3(pro2,spd2)) # [1,3,2]
