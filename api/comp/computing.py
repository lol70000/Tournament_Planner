import random

def make_table(teams: int, gyms: int, starttime: str, time_per_game: int, time_per_break: int):
    team_dict = make_teams(teams)
    games_list = games_dict(teams)
    # print(games_list)
    # number_of_games = len(games_list)
    gym_dict = make_gym_dict(gyms)

    # print(number_of_games)
    fill_gyms_table(games_list, gym_dict, team_dict)
    # for i in gym_dict:
    #     print(gym_dict[i])
    # print(team_dict)
    return gym_dict

def fill_gyms_table(games_list: list, gyms_dict: dict, teams_dict: dict):
    counter = 0
    while len(games_list) != 0:
        for i in gyms_dict:
            index = int(i)
            iteration_index = 0
            random_index = random.randint(0,len(games_list)-1)
            selected_game = games_list[random_index]
            while check_already_if_in_gyms(selected_game, gyms_dict, counter):
                random_index = random.randint(0,len(games_list)-1)
                selected_game = games_list[random_index]
                iteration_index+=1
                if iteration_index == len(games_list)*3:
                    break
            else:
                games_list.pop(random_index)
                gyms_dict[i].append(selected_game)
                for y in selected_game:
                    teams_dict[y]["gametimes"].append(index)
                    teams_dict[y]["number_of_follow_up_games"] += 1
            if len(games_list) == 0:
                break
        counter += 1


def check_already_if_in_gyms(selected_game: list, gyms_dict: dict, counter: int) -> bool:
    check = 0
    for i in gyms_dict:
        if len(gyms_dict[i]) <= counter:
            continue
        for selected_team in selected_game:
            if selected_team in gyms_dict[i][counter]:
                check+=1
    if check > 0:
        return True
    else:
        return False

def select_random_game(games: list,) -> list:
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