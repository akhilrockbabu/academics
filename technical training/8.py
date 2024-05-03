'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example : 
Input: 2,0,2
Output: 2

input:
{3, 0, 2, 0, 4}
output :
7

input :{0 , 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
output : 6'''


def trap(arr,n):
    size=n-1
    local_max=arr[0]
    water=0
    last_bucket=0
    for i in range(1,size+1):
        if arr[i]>=local_max:
            local_max=arr[i]
            local_max_index=i
            last_bucket=0
        else:
            water+=local_max-arr[i]
            last_bucket+=local_max-arr[i]
    if local_max_index<size:
        water-=last_bucket
        local_max=arr[size]
        for i in range(size,local_max_index-1,-1):
            if arr[i]>=local_max:
                local_max=arr[i]
            else:
                water+=local_max-arr[i]
    return water


blocks=list(map(int,input('enter the coins').split()))
print(trap(blocks,len(blocks)))
