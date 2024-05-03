'''Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square. '''

import math
def sqrt_even_num(n1,n2):
    l=[]
    if n1>999 and n2<=9999:
        for i in range(n1,n2+1):
            if math.sqrt(i).is_integer():
                s=str(i)
                if s[0]!='0' and s[1]!='0' and s[2]!='0' and s[3]!='0':
                    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
                        l.append(s)
    else:
        print('please enter a four digit number')
    return l


n1=int(input("enter a four digit lower limit"))
n2=int(input("enter a four digit upper limit"))
print(sqrt_even_num(n1,n2))


'''enter a four digit lower limit2000
enter a four digit upper limit9000
['4624', '8464']'''
    
