def triangle(x):
    if(x.isdigit()):
        if(int(x)<=0):
           print("Paramemeter harus angka dan positif!")
        else:
            for i in range(1,int(x)+1):
                print(i*"#")
    else:
        print("Paramemeter harus angka dan positif!")
    


a=input()
triangle(a)
