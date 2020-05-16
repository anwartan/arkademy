def cek_kata(a):
    b=a.split(" ")
    total=0
    for i in range(len(b)):
        if(b[i].isdigit()!=True):
            total+=1
    print(str(total)+"/"+str(len(b)))

x=input()
cek_kata(x)



