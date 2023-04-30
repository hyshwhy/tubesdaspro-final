import Database
import Commands
Database.init()

while True:
    perintah = input(">>> ")
    
    Commands.run(perintah)
    if perintah=="exit":
        break