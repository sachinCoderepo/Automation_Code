# WAP TO READ A FILE
# with open("example") as f:
#     t=f.read()
#     print(t)

# WAP for append in file
# WAP to read only 1st line
# with open("another","a") as f:
#     # t=f.readline()
#     f.write("hey whats up?/n")
    

# for n lines
# def file_rea(fname, nlines):
#     from itertools import islice
#     with open(fname) as f:
#         for line in islice(f, nlines):
#             print(line)
# file_rea("another",6)




# WAP TO READ LINES AND STORE IN LIST
# list=[]
# def rt(fname):
#     i=1
#     with open(fname) as f:
#      while i!=8:
#         l=f.readline()
#         list.append(l) 
#         i=i+1   

# rt("another")
# print(list)



# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# print(f(3))


# read the file and print twinkal is present is not
# with open("another.txt") as f:
#     s=f.read()
#     print(s)
#     if "twinkal" in s:
#         print("twenkal is present")
#     else:
#         print("twinkal is not present")


# WAPfor print table in different-different file
# for i in range(2, 21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write('\n')



# find abusing word and put censor on it

# with open("abc.txt") as f:
#     s=f.read()
# s=s.replace("abusing","******")
# with open("abc.txt","w") as f:
#     f.write(s)



words=["donkey","monkey","bsdk", "stupid"]
with open("sample.txt") as f:
    s=f.read()
for word in words:
    s=s.replace(word,"******")
    with open("sample.txt","w") as f:
        f.write(s)


        