'''Given an array arr[] containing N integers.
In one step, any element of the array can either be increased or decreased by one.
Find minimum steps required such that the product of the array elements becomes 1.
Input:
N = 3
arr[] = [-2, 4, 0)]
Output:
5
Explanation:
We can change -2 to -1, 0 to -1 and 4 to 1.
So, a total of 5 steps are required to update the elements such that the product of the final array is 1.'''

def steps(arr):
    step=0
    neg=0
    for i in arr:
        if i<0:
            neg+=1
            while(i!=-1):
                i+=1
                step+=1
        if i>0:
            while(i!=1):
                i-=1
                step+=1
        if i==0:
            step+=1
    if neg%2!=0:
        step=step+2
    return step

arr=[-5,1,2,-3,-2]
print(steps(arr))
