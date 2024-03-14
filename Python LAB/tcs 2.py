
print('select your numbers from : -3  -5  10  23  12  1  -10')#displays the numbers to choose from
n=int(input('how many numbers you want to select '))
num=[]#list to store selected numbers
for i in range(n):
    print('enter priority',i+1, 'number : ')
    d=int(input())
    num.append(d)
efficiency=0
for i in range(len(num)):
    efficiency+=num[i]*(i+1)

if efficiency<0:
    print(0)
else:
    print(efficiency)
    
