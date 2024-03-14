st=input('enter a scentence').split()
st=[i for i in st if len(i)==len(max(st,key=len))]
print('length of longest word',len(st[0]))
if len(st)>1:
    print('BINGO')
