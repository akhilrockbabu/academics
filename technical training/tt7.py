def search(nums,k):
    low=0
    high=len(nums)-1
    result=-1
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==k:
            result=mid
            high=mid-1
        elif nums[mid]>k:
            high=mid-1
        else:
            low=mid+1
    if result!=-1:
        print(k,'is at index',result)

search(list(map(int,input('enter the array').split(' '))),int(input('enter the number')))
