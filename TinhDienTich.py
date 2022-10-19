import math #thu vien toan de tinh can bac hai

#input
    a= float(input("Moi nhap canh 1:"))
    b= float(input("Moi nhap canh 2:"))
    c= float(input("Moi nhap canh 3:"))

    print ("Gia tri canh 1 la :"+ str(a))
    print ("Gia tri canh 2 la :"+ str(b))
    print ("Gia tri canh 3 la :"+ str(c))
#kiem tra dieu kien
    if (a+b)>c:
        print("a,b,c khong la 3 canh cua tam giac")
        exit()
    else:    
    #tinh nua chu vi
        p=(a+b+c)/2
    #tinh dien tich
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    #tinh tong 3 canh
        Tong=a+b+c
    
#hien thi ket qua
    print ("Gia tri tong 3 canh la :"+ str(Tong))
    print ("Gia tri dien tich tam giac la :"+ str(s))

