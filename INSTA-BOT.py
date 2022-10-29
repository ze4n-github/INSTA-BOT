import os
import time
RED = '\033[31m'
RESET = '\033[39m'
VERDE = '\033[32m'
AZUL = '\033[34m'
AMARILLO = '\033[33m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
os.system("clear")
time.sleep(0.5)
print(AZUL+"""
 _____   _   _    _____   _______                       ____     ____    _______ 
|_   _| | \ | |  / ____| |__   __|     /\              |  _ \   / __ \  |__   __|
  | |   |  \| | | (___      | |       /  \     ______  | |_) | | |  | |    | |   
  | |   | . ` |  \___ \     | |      / /\ \   |______| |  _ <  | |  | |    | |""" + RED + " Version 1.0")
print(""" _| |_  | |\  |  ____) |    | |     / ____ \           | |_) | | |__| |    | |
|_____| |_| \_| |_____/     |_|    /_/    \_\          |____/   \____/     |_|  """ + AZUL + " CREATED BY ZE4N")
print ("\n \n")
time.sleep(0.7)



print(CYAN+"Autor    :" + RED + "ZE4N \n ")
time.sleep(0.5)
print(CYAN+"INSTAGRAM:" + RED +  "ze4n.sh \n ")
time.sleep(0.5)
print(CYAN+"TIK TOK  :" + RED +  "ZE4N___C0NGU1T0X \n \n")
time.sleep(1.2)


print(VERDE+"[1] Ganar seguidores")
print("[2] Dejar de seguir \n")

a = input (MAGENTA+ "Elige una opcion: " +RESET)
if a =="1": os.system("bash FOLLOW.sh")
elif a =="2": os.system("bash UNFOLLOW.sh")
