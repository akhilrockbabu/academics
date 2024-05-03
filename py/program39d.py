'''to increment a list of integers by 10% if the number>1000 else by 5%'''

s=map(int,input('enter a list of numbers').split())
l=list(map(lambda x: x+x*0.1 if x>1000 else x+x*0.05,s))
print(l)


'''enter a list of numbers1001 23
[1101.1, 24.15]'''
