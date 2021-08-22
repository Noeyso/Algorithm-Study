## 백준_2153

import string
lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)

word = input()

total=0
for s in word:
    if s.islower():
        total+=(lower_list.index(s)+1)
    else:
        total+=(upper_list.index(s)+27)

def isPrime(num):    
    for i in range(2,num):
        if num%i==0:
            return "It is not a prime word."
    return "It is a prime word."
print(isPrime(total))

##ord를 사용해서 계산하는 방법도 있다!! ord('a')==97
