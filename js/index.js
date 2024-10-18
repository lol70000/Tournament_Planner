class team {
    constructor(teamname){
        this.name = String(teamname);
        this.game_times = [];
    }

    return_name(){
        return String(this.name);
    }
}

class games {
    constructor(team1, team2){
        this.dict = {};
        str1_team = team1.return_name;
        str2_team = team2.return_name;
        game_string = str1_team + str2_team
        this.dict.game = String(game_string)
        this.dict.team1 = str1_team
        this.dict.team2 = str2_team
    }
}

