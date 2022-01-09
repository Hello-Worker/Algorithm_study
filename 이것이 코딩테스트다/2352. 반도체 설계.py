n = int(input())
data = list(map(int,input().split()))
result = []

for i in range(1,n+1):
    b = i - int(data[i-1])
    result.append(abs(b))

if result[i+1]-result[i]<0
print(result)
