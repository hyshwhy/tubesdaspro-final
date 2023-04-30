import Database
import random
import Misc

def bangun():
    pasir=0
    batu=0
    air=0
    if Database.access!="":
        print("Hanya jin pembangun yang memiliki akses")
    else:
        pasir=random.randint(1,5)
        batu=random.randint(1,5)
        air=random.randint(1,5)

        if pasir<=Database.bahan_bangunan[0][2] and batu<=Database.bahan_bangunan[1][2] and air<=Database.bahan_bangunan[2][2]:
            Database.daftar_candi[Misc.MinIdCandi()] = [Misc.MinIdCandi(), Database.user, pasir, batu, air]

            Database.bahan_bangunan[0][2] -= pasir
            Database.bahan_bangunan[1][2] -= batu
            Database.bahan_bangunan[2][2] -= air

            print(f"Sisa candi yang perlu dibangun: {Misc.HitungSisaCandi()}.")
        else:
            "Bahan bangunan tidak cukup"

