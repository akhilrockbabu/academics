'''Find the element which has a occurance of more than (n/2) times in the array.
where n is the number of elements of array.

Example :
arr=(2,1,0,2,2)
output=2
explanation : 2 occurs at the more than half the number of elements of array'''

def nums(arr):
    l=[]
    for i in set(arr):
        if arr.count(i)>len(arr)//2:
            print(i)
    

arr=list(map(int,input('enter the array').split()))
nums(arr)
