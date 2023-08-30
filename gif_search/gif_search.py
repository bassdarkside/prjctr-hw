import requests
from decouple import config
from colorama import Fore


KEY = config("KEY")

B = Fore.BLUE
G = Fore.GREEN
Y = Fore.YELLOW


def gif_request(keyword):
    end_point = "http://api.giphy.com/v1/gifs/search"
    url = f"{end_point}?q={keyword}&api_key={KEY}&limit=5&offset=0&rating=r"
    response = requests.get(url)
    return response.json()


def build_output(*args):
    response = gif_request(*args)
    res = ""
    for gif in response["data"]:
        res += f"{G}{gif['bitly_url']} <-- {B}{gif['title']}{Y}\n"
    return res


user_input = input(f"{G}Enter keyword for GIF search: {Fore.RESET}")
list_results = build_output(user_input)
print(f"Search results:\n{list_results}")
