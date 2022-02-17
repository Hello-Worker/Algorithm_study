n = list(map(str, input()))
answer = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in n:
    for j in range(len(dial)):
        if i in dial[j]:
            answer += j+3

print(answer)