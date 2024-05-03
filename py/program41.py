'''function to find sum of list of numbers'''

def total(l):
    if len(l)<=1:
        return l[0];
    else:
        return l[0]+total(l[1:])

l=[1,2,3,4,5]
print(total(l))


'''5'''
