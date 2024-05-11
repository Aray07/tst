import requests
import random
import time
import os
from colorama import Fore

author = "Aray"
print("Author: " + author)
script = "Auto Post Discord"
print("Script: " + script)
print("===========================================\n")

channel_id = input("Masukkan ID channel: ")
waktu = int(input("Set Waktu Kirim Pesan (dalam detik): "))

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    messages = f.read().splitlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    # Gabungkan pesan menjadi satu pengiriman jika lebih dari satu baris
    message = '\n'.join(random.choices(messages, k=random.randint(1, 5)))

    payload = {
        'content': message
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message to channel " + channel_id + ": ")
    print(Fore.YELLOW + message)

    time.sleep(waktu)
