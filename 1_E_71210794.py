awal= int(input("Masukan awal deret : "))
akhir= int(input("Masukan akhir deret : "))


for i in range (1):
    for j in range (awal, akhir):
        if j%2==0 and j%5!=0 and j%9!=0:
            print(j, end =" ")