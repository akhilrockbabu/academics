def unfair(lis,k):
    lis.sort()
    unfairness=float('inf')
    for i in range(len(lis)):
        if len(lis[i:i+k])==k:
            if max(lis[i:i+k])-min(lis[i:i+k])<unfairness:
                unfairness=max(lis[i:i+k])-min(lis[i:i+k])
                sublis=lis[i:i+k]
    print(sublis)

unfair(list(map(int,input('enter the list').split(' '))),int(input('enter the num')))
        
        
