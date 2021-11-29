# list1 = [1,1,2,3,4,5,5,7,6,9,10]
# list2 = [11,12,13,4,5,6,7,18,19,20]
# list3 = []
# for i in list1:
#     if i in list2:
#         pass
#     else:
#         list3.append(i)
# for i in list2:
#     if i in list1:
#         pass
#     else:
#         list3.append(i)
# print(len(list3))

n=int(input())
n3={}
for i in range(n):
    n1=input("Enter Student Name : ")
    n2=int(input("Enter Student Marks : "))
    n3[n1]=n2
print(n3) 