string=input("enter a string")
rev=string[::-1]
bool(rev==string) and print("the given string",string,"is a palindrome")
bool(rev!=string) and print("the given string",string,"is not a palindrome")
