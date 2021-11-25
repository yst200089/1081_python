i for i in range(6):
[0, 1, 2, 3, 4, 5]
[i if i%2 == 0 else 3*i+1 for i in range(6)]
[0, 4, 2, 10, 4, 16]
print(*[i if i%2 == 0 else 3*i+1 for i in range(6)])
0 4 2 10 4 16