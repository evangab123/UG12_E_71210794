dia= int(input("Masukan Angka : "))


for i in range (0, dia):
    for j in range (dia-i):
        print(" ", end="")
    for j in range (0, i+1):  
        print(" *", end="")
    print()
for k in range (dia-1):
    for j in range (-1,k+1):
        print(" ", end= "")
    for j in range (dia -1 -j):
        print(" *", end ="")
    print()

  