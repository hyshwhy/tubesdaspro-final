import Database
import Misc
import random

def batchbangun():
    if Database.access!="":
        print("Hanya Bandung Bondowoso yang memiliki akses")
    else:   
        candi_berhasil=Database.daftar_candi
        bahan_berhasil=Database.bahan_bangunan
        count=0
        pasirTotal=0
        batuTotal=0
        airTotal=0
        for i in range (Misc.lengthList(Database.daftar_akun)):
            pasir=0
            batu=0
            air=0
            
            
            if Database.daftar_akun[i][2]=="pembangun":
                pasir=random.randint(1,5)
                batu=random.randint(1,5)
                air=random.randint(1,5)
                count = count + 1
                candi_berhasil[Misc.MinIdCandi()] = [Misc.MinIdCandi(), Database.daftar_akun[i][0], pasir, batu, air]
                pasirTotal+=pasir
                batuTotal+=batu
                airTotal+=air

        print(f"Mengerahkan {count} jin untuk membangun candi dengan total bahan {pasirTotal} pasir, {batuTotal} batu, dan {airTotal} air.")

        if pasirTotal<=Database.bahan_bangunan[0][2] and batuTotal<=Database.bahan_bangunan[1][2] and airTotal<=Database.bahan_bangunan[2][2]:
            print(f"Jin berhasil membangun total {count} candi")
            Database.daftar_candi=candi_berhasil
            Database.bahan_bangunan[0][2] -= pasirTotal
            Database.bahan_bangunan[1][2] -= batuTotal
            Database.bahan_bangunan[2][2] -= airTotal
        else:
            print("Bangun gagal, kurang",(pasirTotal-Database.bahan_bangunan[0][2]),"pasir",(batuTotal-Database.bahan_bangunan[1][2]),"batu,","dan", (airTotal-Database.bahan_bangunan[2][2]),"air")

