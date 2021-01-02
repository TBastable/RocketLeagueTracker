import requests
import json


def get_tracker_data(userID, platform):
    """
    User inputs userID and platform and function returns a dictionary of custom data from API JSON file
    :param userID: Username on either steam, xbox or playstation
    :param platform: platform, either "xbl", "psn" or "steam"
    :return:
    """
    custom_dictionary = {}
    URL = f'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{userID}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    resp = requests.get(URL, headers=headers)
    info = json.loads(resp.text)
    platform_dic = {'xbl': 'Xbox Live', 'psn': 'Playstation Network', 'steam': 'Steam'}
    custom_dictionary['platform'] =platform_dic[info['data']['platformInfo']['platformSlug']]
    custom_dictionary['username'] = info['data']['platformInfo']['platformUserHandle']
    custom_dictionary['season_name'] = info['data']['metadata']['currentSeason']
    custom_dictionary['lifetime_wins'] = info['data']['segments'][0]['stats']['wins']['displayValue']
    custom_dictionary['lifetime_win_rank'] = info['data']['segments'][0]['stats']['wins']['rank']
    custom_dictionary['goal_shot_ratio'] = info['data']['segments'][0]['stats']['goalShotRatio']['displayValue']
    custom_dictionary['season_reward'] = info['data']['segments'][0]['stats']['seasonRewardLevel']['metadata']['rankName']
    print(custom_dictionary)
    return custom_dictionary



def get_matches(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in get_matches(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in get_matches(key, d):
                        yield result


def tracker_data_print(dictionary):
    print(f"These are the Rocket League user stats for {dictionary['username']}, playing on {dictionary['platform']}\n"
          f"We are currently playing in Season {dictionary['season_name']}, and you will be recieving {dictionary['season_reward']} season rewards\n"
          f"Lifetime stats\n"
          f"Lifetime wins: {dictionary['lifetime_wins']}\n"
          f"Lifetime win rank: {dictionary['lifetime_win_rank']}\n"
          f"Lifetime goal to shot ratio: {dictionary['goal_shot_ratio']}%")

my_tracker_info = get_tracker_data('WoolStarfish663', 'xbl')
tracker_data_print(my_tracker_info)

