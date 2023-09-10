# CALCULATE THE ELECTRICITY BILL
# first(100) units = 0
# next 100 units = 5
# after 200 units = 10

units  = int(input("Enter your total units"))

if units<100:
    print("The bill is zero")
elif units>100 and units <200:
    x = (units*5)
    print(x)
elif units>=200:
    y = (units*10)
    print(y)

# or we can modify the elif condition as
# elif units in range(100,200):

