import requests
import telebot
from telebot import types, apihelper, logging
from decouple import config


BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


def gif_request(keyword):
    GIPHY_KEY = config("GIPHY_KEY")
    params = {"q": keyword, "api_key": GIPHY_KEY, "limit": 1, "rating": "r"}
    url = "http://api.giphy.com/v1/gifs/search/"
    response = requests.get(url, params=params).json()
    results = ""
    for gif in response["data"]:
        results += f"{gif['bitly_url']}\n"
    return results


@bot.message_handler(commands=["start", "main", "hello"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔦 Start search!")
    markup.add(btn1)
    bot.send_message(
        message.chat.id,
        f"👋 Hi, {message.from_user.first_name}! Let's get search!",
        reply_markup=markup,
    )


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "🔦 Start search!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.from_user.id,
            "🔍 Enter keyword for search GIF images:",
            reply_markup=markup,
        )
    elif message.text:
        list_results = gif_request(message.text.lower())
        bot.send_message(message.from_user.id, "Here's what I found for you 👉")
        bot.send_message(
            message.from_user.id, f"{list_results}", parse_mode="Markdown"
        )


try:
    apihelper.SESSION_TIME_TO_LIVE = 5 * 60
    apihelper.RETRY_ON_ERROR = True
    bot.infinity_polling()
except telebot.apihelper.ApiTelegramException as e:
    logging.log(e)
