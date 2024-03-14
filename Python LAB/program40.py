'''factorial using recursion'''

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

n=int(input('enter the number'))
print(fact(n))


'''enter the number5
120'''
