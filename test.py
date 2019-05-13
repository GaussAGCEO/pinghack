from time import sleep
import os
import ctypes

def pingfake():
    username = input("Benutzername: ")
    pingAddr = input("IPv4 Adresse: ")
    

    clear = None
    if(os.name == "posix"):
        clear = lambda: os.system('clear')
        for i in range(88):
            clear()
            clear()
    elif(os.name == "nt"):
        clear = lambda: os.system('cls')
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW("Eingabeaufforderung - ping "+pingAddr+" -t")
    
    x = "Microsoft Windows [Version 10.0.17763.437]\n(c) 2018 Microsoft Corporation. Alle Rechte vorbehalten.\n"
    print(x)
    c = 'C:/Users/'
    print(c+username+'>ping '+pingAddr+' -t\n\nPing wird ausgeführt für '+pingAddr+' mit 32 Bytes Daten:')
    while 0 == 0:
        print("Antwort von 10.14.51.140: Zielhost nicht erreichbar.")
        sleep(3)

pingfake()
