import Database

def appendGlobalUser(elmt,arr):
    for i in range(lengthList(arr)):
        if arr[i] == ['' for i in range(3)]:
            arr[i]=elmt
            break

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

def MinIdCandi():
    for i in range (100):
        if Database.daftar_candi[i] == [0, "", 0, 0, 0]:
            return i
        
def HitungSisaCandi():
    count = 0
    lenArr = lengthList(Database.daftar_candi)
    for i in range(lenArr):
        if Database.daftar_candi[i] == [0, '', 0, 0, 0]:
            count = count + 1
    return(count)

def HitungBaris_daftar_akun():
    count = 0
    lenArr = lengthList(Database.daftar_akun)
    for i in range(lenArr-1,-1,-1):
        count += 1
        if Database.daftar_akun[i] != ['', '','']:
            break
    return(102-count)

def HitungBaris_daftar_candi():
    count = 0
    lenArr = lengthList(Database.daftar_candi)
    for i in range(lenArr-1,-1,-1):
        count += 1
        if Database.daftar_candi[i] != [0, '', 0, 0, 0]:
            break
    return(100-count)