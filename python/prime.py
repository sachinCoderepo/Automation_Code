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

# num = int(input("inter a number : "))
# for i in range(2,int(num/2)+1):
# 	if num % i ==0:
# 		print(num, "is not a prime number")
# 		break		
# else:
# 	print(num, "is a prime number")