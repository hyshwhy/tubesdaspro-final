import Database
import Login, Logout,Summonjin,Hapusjin,Kumpul, Bangun,Batchbangun,Batchkumpul,Help, Save, Exit
def run(perintah):
    if perintah == "login":
        Login.login()
    elif perintah =="logout":
        Logout.logout()
    elif perintah== "printakun":
        print(Database.daftar_akun)
    elif perintah=="summonjin":
        Summonjin.summonjin()
    elif perintah=="hapusjin":
        Hapusjin.hapusjin()
    elif perintah=="printbahan":
        print(Database.bahan_bangunan)
    elif perintah=="kumpul":
        Kumpul.kumpul()
    elif perintah=="bangun":
        Bangun.bangun()
    elif perintah=="printcandi":
        print(Database.daftar_candi)
    elif perintah=="batchbangun":
        Batchbangun.batchbangun()
    elif perintah=="batchkumpul":
        Batchkumpul.batchkumpul()
    elif perintah=="help":
        Help.help()
    elif perintah=="save":
        Save.save()
    elif perintah=="exit":
        Exit.exit()








