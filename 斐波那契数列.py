
list1=[1,1]
a=int(input())-1
counter=1
while counter!=a:
    c=list1[counter]+list1[counter-1]
    list1.append(c)
    counter+=1
print(list1)




