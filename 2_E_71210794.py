harii = input("Hi Tutu, Silahkan masukan hari yang ingin Anda telusuri : ")
#harihari = ["senin", "selasa", "rabu" , "kamis" , "jumat"]

pelajaran= [["1 Algortima Graf", "3 Sistem Operasi", "4 PAK", "5 Praktikum INLAN"], ["2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN" ],["1 IMK", "3 LogMat", "4 Praktekkom"],["2 Sitem Basis Data", "4 Praktikum Sistem Basis Data", "6 INLAN"]]
hari = harii.lower()
#pelajaran= [
#["1 Algortima Graf", "2 Matematika Teknik", "1 IMK", "2 Sitem Basis Data"],
#["3 Sistem Operasi", "4 Bhs Indonesia","3 LogMat", "4 Praktikum Sistem Basis Data"],
#["4 PAK", "6 PKN" , "4 Praktekkom""6 INLAN"],
#["5 Praktikum INLAN"]
 #]
if hari == "senin":
        for mapel in pelajaran[0]: 
                print ("kelas ke-"+mapel)
elif hari == "selasa":
        for mapel in pelajaran[1]:
            print ("kelas ke-"+mapel)

elif hari == "rabu":
        print ("Hari rabu Anda tidak ada kelas")
elif hari == "kamis":    
        for mapel in pelajaran[2]:
            print ("kelas ke-"+mapel)
elif hari =="jumat":
        for mapel in pelajaran[3]:
            print("kelas ke-"+mapel)

else:
    print("Pilih dari hari senin sampai jumat !")