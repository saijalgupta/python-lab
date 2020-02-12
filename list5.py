l1=[1,2,3,4]
l2=[1,4,9,5]
l=[i for i in l1 if i not in l2]
m=[i for i in l2 if i not in l1]
print(l+m)
