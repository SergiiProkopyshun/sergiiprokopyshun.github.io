from telethon import TelegramClient, events
import asyncio
from PIL import Image
import pyscreenshot as ImageGrab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Ваші API ID та хеш, отримані від Telegram
api_id = '25362028'
api_hash = 'da9cd1df95149fede816e2b5aa22a813'

# Створюємо клієнт
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

            # Налаштовуємо Headless режим для веб-браузера
            chrome_options = Options()
            chrome_options.add_argument('--headless')

            # Запускаємо веб-браузер у Headless режимі
            driver = webdriver.Chrome(options=chrome_options)

            # Відкриваємо веб-сторінку з мапою
            driver.get('https://alerts.in.ua/')
            await asyncio.sleep(1)  # Чекаємо 30 секунд перед роботою іншого коду

            # Отримуємо розмір екрану
            screen = ImageGrab.grab()
            screen_width, screen_height = screen.size

            # Визначаємо координати області для скріншоту (центральна частина)
            left = int(screen_width * 0.17)
            top = int(screen_height * 0.13)
            right = int(screen_width * 0.84)
            bottom = int(screen_height * 0.94)

            # left = int(screen_width * 0.17)
            # top = int(screen_height * 0.14)
            # right = int(screen_width * 0.84)
            # bottom = int(screen_height * 0.92)

            # Робимо скріншот карти
            im = ImageGrab.grab(bbox=(left, top, right, bottom))
            desired_size = (1300, 870)
            resized_im = im.resize(desired_size, Image.LANCZOS)

            name = "map.png"
            resized_im.save(name)

            # Якщо існує попереднє повідомлення, видаляємо його
            if last_message_id:
                await client.delete_messages(channel_entity, last_message_id)

            # Надсилаємо скріншот на канал і зберігаємо ID цього повідомлення
            message = await client.send_file(channel_entity, name, caption="<b>Мапа повітряних тривог❗️❗️❗️</b>", parse_mode='html')
            last_message_id = message.id

            # Видаляємо файл скріншоту після відправлення
            os.remove(name)

            # Закриваємо веб-браузер
            driver.quit()

            # Знімаємо блокування
            is_processing = False

# Запускаємо клієнт
with client:
    client.loop.create_task(main())
    client.loop.run_forever()
