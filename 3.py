

def HollowTriangle(a):
    if(a%2==1):
        z = (int(a)+1)/2
        a=int(a)
        for i in range(int(z)):
            for j in range(a):
                if(i==0 or i==j or a-i-1==j):
                    print("o",end=" ")
                elif(j>=i and a-i-1>j ):
                    print("x",end=" ")
                else:
                    print(" ",end=" ")
            print()
    else:
        print("Bilangan Bukan Ganjil")
a=int(input())
HollowTriangle(a)
