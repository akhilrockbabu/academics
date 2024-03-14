'''Program to print the pattern:
  5 4 3 2 1 1 2 3 4 5
  5 4 3 2     2 3 4 5
  5 4 3         3 4 5
  5 4             4 5
  5                 5
  '''
 
for i in range(1,6): #i loop for rows
    for j in range(1,11): # j loop for columns
        if (j==1 or j==10) and i<=5:
            print("5",end=" ")
        elif (j==2 or j==9) and i<=4:
            print("4",end=" ")
        elif (j==3 or j==8) and i<=3:
            print("3",end=" ")
        elif (j==4 or j==7) and i<=2:
            print("2",end=" ")
        elif (j==5 or j==6) and i<=1:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    break
print("")
for i in range(1,6): #i loop for rows
    for j in range(1,11): # j loop for columns
        if (j==1 or j==10) and i<=5:
            print("4",end=" ")
        elif (j==2 or j==9) and i<=4:
            print("3",end=" ")
        elif (j==3 or j==8) and i<=3:
            print("2",end=" ")
        elif (j==4 or j==7) and i<=2:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    break
print("")
for i in range(1,6): #i loop for rows
    for j in range(1,11): # j loop for columns
        if (j==1 or j==10) and i<=5:
            print("3",end=" ")
        elif (j==2 or j==9) and i<=4:
            print("2",end=" ")
        elif (j==3 or j==8) and i<=3:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    break
print("")
for i in range(1,6): #i loop for rows
    for j in range(1,11): # j loop for columns
        if (j==1 or j==10) and i<=5:
            print("2",end=" ")
        elif (j==2 or j==9) and i<=4:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    break
print("")
for i in range(1,6): #i loop for rows
    for j in range(1,11): # j loop for columns
        if (j==1 or j==10) and i<=5:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    break
print("")
 
'''Output:
5 4 3 2 1 1 2 3 4 5  
5 4 3 2   2 3 4 5  
5 4 3     3 4 5  
5 4       4 5  
5         5  '''
