n =str(input())
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    n = n.replace(i, 'a')
print(len(n))