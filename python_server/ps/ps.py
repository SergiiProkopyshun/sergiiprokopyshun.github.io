from telethon import TelegramClient, events
import re

api_id = '19564004'
api_hash = '8430fb375ac8c98d5ca6b8c16736f07c'

client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(chats='@kpszsu'))
async def process_message(event):
    message = event.message

    if message.fwd_from:
        return

    if not message.text and not message.media:
        return

    print(f"Received message: {message.text}")

    if '⚡️' in message.text or '📢 Відбій' in message.text or '+' in message.text or '📢Відбій' in message.text:
        return

    edited_text = message.text.replace('⚠️ Увага!', '').replace('⚠Увага!', '').replace('⚠ Увага!', '').replace('⚠️Увага!', '').strip()
    edited_text = re.sub(r'[✈️🚀🛵☄️🛬]\s*', '', edited_text).strip()
    print(f"Edited text: {edited_text}")

    if not edited_text:
        return

    formatted_text = f"⚠️ <b>{edited_text}</b>"
    print(f"Formatted text: {formatted_text}")

    await client.send_message('@airalarm_map', formatted_text, parse_mode='html')

print("Starting the Telethon client...")
client.start()
print("Telethon client started successfully!")
client.run_until_disconnected()
print("Program terminated.")
