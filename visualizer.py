import json
import os

import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def get_player_id(url) -> str:
    """
    Gets the Steam64 ID of a player from their profile url
    :param url: a string representation of a Steam user's profile page
    :return: a string representation of their Steam64 ID
    """
    id_text = url.strip("/").split("/")[-1]
    id_page = requests.get(f"https://steamid.io/lookup/{id_text}").text
    soup = BeautifulSoup(id_page, "html.parser")
    try:
        id_dd = soup.find_all("dd")[2]
    except IndexError:
        return ""
    else:
        id = id_dd.find("a").get_text()
        return id

def get_player_name(key, sid) -> str:
    """
    Gets a Steam user's name given their ID number
    :param key: API key for using the Steam Web API
    :param sid: the Steam64 ID of the user to get name of
    :return: a string representation of a Steam username
    """
    player_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={sid}"
    player_name = json.loads(requests.get(player_url).text)["response"]["players"][0]["personaname"]
    return player_name

def get_owned_games(key, sid) -> list:
    """
    Gets a user's Steam games and puts their info in JSON into a list 
    :param key: the API key in order to get the game data
    :param sid: the Steam ID number of the user 
    :return: a list of all the user's Steam games and their info in JSON 
    """
    games_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={sid}&include_appinfo=1&include_played_free_games=1&format=json"
    games_response = json.loads(requests.get(url=games_url).text)["response"]["games"]
    return games_response

def get_playtimes(games) -> dict:
    """
    Gets the playtimes of each of the games in the provided list
    :param games: a list of games owned by the Steam user
    :return: a dictionary of game titles with their corresponding playtimes from the Steam user
    """
    playtimes = {}
    other_times_sum = 0
    for game in games:
        if game["playtime_forever"] != 0:
            playtimes.update({game["name"]: game["playtime_forever"]}) 
    if len(playtimes) > 9:
        while len(playtimes) > 9:
            min_game = get_min_game(playtimes)
            other_times_sum += min_game[1]
            playtimes.pop(min_game[0])
        playtimes.update({"Other": other_times_sum})
    return playtimes

def get_min_game(playtimes) -> tuple:
    """
    Gets the game with the minimum playtime from a dictionary of games and their corresponding playtimes
    :param playtimes: dictionary of games and their corresponding playtimes
    :return: a tuple of the game name with its playtime representing the game with the minimum playtime
    """
    min_name = list(playtimes.keys())[0]
    min_time = list(playtimes.values())[0]
    for (name, time) in playtimes.items():
        if time < min_time:
            min_name = name
            min_time = time
    return min_name, min_time

def plot_playtimes(playtimes, name) -> None:
    """
    Plots the playtimes of all of a user's games in a pie chart (9 of most played, the rest in "Other")
    :param playtimes: dictionary of the top 9 and other games with their corresponding playtimes
    :param name: the name of the Steam user
    """
    if playtimes: # Check if playtimes are hidden or not
        game_titles = list(playtimes.keys())
        game_times = list(playtimes.values())
        plt.figure(figsize=(10, 6))
        y = np.array(game_times)
        plt.pie(y, autopct="%1.1f%%", pctdistance=1.15)
        plt.title(f"{name}'s Most Played Games")
        plt.legend(game_titles, loc="lower right", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
    else:
        print(f"{name} has no playtimes recorded.")

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("API_KEY")
    profile_url = input("Enter a Steam Profile URL: ")
    try:
        player_id = get_player_id(profile_url)
        player_name = get_player_name(api_key, player_id)
        player_games = get_owned_games(api_key, player_id)
    except IndexError:
        print(f"This user cannot be found.")
    except KeyError:
        print(f"{player_name}'s games are hidden.")
    else:
        playtimes = get_playtimes(player_games)
        plot_playtimes(playtimes, player_name)