N = int(input())
lists = []
for i in range(N):
    s,e = map(int, input().split())
    lists.append([s,e])

go = sorted(lists, key=lambda x: x[0])
back = sorted(lists, key=lambda x: x[1])

result = lists[-1][0] - lists[0][1]
if result <= 0:
    print(0)
else:
    print(result)