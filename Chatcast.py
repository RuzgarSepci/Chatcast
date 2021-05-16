import socket, threading
def oku(bruh, nigga):
    soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        try:
            soket.bind((bruh, nigga))
        except:
            continue
        break
    print("\nSuccessfully connected the room!\n")
    while True:
        try:
            mesaj, kimlik = soket.recvfrom(1024)
            print(mesaj.decode())
        except:
            continue
soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print("Chatcast v1.0.0")
print("2021 (c) Ruzgar Sepci. All rights reserved.")
adres = input("\nYour IP address in the network you want to connect:\n>>>")
port = int(input("\nThe port you want to connect:\n>>>"))
rumuz = input("\nYour nickname:\n>>>")
hosgeldin = "[SYSTEM] " + rumuz + " joined the room!"
threading.Thread(target=oku, args=(adres, port)).start()
while True:
    try:
        soket.bind((adres, 0))
    except:
        continue
    break
while True:
    try:
        soket.sendto(hosgeldin, ("<broadcast>", port))
    except:
        continue
    break
while True:
    mesaj = input("")
    mesaj = "<" + rumuz + ">" + mesaj
    mesaj = mesaj.encode()
    while True:
        try:
            soket.sendto(mesaj, ("<broadcast>", port))
        except:
            continue
        break
