# Kampresultat

def show_match_result(home_team: str, home_score: int, away_team: str, away_score: int):
    if home_score > away_score:
        print(f"The winner is the home team {home_team}")
    elif away_score > home_score:
        print(f"Away team {away_team} takes the victory")
    else:
        print("The game ends with a tie")

show_match_result("Brann", 3, "Start", 2)
show_match_result("RBK", 1, "Molde", 2)
show_match_result("Hardy", 3, "Djerv", 3)
