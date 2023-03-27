# a = int(input("enter a no:"))
# print("square  of the input num is :",a*a)

# name = "sachin"
# print(name[::-1])
def countingValleys( s):
    # Write your code here
    valleycount = level = 0
    
    d ={'U':1, 'D':-1}
    
    for step in s:
        level += d[step]
        print(level)
        if level== 0 and step == 'U':
            valleycount+=1
           
    return valleycount 


print(countingValleys("UDDDUDUU"))