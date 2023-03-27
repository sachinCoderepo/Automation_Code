# # # Python program to find minimum
# # # sum of product of number
def findMinSum(num):
	sum = 0
	i = 2
	for a in range(2, int(num/2)+1):
		if num % a == 0:
			while(i*i <= num):
				while(num % i == 0):
					sum = sum + i
					num = num // i
				i = i+1
				if num==1:
					return sum
			else:
				sum = num+sum
				return sum
	else:
		return num+1
	
for j in range(1,30):
	print(f"min sum of factor {j} =" , (findMinSum(j)))











