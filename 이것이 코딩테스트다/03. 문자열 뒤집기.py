S = list(input())
zero = 0
one = 0
for i in range(len(S)-1): #마지막 자리는 필요없음
    if S[i] == '0': # 첫번째자리가 0이면
        zero += 1 # 0덩어리 1증가
    if S[i] != S[i+1]:
        if S[i+1] == '0':
            zero += 1
        else:
            one += 1

print(min(zero,one))



#s = input()
#a = []
#for i in range(len(s) - 1):
#    if s[i + 1] != s[i]:
#        a.append(s[i])
#a.append(s[-1])

#print(min(a.count('1'), a.count('0')))
