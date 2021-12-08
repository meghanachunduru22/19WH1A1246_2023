n = 5
for i in range(n):
    for j in range(65,65+i+1):
        print(chr(j),end=" ")
    print()

for i in range(65,65+n+1):
    print((chr(i)+" ")*(i-64))

    