# 4-1) 10952번: A+B-5
while (True):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break;
    else:
        print(A + B)

# 4-2) 10951번: A+B-4
while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    print(A + B)

# 4-3) 1110번: 더하기 사이클 (틀림)
