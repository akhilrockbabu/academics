def uniqchar(s,k):
    i=0
    j=1
    maxlen=0
    while(i<=j and i<len(s) and j<=len(s)):
        print(s[i:j])
        chars=len(set(s[i:j]))
        if chars==k and maxlen<len(s[i:j]):
            maxlen=len(s[i:j])
        elif chars<k:
            j+=1
        elif chars>k:
            i+=1
        else:
            j+=1
    print(maxlen)


uniqchar(input('enter the string'),int(input('enter the number')))
