from ctypes.wintypes import WORD


n = int(input())
word = []
cnt = n
for i in range(n):
    word.append(input())

for j in word:
    for k in range(1,len(j)):
        if j[k-1] == j[k]:
            pass
        elif j[k-1] in j[k:]:
            cnt -= 1
            break
print(cnt)



