'''Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k.
Example 1:
Input:
N = 5
Arr = (10, 2, -2, -20, 10)
k = -10
Output: 3
Explaination:
Subarrays: arr [O...3], arr [1...4), ar[3..4)
have sum exactly equal to -10.

Example 2:
Input:
N = 6
Arr = (9, 4, 20, 3, 10, 5)
k=33
Output: 2
Explaination:
Subarrays: ar0...2], arr[2...4) have sum
exactly equal to 33.'''


arr=[10,2,-2,-20,10]
k=-10
res=0
sumi=0
d={}
for i in arr:
    sumi+=i
    if sumi==k:
        res+=1
    if sumi in d:
        d[sumi]+=1
    else:
        d[sumi]=1
    if sumi-k in d:
        res+=d[sumi-k]
print(res)

