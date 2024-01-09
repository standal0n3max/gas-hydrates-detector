import os
import telebot
import shutil
import time


# Your Bot Token and Chat ID
bot_token = '6914021079:AAEbz2uFILt78cQ_v1_bZZEdUT45Z_PLuA8'
chat_id = '1247024625'

# Create a bot object
bot = telebot.TeleBot(token=bot_token)

temp_dir = 'Processing/temp'

# Check if the directory already exists
if not os.path.exists("Processing/saved"):
    # Create the directory
    os.makedirs("Processing/saved")

while True:
    # Count the number of files in the temp directory
    files = [filename for filename in os.listdir(temp_dir) if filename.endswith('.mp4')]
    num_files = len(files)

    # Check if there are 3 or more videos in the directory
    if num_files >= 3:
        # Send a message to the Telegram bot
        bot.send_message(chat_id=chat_id, text='Hydrate nucleation occurred')

        # Move all videos to Processing/saved
        for filename in files:
            shutil.move(os.path.join(temp_dir, filename), 'Processing/saved')

        pass

    time.sleep(30)