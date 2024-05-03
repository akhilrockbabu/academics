'''to remove all the strings with length < 5 from a list of strings'''

s=input('enter a string')
l=list(filter(lambda x:len(x)>5,s.split()))
print(l)


'''enter a stringakhila akhil hill
['akhila']'''
