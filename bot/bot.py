import io
import telebot

from src.tools import get_frame_from_server, convert_frame_to_image


# Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token
API_TOKEN = '7164360283:AAFck78_pv9JbPszHy7Ccl_GoZoXVWgKTQs'
ENDPOINT = "http://backend:8000/image"

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your simple bot. How can I help you today?")


@bot.message_handler(commands=['send_image'])
def send_image(message):
    frame = get_frame_from_server(ENDPOINT)
    image = convert_frame_to_image(frame["frame"])
    
    # Save the image to a bytes object
    with io.BytesIO() as image_bytes:
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)
        bot.send_photo(message.chat.id, image_bytes)


# Start polling
bot.polling()
