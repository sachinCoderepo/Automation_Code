a = int(input("Enter a no. for know the no is prime or not--"))
flage=True
for n in range (2,a):
    if a%n == 0:
        flage=False
        break
if flage:
    print('number is prime')  
else:
    print("number is not prime")

