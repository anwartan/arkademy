def cariPasangan(a):
    a.sort()
    i=0
    jwb=[]
    while(i<len(a)-1):
        if(a[i]==a[i+1]):
            jwb.append([a[i],a[i+1]])
            i+=2
        else:
            i+=1

    print(len(jwb),"pasang:")
    for i in range(len(jwb)):
        if(i==len(jwb)-1):
            print(jwb[i],end="")
        else:
            print(jwb[i],end=",")

a=list(map(int,input().split()))
cariPasangan(a)

