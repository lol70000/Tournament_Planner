document.getElementById("submit").onclick = main;

async function main() {
    games = {};

    // Get all the vairables from the form

    num_teams = document.getElementById("number_of_teams").value;
    num_gyms = document.getElementById("number_of_gyms").value;
    game_time = document.getElementById("time_per_game").value;
    break_time = document.getElementById("time_per_break").value;
    start_time = document.getElementById("start_time").value;

    // fill the teams table with elemenets for all the teams

    teams = await make_teams_dict(num_teams);
    combinations = await make_all_combinations(teams);

    await getRandomElement(combinations);
};

async function getRandomElement(combinations) {
    const random_index = Math.floor(Math.random() * combinations.length);
    console.log(random_index);
};

async function make_all_combinations(teams) {
    teams_numbers = [];
    comb = [];

    for (let [key, value] of Object.entries(teams)){
        teams_numbers.push(key);
    };

    for (let i = 0; i < teams_numbers.length; i++) {
        for (let j = i + 1; j < teams_numbers.length; j++) {
            comb.push([teams_numbers[i], teams_numbers[j]]);
        };
    };

    return comb;
};

async function make_teams_dict(number_teams){
    teams = {};
    for (i = 1; i <= number_teams; i++) {
        teams[i] = {num_follow: 0};
    };
    return teams;
};