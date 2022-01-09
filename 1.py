print("====Soal 1===")
print("====5200411260===")
print("====M Nurmansyah===")
print("Masukan Inputan!!!")
ram = int(input("Kapasitas RAM (MBps): "))
blok = int(input("Blok/Unit : "))
petabit = int(input("Total Petabit (MBps): "))
so = int(input("RAM yang dipakai SO (MBps): "))
prog1 = int(input("RAM yang dipakai Program 1 (MBps): "))
prog2 = int(input("RAM yang dipakai Program 2 (MBps): "))

kram = ram * 1000
sampah = ram - (so + prog1 + prog2)
isiBlok = kram / blok
alokasi1 = (so / isiBlok)
blok1 = ((prog1 + prog2) / isiBlok) + alokasi1
blok0 = blok - blok1
alokasi0 = blok -alokasi1

print("================== ")
print("====Ouputan!!!====")
print("Kapasitas RAM adalah",ram,"MBps")
print("Kapasitas Peta Bit adalah",petabit,"MBps")
print("Memori yang terpakai :",so,"MBps")
print("Kapasitas Sampah memori :",sampah,"MBps")
print("Jumlah Blok Bernilai 1 : ",blok1,"KBps")
print("Jumlah Blok Bernilai 0 : ",blok0,"KBps")
print("Alokasi Blok Bernilai 1 : ",alokasi1,"KBps")
print("Alokasi Blok Bernilai 0 : ",alokasi0,"KBps")