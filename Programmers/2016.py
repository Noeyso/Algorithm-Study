def solution(a, b):
    weeks=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days=[31,29,31,30,31,30,31,31,30,31,30,31]
    return weeks[(sum(days[:a-1])+b-1)%7]
