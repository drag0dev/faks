for i in range(1,11):
    print(i*i)
# 1 4 9 16 25 36 49 64 89 100

for i in [1,3,5,7,9]:
    print(i, ":", i**3)
    print(i)
# 1 : 1
# 1
# 3 : 27
# 3
# 5 : 125
# 5
# 7 : 343
# 7
# 9 : 729

x = 2 
y = 10
for j in range(0,y,x):
    print(j)
    print(x + y)
print("done")
# 0
# 12
# 2
# 12
# 4
# 12
# 6
# 12
# 8
# 12

ans = 0
for i in range(1, 11):
    ans = ans  + i*i
    print(i)
print(ans)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 385