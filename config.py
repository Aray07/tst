import os

# Channel IDs
channel_ids = {f'channel_{i}': os.getenv(f'CHANNEL_{i}_ID') for i in range(1, 1000)}

# Messages
messages = {channel_ids[f'channel_{i}']: os.getenv(f'CHANNEL_{i}_MSG') for i in range(1, 1000)}

# Discord Bot Token
token = os.getenv('DISCORD_TOKEN')

# Webhook URL
webhook_url = os.getenv('WEBHOOK_URL')

# Delays in minutes
delays = {
    f'channel_{i}': (int(os.getenv(f'CHANNEL_{i}_DELAY_MIN')), int(os.getenv(f'CHANNEL_{i}_DELAY_MAX')))
    for i in range(1, 1000)
}
