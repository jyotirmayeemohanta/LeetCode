# list= [[1,3,1],[1,5,1],[4,2,1]]
# i=0
# k=7
# while i<len(list):
#     sum=0
#     if type(list[i])==list:
    #     j=0
    #     sum=0
    #     while j<len(list[i]):
    #         sum+=list[i][j]
    #         j+=1
    #     if sum==k:
    #         print(list[i])
    # i+=1
# print(5+3)



# l=[3,1,45,2]  
# i=0
# li=[]
# while i<len(l):
#     j=0
#     while j<len(l):
#         if l[i]+l[j]==48:
#             li.append(l[i])
#             # li.append(l[j])
#         j+=1
#     i+=1
# print(li)

# list= [[1,3,1],[1,5,1],[4,2,1]]
# i=0
# l=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         if list[i][j]+list[i][k]==7:
#             l.append(list[i][j])
#             l.append(list[i][k])
#             print(l)
#             k+=1
#         print(l)
#         j+=1
#     i+=1   




# input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# l=[[1,3,1],[1,5,1],[4,2,1]]
# i=0
# sum=0
# j=0
# while j<len(l):
#     sum+=l[i][j]
#     j+=1
# i+=1
# while i<len(l):
#     sum+=l[i][-1]
#     i+=1
# print(sum)

l=[[1,2,3],[4,5,6]]
i=0
sum=0
j=0
while j<len(l[i]):
    sum+=l[i][j]
    j+=1
i+=1
while i<len(l):
    sum+=l[i][-1]
    i+=1
print(sum)

