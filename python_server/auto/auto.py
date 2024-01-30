from telethon import TelegramClient, events

api_id = '25362028'
api_hash = 'da9cd1df95149fede816e2b5aa22a813'
phone_number = '+380992105723'
source_channel = '@air_alert_ua'
destination_channel = '@airalarm_map'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    await client.send_message(destination_channel, event.message.text)

if __name__ == "__main__":
    client.start(phone_number)
    client.run_until_disconnected()
