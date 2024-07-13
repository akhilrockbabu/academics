def rotate(arr):
    arr2=[[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr2[j][i]=arr[i][j]
    for i in arr2:
        print(i[::-1])

rotate([[1,2,3],[4,5,6],[7,8,9]])