'''write a function that accepts full name and display in reveerse order of words with space between them'''
def rev_names(name):
    for word in name[::-1]:
        print(word,end=' ')
n=input('enter a full name')
n=n.split()
rev_names(n)

