import argparse, os
import Database

def CSV_Parser():
    Database.init()

    fu = open("Data\\user.csv", 'r')
    baris = 0
    fake = fu.readline()

    while True:
        line = fu.readline()
        kolom = 0
        temp = ''
        for i in range (len(line)):
            if line[i]==";" or line[i]=="\n":
                Database.daftar_akun[baris][kolom] = temp
                temp = ''
                kolom = (kolom + 1) % 3
            else:
                temp += line[i]
            
        baris += 1
        
        if not line:
            break
    fu.close
    
    fc = open("Data\\candi.csv", 'r')
    baris = 0
    fake = fc.readline()

    while True:
        line = fc.readline()
        kolom = 0
        temp = ''
        for i in range (len(line)):
            if line[i]==";" or line[i]=="\n":
                Database.daftar_candi[baris][kolom] = temp
                temp = ''
                kolom = (kolom + 1) % 5
            else:
                temp += line[i]
            
        baris += 1
        
        if not line:
            break
    fc.close
    
    fb = open("Data\\bahan_bangunan.csv", 'r')
    baris = 0
    fake = fb.readline()

    while True:
        line = fc.readline()
        kolom = 0
        temp = ''
        for i in range (len(line)):
            if line[i]==";" or line[i]=="\n":
                Database.bahan_bangunan[baris][kolom] = temp
                temp = ''
                kolom = (kolom + 1) % 3
            else:
                temp += line[i]
            
        baris += 1
        
        if not line:
            break
    fb.close
    
    
    


def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder")
    args = parser.parse_args()

    if args.nama_folder == '':
        print("Tidak ada nama folder yang diberikan!")
        print("\nUsage: python -u main.py <nama_folder>")
    if os.path.exists(args.nama_folder):
        print("Loading...\n")

        # parsing csv to list 
        CSV_Parser()
    else:
        print(f"Folder \"{args.nama_folder}\" tidak ditemukan")

