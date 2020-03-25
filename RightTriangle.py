t=int(input())
for l in range (t):
    rows=int(input())
    print("Case #{}:".format(l+1))
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            if(j <= rows - i):
                print(' ', end = '')
            else:
                print('*', end = '')
        print()
            
            
    
