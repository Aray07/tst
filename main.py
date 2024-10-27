python
   import requests
   import schedule
   import time
   from datetime import datetime
   from config import channel_ids, messages, token, webhook_url, delays

   # Fungsi untuk mengirim pesan
   def send_message(channel_id):
       current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       status_message = None

       headers = {
           'authorization': token,
           'Content-Type': 'application/json'
       }

       try:
           message_content = messages.get(channel_id, None)
           if message_content:
               payload = {'content': message_content}
               r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=payload, headers=headers)
               r.raise_for_status()
               status_embed = {
                   "title": "WEBHOOK AUTO MESSAGE",
                   "color": 3447003,
                   "description": f"Channel ID: <#{channel_id}>\nSent successfully at {current_time}",
                   "footer": {"text": "Script by @Tama"}
               }
               payload = {"embeds": [status_embed]}
               requests.post(webhook_url, json=payload, headers=headers)
       except requests.exceptions.RequestException as e:
           status_embed = {
               "title": "Failed to Send Message",
               "color": 15158332,
               "description": f"Discord Channel: <#{channel_id}>\nTime Sent: {current_time}",
               "footer": {"text": "Script by @Tama"}
           }
           payload = {"content": status_message, "embeds": [status_embed]}
           try:
               requests.post(webhook_url, json=payload, headers=headers)
           except requests.exceptions.RequestException as e:
               print("An error occurred while sending the failure message:", e)

   # Mengatur jadwal pengiriman pesan berdasarkan delay
   for channel, delay in delays.items():
       schedule.every(delay[0]).to(delay[1]).minutes.do(send_message, channel_id=channel_ids[channel])

   while True:
       schedule.run_pending()
       time.sleep(1)
