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

channel_ids = []
while True:
    channel_id = input("Masukkan ID channel (tekan Enter untuk selesai): ")
    if not channel_id:
        break
    channel_ids.append(channel_id)

waktu = int(input("Set Waktu Kirim Pesan (dalam detik): "))

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    for channel_id in channel_ids:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message to channel " + channel_id + ": ")
        print(Fore.YELLOW + payload['content'])

        time.sleep(waktu)
