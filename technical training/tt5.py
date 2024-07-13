def valid(s):
    '''new=[]
    if len(s)%2==0:
        for i in s:
            if i=='{':
                new.append(i)
            else:
                if len(new)!=0:
                    new.pop(-1)
        if len(new)==0:
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')'''

    count=0
    for i in s:
        if i=='{':
            count+=1
        else:
            count-=1
            if count<0:
                break
    if count==0:
        print('valid')
    else:
        print('invalid')

valid(input())
            
        
