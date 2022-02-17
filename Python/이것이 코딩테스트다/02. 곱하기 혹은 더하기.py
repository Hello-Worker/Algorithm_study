# 0~9로 이루어진 문자열 S가 주어졌을 때, 왼쪽에서 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+'연산자를 넣어 가장 큰 수를 만들어라.
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
# ex) 02984라는 문자열이 주어지면 0+2x9x8x4= 576이 답이다.

S = list(map(int,input()))
result = int(S[0])

for i in range(1,len(S)):
    if S[i] == 0 or S[i] == 1 or result == 0:
        result += int(S[i])
    
    else: 
        result *= int(S[i])

print(result) 
