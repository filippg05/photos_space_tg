import telegram
import os
import random
import time
import argparse


def publish_photos(bot_token, chat_id, images_dir, interval):
    bot = telegram.Bot(token=bot_token)
    image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
    random.shuffle(image_files)
    while True:
        for image_file in image_files:
            photo_path = os.path.join(images_dir, image_file)
            try:
                with open(photo_path, 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                    print(f"Отправлено изображение: {image_file}")
            except Exception as e:
                print(f"Ошибка: {e}")
        print(f"Ожидание {interval} секунд...")
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Публикация фотографий в Telegram-канал")
    parser.add_argument("bot_token", type=str, help="Токен Telegram-бота")
    parser.add_argument("chat_id", type=int, help="ID Telegram-канала")
    parser.add_argument("images_dir", type=str, help="Путь к директории с фотографиями")
    parser.add_argument("interval", type=int, help="Интервал в секундах между публикациями", default=14400) 

    args = parser.parse_args()

    publish_photos(args.bot_token, args.chat_id, args.images_dir, args.interval)