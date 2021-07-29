# 0과 1로만 이루어진 문자열S
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
# S에 있는 모든 숫자 전부 같게 만들기
# 최소 횟수 출력
# 적은 숫자의 


S = [0,0,0,1,1,0,0]

cnt_0 = 0 # 전부 0으로 바꾸는 횟수
cnt_1 = 0 # 전부 1로 바꾸는 횟수

if S[0] == 0:
    cnt_1 = 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            if S[i] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1

else:
    cnt_0 = 1
    for i in (len(S)-1):
        if S[i] != S[i+1]:
            if S[i] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1

print(min(cnt_0, cnt_1))