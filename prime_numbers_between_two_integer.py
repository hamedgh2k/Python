first = int(input("Please enter the first number: "))
second = int(input("Please enter the sirst number: "))
for i in range(first + 1,second):
  count = 0
  for j in range(1,i + 1):
    if i % j == 0:
      count += 1
  if count == 2:
    print(i)
