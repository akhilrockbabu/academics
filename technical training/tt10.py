def valleys(uds):
    current=0
    status=0
    count=0
    for i in uds:
        if i=='u':
            current+=1
        else:
            current-=1
        if current<0:
            status=-1
        if current==0 and status==-1:
            count+=1
    print('vallyes = 'count)
        
valleys(input('enter the string'))