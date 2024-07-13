def stocks(nums):
    buy=nums[0]
    profit=0
    sell=-1
    for i in range(len(nums)):
        if nums[i]<buy:
            buy=nums[i]
        if nums[i]-buy>profit:
            profit=nums[i]-buy
            sell=nums[i]
    print('profit = ',profit)

stocks(list(map(int,input('enter the list').split())))