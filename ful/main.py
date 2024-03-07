# from telethon import TelegramClient, events
# import asyncio
# import os
#
# from pyppeteer import launch
#
# # Ваші API ID та хеш, отримані від Telegram
# api_id = '25362028'
# api_hash = 'da9cd1df95149fede816e2b5aa22a813'
#
# # Токен вашого бота Telegram
# bot_token = '6330357107:AAG0s_PdVm7bkhFkcDN1u9L2i7bWOd-X54Y'
#
# # ID чату або каналу, куди ви хочете надіслати скріншот
# chat_id = '-1001939636184'
#
# # Створюємо клієнт Telegram
# client = TelegramClient('anon', api_id, api_hash)
#
# # Змінна для зберігання ID останнього повідомлення
# last_message_id = None
#
# # Змінна для блокування
# is_processing = False
#
# async def main():
#     # Отримуємо entity для каналу
#     channel_entity = await client.get_entity('https://t.me/hfehsfsyfhsehf')
#
#     # Підписуємося на повідомлення з каналу
#     @client.on(events.NewMessage(chats=channel_entity))
#     async def my_event_handler(event):
#         global last_message_id
#         global is_processing
#
#         # Якщо вже обробляється повідомлення, пропускаємо це
#         if is_processing:
#             return
#
#         # Якщо повідомлення містить слова "тривога" або "відбій" або "артобстрілу!"
#         if 'тривога' in event.raw_text or 'тривоги' in event.raw_text or 'артобстрілу!' in event.raw_text:
#             # Встановлюємо блокування
#             is_processing = True
#
#             # Запускаємо браузер
#             browser = await launch()
#
#             # Відкриваємо нову сторінку
#             page = await browser.newPage()
#
#             # Встановлюємо розмір вікна браузера
#             await page.setViewport({'width': 1920, 'height': 1080})
#
#             # Переходимо на веб-сторінку
#             await page.goto('https://map.ukrainealarm.com/')
#
#             # Виконуємо JavaScript для зменшення масштабу сторінки
#             await page.evaluate("document.body.style.zoom='25%'")
#
#             # Затримка для завантаження сторінки
#             await asyncio.sleep(5)  # Почекайте 5 секунд або налаштуйте час за потреби
#
#             # Зберігаємо скріншот
#             screenshot_name = 'screenshot.png'
#             await page.screenshot({'path': screenshot_name})
#
#             # Якщо існує попереднє повідомлення, видаляємо його
#             if last_message_id:
#                 await client.delete_messages(channel_entity, last_message_id)
#
#             # Надсилаємо скріншот на канал і зберігаємо ID цього повідомлення
#             message = await client.send_file(channel_entity, screenshot_name, caption="<b>Мапа повітряних тривог❗️❗️❗️</b>", parse_mode='html')
#             last_message_id = message.id
#
#             # Видаляємо файл скріншоту після відправлення
#             os.remove(screenshot_name)
#
#             # Закриваємо браузер
#             await browser.close()
#
#             # Знімаємо блокування
#             is_processing = False
#
# # Запускаємо клієнт
# with client:
#     client.loop.create_task(main())
#     client.loop.run_forever()




from telethon import TelegramClient, events
import asyncio
import os
from pyppeteer import launch
from PIL import Image, ImageGrab

# Ваші API ID та хеш, отримані від Telegram
api_id = '25362028'
api_hash = 'da9cd1df95149fede816e2b5aa22a813'

# Токен вашого бота Telegram
bot_token = '6330357107:AAG0s_PdVm7bkhFkcDN1u9L2i7bWOd-X54Y'

# ID чату або каналу, куди ви хочете надіслати скріншот
chat_id = '-1001939636184'

# Створюємо клієнт Telegram
client = TelegramClient('anon', api_id, api_hash)

# Змінна для зберігання ID останнього повідомлення
last_message_id = None

# Змінна для блокування
is_processing = False

async def main():
    # Отримуємо entity для каналу
    channel_entity = await client.get_entity('https://t.me/hfehsfsyfhsehf')

    # Підписуємося на повідомлення з каналу
    @client.on(events.NewMessage(chats=channel_entity))
    async def my_event_handler(event):
        global last_message_id
        global is_processing

        # Якщо вже обробляється повідомлення, пропускаємо це
        if is_processing:
            return

        # Якщо повідомлення містить слова "тривога" або "відбій" або "артобстрілу!"
        if 'тривога' in event.raw_text or 'тривоги' in event.raw_text or 'артобстрілу!' in event.raw_text:
            # Встановлюємо блокування
            is_processing = True

            # Запускаємо браузер
            browser = await launch()

            # Відкриваємо нову сторінку
            page = await browser.newPage()

            # Встановлюємо розмір вікна браузера
            await page.setViewport({'width': 1920, 'height': 1080})

            # Переходимо на веб-сторінку
            await page.goto('https://map.ukrainealarm.com/')

            # Виконуємо JavaScript для зменшення масштабу сторінки
            await page.evaluate("document.body.style.zoom='25%'")

            # Затримка для завантаження сторінки
            await asyncio.sleep(1)  # Почекайте 5 секунд або налаштуйте час за потреби

            # Зберігаємо скріншот
            screenshot_name = 'screenshot.png'
            await page.screenshot({'path': screenshot_name})

            # Визначаємо координати області для скріншоту (центральна частина)
            left = int(1502 * 0.14)
            top = int(1049 * 0.03)
            right = int(1502 * 1.139)
            bottom = int(1049 * 1.01)

            # Робимо скріншот карти
            im = Image.open(screenshot_name)
            cropped_im = im.crop((left, top, right, bottom))
            desired_size = (1502, 1049)
            resized_im = cropped_im.resize(desired_size, Image.LANCZOS)
            resized_im.save(screenshot_name)

            # Якщо існує попереднє повідомлення, видаляємо його
            if last_message_id:
                await client.delete_messages(channel_entity, last_message_id)

            # Надсилаємо скріншот на канал і зберігаємо ID цього повідомлення
            message = await client.send_file(channel_entity, screenshot_name, caption="<b>Мапа повітряних тривог❗️❗️❗️</b>", parse_mode='html')
            last_message_id = message.id

            # Видаляємо файл скріншоту після відправлення
            os.remove(screenshot_name)

            # Закриваємо браузер
            await browser.close()

            # Знімаємо блокування
            is_processing = False

# Запускаємо клієнт
with client:
    client.loop.create_task(main())
    client.loop.run_forever()

