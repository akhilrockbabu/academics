line=input('enter the scentence')
words={}
for i in line.split():
    words[i]=words.get(i,0)+1
print(words)
