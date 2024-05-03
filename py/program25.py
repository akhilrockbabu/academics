st=input('enter a string')
if st.lower().endswith('ing'):
    st+='ly'
else:
    st+='ing'
print(st)
