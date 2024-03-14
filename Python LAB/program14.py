string=input("enter a string")
rev=string[::-1]
if string==rev:
    print("the given string ",string,"is a palindrome")
else:
    print("the given string ",string,"is not a palindrome")
