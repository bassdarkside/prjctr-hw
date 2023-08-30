import requests
import telebot
from telebot import types
from decouple import config


GIPHY_KEY = config("GIPHY_KEY")
BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


def gif_request(keyword):
    end_point = "http://api.giphy.com/v1/gifs/search"
    url = f"{end_point}?q={keyword}&api_key={GIPHY_KEY}&limit=1&offset=0&rating=r"
    response = requests.get(url)
    return response.json()


def build_output(*args):
    response = gif_request(*args)
    res = ""
    for gif in response["data"]:
        res += f"{gif['bitly_url']}\n"
    return res


@bot.message_handler(commands=["start", "main", "hello"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔦 Start search!")
    markup.add(btn1)
    bot.send_message(
        message.chat.id,
        f"👋 Hi, {message.from_user.first_name}! I'm GiflerBot!",
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
        list_results = build_output(message.text.lower())
        bot.send_message(
            message.from_user.id, f"{list_results}", parse_mode="Markdown"
        )


bot.polling(none_stop=True, interval=0)
