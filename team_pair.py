def team_pairs():
    teams = ['Dragons', 'Pandas', 'Wolves', 'Unicorn']
    null = 0
    for home_team in teams:
        for away_team in teams:
            if home_team == away_team: 
                null += 1
            else:
                print("Home team: " + home_team + " vs " + "Away team: " + away_team)
                print()

team_pairs()