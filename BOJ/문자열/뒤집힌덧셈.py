## 백준_1357

x,y = map(int,input().split())


def Rev(num):
    n = str(num)
    total=0
    g=1
    for i in n:
        int(i)
        total+=int(i)*g
        g*=10
    return total
print(Rev(Rev(x)+Rev(y)))


'''
## 다른 풀이 
x,y = map(str,input().split())
s = str(int(x[::-1])+int(y[::-1]))
print(int(s[::-1]))
'''
