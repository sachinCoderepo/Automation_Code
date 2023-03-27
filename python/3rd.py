# story = "once upon a time in mumbai has a villan name rocky bhai"
# print(len(story))
# print(story.endswith("bhai"))
# print(story.count("a"))
# print(story.find("ock"))
# print(story.replace("rocky" , "rajan"))
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# print(set(ar))
# count = 0
# l =[]
# s =0
# for i in set(ar):
#     l.append(ar.count(i)) 
    

# print(sum([i//2 for i in l]))
# for i in l:
#     s = s+i//2
# print(s)


def prime(n):
    for i in range(2,int(n/2)+1):

        if n%i ==0:
            print("Not prime")
            break
    else:
        print("prime")

prime(29)