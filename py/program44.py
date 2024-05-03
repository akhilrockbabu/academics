'''program to find sum of digits of a number'''

def sum_of_dgts(n):
    if n%10==n:
        return n
    else:
        return (n%10)+sum_of_dgts(n//10)
        


n=int(input("enter a number"))
print(sum_of_dgts(n))

'''enter a number124
7'''

