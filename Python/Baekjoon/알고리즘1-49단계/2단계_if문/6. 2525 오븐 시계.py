n = list(map(int, input().split()))
m = int(input())
n[1]+=m

if n[1] >= 60:
    n[0] += n[1] // 60
    n[1] = n[1] % 60
    
elif n[1] < 60:
    pass

if n[0] >= 24:
    n[0] = n[0] % 24
    
print(n[0],n[1])