from math import sqrt  

num=list(range(1,101))
result=""

for i in num:
    if i % sqrt(i)==0:
        result+=str(i)+" "

print("The next doors is opened:\n"+result)
