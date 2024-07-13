def valid(s):
    new=[]
    if len(s)%2==0:
        for i in s:
            if i=='}' and new and new[-1]=='{':
                new.pop(-1)
            elif i==']' and new and new[-1]=='[':
                new.pop(-1)
            elif i==')' and new and new[-1]=='(':
                new.pop(-1)
            else:
                new.append(i)
            
        if len(new)==0:
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')

valid(input())
                
                    
                
        
