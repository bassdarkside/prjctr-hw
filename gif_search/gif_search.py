import requests
from decouple import config
from colorama import Fore


def gif_request(keyword):
    KEY = config("KEY")
    B = Fore.BLUE
    Y = Fore.YELLOW
    params = {"q": keyword, "api_key": KEY, "limit": 5, "rating": "r"}
    url = "http://api.giphy.com/v1/gifs/search/"
    response = requests.get(url, params=params).json()
    results = ""
    for gif in response["data"]:
        results += f"{G}{gif['bitly_url']} <-- {B}{gif['title']}{Y}\n"
    return results


G = Fore.GREEN
user_input = input(f"{G}Enter keyword for GIF search: {Fore.RESET}")
list_results = gif_request(user_input)
print(f"Search results:\n{list_results}")
