

import requests


def get_tracker_data(userID, platform):
    """
    User inputs userID and platform and function returns a dictionary of custom data from API JSON file
    :param userID: Username on either steam, xbox or playstation
    :param platform: platform, either "xbl", "psn" or "steam"
    :return:
    """
    custom_dictionary = {}
    url = f"https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{userID}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/86.0.4240.198 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    info = resp.json()
    platform_dic = {"xbl": "Xbox Live",
                    "psn": "Playstation Network", "steam": "Steam"}
    custom_dictionary["platform"] = platform_dic[
        info["data"]["platformInfo"]["platformSlug"]
    ]
    custom_dictionary["username"] = info["data"]["platformInfo"]["platformUserHandle"]
    custom_dictionary["season_name"] = info["data"]["metadata"]["currentSeason"]
    custom_dictionary["lifetime_wins"] = info["data"]["segments"][0]["stats"]["wins"][
        "displayValue"
    ]
    custom_dictionary["lifetime_win_rank"] = info["data"]["segments"][0]["stats"][
        "wins"
    ]["rank"]
    custom_dictionary["goal_shot_ratio"] = info["data"]["segments"][0]["stats"][
        "goalShotRatio"
    ]["displayValue"]
    custom_dictionary["season_reward"] = info["data"]["segments"][0]["stats"][
        "seasonRewardLevel"
    ]["metadata"]["rankName"]
    custom_dictionary["game_data"] = get_matches(info)
    print(custom_dictionary)
    return custom_dictionary


def get_matches(data):
    """
    From JSON Rocket League tracker data, returns the gametype and number of matches played this season
    :param data: pass to it RL tracker JSON as text `data`
    :return: returns a dictionary with gametype and number of games played
    """
    match_dic = {}
    for i in range(2, 10):
        match = data["data"]["segments"][i]["stats"]["matchesPlayed"]["value"]
        name = data["data"]["segments"][i]["metadata"]["name"]
        match_dic[name] = match
    return match_dic


def tracker_data_print(dictionary):
    """A simple function for printing results of custom dictionary passed to it"""
    print(
        f"These are the Rocket League user stats for {dictionary['username']}, playing on {dictionary['platform']}\n"
        f"We are currently playing in Season {dictionary['season_name']}, "
        f"and you will be recieving {dictionary['season_reward']} season rewards\n"
        f"Lifetime stats\n"
        f"Lifetime wins: {dictionary['lifetime_wins']}\n"
        f"Lifetime win rank: {dictionary['lifetime_win_rank']}\n"
        f"Lifetime goal to shot ratio: {dictionary['goal_shot_ratio']}%"
    )


my_tracker_info = get_tracker_data("UKF%20WONDERBOY", "xbl")
tracker_data_print(my_tracker_info)
