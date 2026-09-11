arr=[10,20,30,40]
sum=0
for a in arr:
    sum=sum+a
print(sum)

arr2=[]
arr3=[]
arr=[0,5,0,3,8,0,2]
for x in arr:
    if x!=0:
        a=x
        arr2.append(a)

    else:
        b=x 
        arr3.append(b)
           
arr2.append(arr3)
print(arr2)

