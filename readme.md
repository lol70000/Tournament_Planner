# Tournament Plan Generator

## class structure

- Team
    - Name (f.E. Team 1/ Team A)
    - Gametimes (a list of all games to add teh fonctionality of being able to limit how many games in a row one team has)

- Games
    - dict of combination of games with teams as values f. E.({"Team1 : Tema2" :["Team1","team2"] })

- Gametimes
    - time_identifier (f.E. 1/2)
    - list of len(number_of_places)
    - function wich can get random games from games class and check if team not already given for that time wich also checks with the team class to give the team class the game time ans how many games in a row there already are.

- Table
    - a dict which combines all the gametimes in to one table ans ads the time as the key and then the gametimes as a dict within the dict.1