def solution(numbers, hand):
    answer = ''

    keypad = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    lx,ly=0,3
    rx,ry=2,3
    
    res=""
    for num in numbers:
        if num in keypad[0]:
            res+="L"
            lx,ly=0,keypad[0].index(num)
        elif num in keypad[2]:
            res+="R"
            rx,ry=0,keypad[2].index(num)
        else:
            tmp_x=1
            tmp_y=keypad[1].index(num)
            dist_l = abs(tmp_x-lx)+abs(tmp_y-ly)
            dist_r = abs(tmp_x-rx)+abs(tmp_y-ry)
            if dist_l==dist_r:
                if hand=='right':
                    res+="R"
                    rx,ry=tmp_x,tmp_y
                else:
                    res+="L"
                    lx,ly=tmp_x,tmp_y
            elif dist_l>dist_r:
                res+="R"
                rx,ry=tmp_x,tmp_y
            else:
                res+="L"
                lx,ly=tmp_x,tmp_y
    return res
