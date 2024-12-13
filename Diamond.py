rowsize=int(input("Enter the number of rows: "))
if rowsize%2==0:
    halfdiamondrow=int(rowsize/2)
else:
    halfdiamondrow=int(rowsize/2)+1
space=halfdiamondrow-1
for i in range(1,halfdiamondrow+1):
    for j in range (1,space+1):
        print(end=" ")
    space=space-1
    number=1
    for j in range(2*i-1):
        print(end=str(number))
        number+=1
    print()
space=1
for i in range(1,halfdiamondrow):
    for j in range(1,space+1):
        print(end=" ")
    space=space+1
    number=1
    for j in range(1,2*(halfdiamondrow-i)):
        print(end=str(number))
        number+=1
    print()