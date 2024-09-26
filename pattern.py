for i in range(0,5):
    for j in range(i,5):
        print("*", end=" ")
    print()

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2 *i -1))
    
    
class pattern():
    def __init__(self):
        print('Hello Guys')
    def drawing(self,coloum, row);
        for i in range(0,coloum):
            for j in range(0, row):
                if i==0 or i == coloum-1:
                    print("*" end="")
                
                        
