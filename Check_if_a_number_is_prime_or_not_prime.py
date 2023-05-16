number = int(input("Please enter the and Integer: "))
z = 0
for i in range(1,number + 1):
    if number % i == 0:
        z += 1
if z == 2:
    print("Number is prime.")
else:
    print("Number is not prime.")
