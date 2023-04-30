import Database

def lengthString(str):
    arr = list(str)
    mark = "$$"
    arr = arr + [mark]
    count = 0
    i = 0
    while arr[i] != "$$":
        count += 1
        i += 1
    return count

def lengthList(arr):
    mark = "$$"
    arr = arr + [mark]
    count = 0
    i = 0
    while arr[i] != "$$":
        count += 1
        i += 1
    return count

def hapusjin():
    if Database.access!="bandung_bondowoso":
        print("Hanya Bandung yang memiliki akses")
    else:
        username = ""
        found = False

        while username == "":
            tempUsername = input("Masukkan username jin :")

            for i in range(lengthList(Database.daftar_akun)):
                if tempUsername == Database.daftar_akun[i][0]:
                    found = True
                    del Database.daftar_akun[i]
                    break
            
            if found == False:
                print("Tidak ada jin dengan username tersebut.")
            else:
                username = tempUsername
                print("Jin telah berhasil dihapus dari alam gaib.")
            
