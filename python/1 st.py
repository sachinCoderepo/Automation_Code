
# a = 10
# b = 7
# i = a+b
# c = i*a
# if (i < 15):
#     print("i is smaller than 15")
    
# else:
#     print(c)
    
# count = 0
# a = 1456466
# while a>0:
#     a= a//10
#     count = count +1
# print(count)
# n = 2
# def staircase(n):
#     for i in range(n):
#         string =""
#         for j in range(n-i-1):
#             string +=" "
        
#     for k in range(i+1):
#         string +="#"
    
#         print(string)
    


# staircase(n)



# size = 7

# m = (2 * size)-2

# for i in range(0, size):

#     for j in range(0, m):

#         print(end =" ")

#     m = m - 1 # decrementing m after each loop

#     for j in range(0, i + 1):

#         # printing full Triangle pyramid using stars

#         print("#", end=' ')

#     print(" ")

n = 5
for i in range(1,n+1):   
    print(f"{' ' * (n-i) }{'#' * i}")