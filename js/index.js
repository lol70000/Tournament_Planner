document.getElementById("submit").onclick = main;

async function main() {
    teams = {};
    games = {};

    // Get all the vairables from the form

    num_teams = document.getElementById("number_of_teams").value;
    num_gyms = document.getElementById("number_of_gyms").value;
    game_time = document.getElementById("time_per_game").value;
    break_time = document.getElementById("time_per_break").value;
    start_time = document.getElementById("start_time").value;

    // fill the teams table with elemenets for all the teams

    for (i = 1; i <= num_teams; i++) {
        teams[i] = {num_follow: 0};
    }
    
    
};