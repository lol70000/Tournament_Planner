document.getElementById("submit").onclick = main;

class team {
    constructor(teamname){
        this.name = String(teamname);
        this.game_times = [];
    };

    return_name(){
        return String(this.name);
    };
};

class games {
    constructor(team1, team2){
        this.dict = {};
        str1_team = team1.return_name;
        str2_team = team2.return_name;
        game_string = str1_team + str2_team;
        this.dict.game = String(game_string);
        this.dict.team1 = str1_team;
        this.dict.team2 = str2_team;
    };
};

class game_times {
    constructor(time_id, num_places){
        this.time_identifier = time_id;
        this.places = [];
    };
};

class table {
    constructor(num_game_times) {
        this.tale_dict = {};
    };
};

function main(){
    num_of_games = document.getElementById("number_of_teams").value;
    num_of_gyms = document.getElementById("number_of_gyms").value;
    start_times = document.getElementById("start_time").value;
    time_per_game = document.getElementById("time_per_game").value;
    time_per_break = document.getElementById("time_per_break").value;
    for(i = 0; i < num_of_games; i++){
        
    }
}