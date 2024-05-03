'''Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station
so that no train waits. We are given two arrays that represent the arrival and departure times of trains that stop.
Example:
Input: arr = (9:00, 9:40, 9:50, 11:00, 15:00, 18:00)
dep = (9:10, 12:00, 11:20, 11:30, 19:00, 20:00)
Output: 3
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)'''

def platform(at,dt,n):
    result=0
    plat=1
    i=1
    j=0
    while(i<n and j<n):
        if at[i]<=dt[j]:
            plat+=1
            i+=1
        else:
            plat-=1
            j+=1
        result=max(plat,result)
    return result

at=list(map(int,input('arrive').split()))
dt=list(map(int,input('departure').split()))
print(platform(at,dt,len(at)))
