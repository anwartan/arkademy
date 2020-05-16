
def findDuplicates(a):
    if(type(a)==str):
        a=a.replace(" ","")
        b=list(a)
        i=0
        jwb={}
        while(i<len(b)-1):
            if(jwb.__contains__(b[i])!=True):
                jwb[b[i]]=1
            else:
                jwb[b[i]]+=1
            i+=1
        total=0
        for i in jwb:
            if(jwb[i]>1):
                total+=1
                print(i+":"+str(jwb[i]))
        if(total==0):
            print("Tidak ada karakter yang berulang!") 
    else:
        print("Harus memasukan parameter dan harus string!")
a=input()
findDuplicates(a)
