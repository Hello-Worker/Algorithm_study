# 4-3) 1110번: 더하기 사이클

num = int(input())
answer = num #초기 입력받은 값을 answer에 저장.
cnt = 0

while True:
    ten = num//10 # 목의 기호. 10의자리수. 68에서 6
    one = num%10 # 나머지 기호. 68을 입력받았을 시 나머지인 8(오른쪽 자리 수)
    num = ((ten + one)%10)+one*10 # (6+8)%10+8*10 = 84
    cnt += 1 # 사이클 횟수
    if num == answer: # num = 초기값
        break
print(cnt)

