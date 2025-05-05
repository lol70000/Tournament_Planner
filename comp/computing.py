import random

def make_table(teams: int, gyms: int, starttime: str, time_per_game: int, time_per_break: int):
    team_dict = make_teams(teams)
    games_list = games_dict(teams)
    number_of_games = len(games_list)
    gym_dict = make_gym_dict(gyms)

    print(team_dict)
    print("\n")
    print(games_list)
    print("\n")
    print(gym_dict)
    print("\n")
    fill_gyms_table(games_list, gym_dict, team_dict)
    print(gym_dict)
    print(team_dict)

def fill_gyms_table(games_list: list, gyms_dict: dict, teams_dict: dict):
    for i in gyms_dict:
        index = int(i)
        selected_game: list = select_random_game(games_list)
        status: bool = check_already_if_in_gyms(selected_game, gyms_dict)
        if not status:
            gyms_dict[i].append(selected_game)
            for y in selected_game:
                teams_dict[y]["gametimes"].append(index)
                teams_dict[y]["number_of_follow_up_games"] += 1


def check_already_if_in_gyms(selected_game: list, gyms_dict: dict) -> bool:
    for i in gyms_dict:
        if selected_game in gyms_dict[i]:
            return True
    return False

def select_random_game(games: list) -> list:
    return games.pop(random.randint(0,len(games)-1))

def make_gym_dict(gyms: int) -> dict:
    dict = {}
    for i in range(gyms):
        dict[i] = []
    return dict

def games_dict(teams: int) -> list:
    list = []
    for i in range(teams):
        for j in range(i+1,teams):
            list.append([i,j])
    return list

def make_teams(teams: int) -> dict:
    dict = {}
    for team in range(teams):
        dict[team]= {"name":f"Team {team+1}",
                    "gametimes":[],
                    "number_of_follow_up_games":0}
    return dict