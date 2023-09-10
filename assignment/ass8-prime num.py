#TO CHECK IF A NUMBER IS A PRIME NUMBER
#Prime number is a natural numer greater than 1 that has no positive divisors other than 1 and itself
#eg:2,5,7,11,13,19,...

num = int(input("Enter your number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print("please enter any number greater than 0")









