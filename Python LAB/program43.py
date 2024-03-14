'''to find sum of first nwhole number'''

def sum_of_first(n):
    if n<=0:
        return n
    else:
        return n+sum_of_first(n-1)

n=int(input("enter the number"))
print(sum_of_first(n-1))


'''enter the number6
15'''
