'''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = (1,2,5), amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
Input: coins = (2), amount = 3
Output: -1
Example 3:
Input: coins = (1), amount = 0
Output: 0'''


coins=list(map(int,input('enter the coins').split()))
amount=int(input('enter the amount'))
l=[0]
for i in range(1,amount+1):
    l.append('$')
    for j in coins:
        if i-j>=0:
            result=l[i-j]
            if result!='$':
                if l[i]=='$':
                    l[i]=result+1
                else:
                    l[i]=min(l[i],result+1)
if l[amount]!='$':
    print(l[amount])
else:
    print(-1)
                     
        
        
