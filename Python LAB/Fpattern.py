h=int(input('enter the height of F'))
w=int(input('enter the width of F'))
for i in range(h):
    for j in range(w):
        if i==0 or j==0 or i==h/2:
            print('*',end=" ")
    print('')

'''enter the height of F10
enter the width of F10
* * * * * * * * * * 
* 
* 
* 
* 
* * * * * * * * * * 
* 
* 
* 
* '''
