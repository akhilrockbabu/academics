#Program to enter list of number and take sum of each digit in the list and check if the sums are greater than 0. If greater add it in a new list. First digits in the list can be negative

l=input('enter the numbers').split()
r=[]
for i in l:
    s=0
    if i[0]=='-':
        for j in range(2,len(i)):
            s+=int(i[j])
        s+=int(i[0:2])
    else:
        for j in range(len(i)):
            s+=int(i[j])
    if s>0:
        r.append(i)
print(r)
        
            

