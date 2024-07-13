'''delete duplicates from sorted natural numbers'''

def deldup(lis):
    i=0
    while(i<len(lis)-1):
        if lis[i]==lis[i+1]:
            lis.pop(i)
        else:
            i+=1
    print(lis)
    
deldup(list(map(int,input().split(' '))))
            
    
