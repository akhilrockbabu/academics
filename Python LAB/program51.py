'''Write a program to search an item in a given list and display the number of occurrences of the given item.'''

l=input('enter the items in list with space').split()
item=input('enter the item to search')
count=0
for i in range(len(l)):
    if l[i].lower()==item.lower():
        count+=1
print('number of occurances are:',count)


'''enter the items in list with space1 2 albert Akhil FRestin FRESTIN frestin
enter the item to searchFresTiN
number of occurances are: 3'''
