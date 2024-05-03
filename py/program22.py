word=input('enter the word')
letters={}
for i in word:
    letters[i]=letters.get(i,0)+1
print(letters)
