    # from rule import *

f = open("q1/config.txt","r")

line = f.readline()
a = line.split()

m = a[0]
m = int(m)
n = a[1]
n = int(n)
k = a[2]
k = int(k)
# print(m ,n ,k)

grid = []

for i in range(0,n):
    l = [0]*m
    grid.append(l)

for count in range (0,k):
    line = f.readline()
    d = line.split()
    x1 = d[0]
    x1 = int(x1)
    x2 = d[1]
    #print(x2)
    x2 = int(x2)
    grid[n-x2][x1-1] = 1
    count+=1

print("Initial state\n")

for i in range(0,n):
    for j in range(0,m):
        print(grid[i][j], end ="")
    print()

print("\n")

sum = 0
while(1):
    # with open("q1/output.txt","w") as g:   #write config.txt onto output initially

    #     for i in range(0,n):
    #         for j in range(0,m):
    #             a = str(grid[i][j])
    #             g.write(a)
    #         g.write("\n")
            

    iter = input("Enter number of iterations:\n")
    iter = int(iter)
    print()
    sum+=iter
    if(iter == -1):
        quit()
     
    with open("q1/output.txt","w") as g:   #write config.txt onto output initially

        for i in range(0,n):
            for j in range(0,m):
                if(grid[i][j] == 1):
                    g.write('X')
                else:
                    g.write('O')
            g.write("\n")
    g.close()
    
    array = []      #making temp array of size [n+2] * [m+1]
    for i in range(0,n+2):
        l = [0]*(m+2)
        array.append(l)


    for i in range(0,n+2):
        for j in range(0,m+2):
            if(i>0 and j>0 and i<n+1 and j<n+1):
                array[i][j] = grid[i-1][j-1]
            else:
                array[i][j] = 0
    #print(array)

    def rule(curr,l,ul,u,ur,r,dr,d,dl):
        if(l == 1):
                return 1

    for count in range(sum):
        g=open("q1/output.txt","w")
        for i in range(1,n+1):
            for j in range(1,m+1):
                curr = array[i][j]
                l = array[i][j-1]
                ul = array[i-1][j-1]
                u = array[i-1][j]
                ur = array[i-1][j+1]
                r = array[i][j+1]
                dr = array[i+1][j+1]
                d = array[i+1][j]
                dl = array[i+1][j-1]

                if(rule(curr,l,ul,u,ur,r,dr,d,dl) == 1):
                    a = i
                    b = j
                    
        array[a][b] = 1   
        for i in range (1,n+1):
            for j in range (1,m+1):
                if(array[i][j] == 1):
                    g.write('X')
                else:
                    g.write('O')
            g.write("\n")
        g.close()
    
    for i in range (1,n+1):
        for j in range(1,m+1):
            if(array[i][j] == 1):
                print('X', end ="")
            else:
                print('O',end = "")
        print()
    
    print()

    f.close()
    g.close()







