'''Write a function to get a new string from a given string by adding 'Is' to the beginning of the input string. If the given string already begins with
'Is' return the input string unchanged.'''

s=input('enter a scentence')
for i in range(len(s)):
    if s[:3].lower()!='is ':
        s='is '+s
print(s)
        

'''enter a scentenceakhil is a good boy
is akhil is a good boy'''
