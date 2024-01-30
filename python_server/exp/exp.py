import re
from telethon import TelegramClient, events

api_id = '19564004'
api_hash = '8430fb375ac8c98d5ca6b8c16736f07c'

client = TelegramClient('anon', api_id, api_hash)

# Ідентифікатор каналу, який слідкуємо
source_channel_username = '@UkraineAlarmSignal'

# Ідентифікатор каналу, куди відправляємо змінене повідомлення
destination_channel_username = '@airalarm_map'

@client.on(events.NewMessage(chats=source_channel_username))
async def process_message(event):
    message = event.message

    if message.fwd_from:
        return

    if not message.text and not message.media:
        return

    print(f"Received message: {message.text}")

    # Ключове слово для слідкування
    keyword = 'ЗМІ'

    if keyword in message.text:
        # Видаляємо значок та робимо текст жирним
        edited_text = f"💥 <b>{message.text.replace('⚠️', '').strip()}</b>"
        # Зберігаємо форматування жирного тексту
        if '**' in message.text:
            edited_text = edited_text.replace('**', '', 1)
            edited_text = edited_text.replace('**', '', 1)
        # Пересилаємо в інший канал
        await client.send_message(destination_channel_username, edited_text, parse_mode='html')

        # Видаляємо оригінальне повідомлення
        await message.delete()

print("Starting the Telethon client...")
client.start()
print("Telethon client started successfully!")
client.run_until_disconnected()
print("Program terminated.")
