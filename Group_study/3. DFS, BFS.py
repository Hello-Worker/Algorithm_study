#def recursive_function(i):
#    #100번째 호출을 했을 때 종료되도록 종료 조건 명시
#    if i == 5:
#        return
#    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
#    recursive_function(i+1)
#    print(i, '번째 재귀함수를 종료합니다.')
# 왜 거꾸로 출력될까 ㅠㅠ
#recursive_function(1)

def recursive_function(i):
    if i == 5:
        print('재귀 끝', i)
        return
    # 각 호출된 함수 이름 지어주기
    print('함수 라벨링 : ', i, '번 재귀함수')
    recursive_function(i+1)
    print('함수 라벨링 : ', i, '번 재귀함수 끝')

recursive_function(1)