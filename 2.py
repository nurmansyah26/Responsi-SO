print("====Soal 2===")
print("====5200411260===")
print("====M Nurmansyah===")
print("Masukan Inputan!!!")
prog1 = str(input("Nama Program 1 : "))
wkt1 = int(input("Waktu Program 1 : "))
prog2 = str(input("Nama Program 2 : "))
wkt2 = int(input("Waktu Program 2 : "))
prog3 = str(input("Nama Program 3 : "))
wkt3 = int(input("Waktu Program 3 : "))
q = int(input("Quantum Time / Jatah waktu : "))

urutan = [wkt1, wkt2, wkt3]

print("================== ")
print("====Ouputan!!!====")
print("Nama Program 1 :",prog1,"dan Lama Waktu Program 1 :",wkt1)
print("Nama Program 2 :",prog2,"dan Lama Waktu Program 2 :",wkt2)
print("Nama Program 3 :",prog3,"dan Lama Waktu Program 3 :",wkt3)
print("Lama Waktu Program 1-3 =",urutan)
print("Quantum Time / Jatah Waktu :",q)
print("Urutan Round Robin nya adalah")
if wkt1>wkt2 and wkt2>wkt3:
        if wkt2>wkt3:
            print(wkt1, wkt2, wkt3)
        else:
            print(wkt1, wkt3, wkt2)
elif wkt2>wkt1 and wkt2>wkt3:
        if wkt1>wkt3:
            print(wkt2, wkt1, wkt3)
        else:
            print(wkt2, wkt3, wkt1)
else:
        if wkt1>wkt2:
            print(wkt3, wkt1, wkt2)
        else:
            print(wkt3, wkt2, wkt1)



