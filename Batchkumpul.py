import Database
import Misc
import random

def batchkumpul():
    if Database.access!="bondowoso":
        print("Hanya Bandung Bondowoso yang memiliki akses")
    else:
        count = 0
        totalPasir = 0
        totalBatu = 0
        totalAir = 0
        for i in range (Misc.lengthList(Database.daftar_akun)):
            if Database.daftar_akun[i][2]=="pengumpul":
                count = count + 1
        for i in range(count):
            pasir=random.randint(1,5)
            batu=random.randint(1,5)
            air=random.randint(1,5)
            totalPasir += pasir
            totalBatu += batu
            totalAir += air

        Database.bahan_bangunan[0][2]+=totalPasir
        Database.bahan_bangunan[1][2]+=totalBatu
        Database.bahan_bangunan[2][2]+=totalAir

        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {totalPasir} pasir, {totalBatu} batu, dan {totalAir} air.")