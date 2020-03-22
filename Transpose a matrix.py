p=list(map(int,input().split()))
r=p[0]
c=p[1]
m=[]
for i in range (r):
    m.append(list(map(int, input().split())))
t=[]
for i in range (c):
    a=[]
    for j in range (r):
        a.append(m[j][i])
    t.append(a)
for i in range(len(t)):
    for j in range (r):
        print(t[i][j] , end=" ")
    print()
    
        
        
         
            
    
