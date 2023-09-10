X = 10
Y = 20
#there are thre connditions - X>Y, X<Y, X=Y
#if there are multiple conditions, then we have to use elif
#if condition 1
#elif condition 2
#elif condition 3
#else........ we can write unlimited conditions
X = int(input("Enter X"))
Y = int(input("Enter Y"))
if X>Y:
    print("X>Y")
elif Y>X:
    print("Y>X")
else:
    print("X=Y")