# def search(nums,target):
#     for i in range(len(nums)):
#         if nums[i]==target:
#             return i
# nums=[1,3,5,6]
# target=5
# print(search(nums,target))

def addtwo_number():
    list1=[3,4,2]
    list2=[4,6,5]
    value1=""
    value2=""
    new_list=[]
    i=0
    while i<len(list1):
        value1+=str(list1[i])
        value2+=str(list2[i])
        i+=1
    var=str(int(value1)+int(value2))
    j=0
    while j<len(var):
        new_list.append(int(var[j]))
        j+=1
    return new_list
print(addtwo_number())