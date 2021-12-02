tc1= [3,20,100,-35,50]
tc2= [3,20,90,35,75]

#testcase 1
maksimal=tc1[0]
minimal=tc1[0]
x = len(tc1)

#testcase 2
maksimal2=tc2[0]
minimal2=tc2[0]
y= len(tc2)

#testcase1
for i in range (0, x):
    if tc1 [i] > maksimal:
        maksimal = tc1[i]
for i in range (0, x):
    if tc1 [i] < minimal:
        minimal = tc1[i]

#testcase2
for i in range (0, y):
    if tc2[i] > maksimal2:
        maksimal2 = tc2[i]
for i in range (0, y):
    if tc2[i] < minimal2:
        minimal2 = tc2[i]

#testcase 1
print(tc1)
print("Nilai terbesar : ",maksimal)
print("Nilai terkecil : ",minimal)

print(" ")

#testcase 2
print(tc2)
print("Nilai terbesar : ",maksimal2)
print("Nilai terkecil : ",minimal2)
