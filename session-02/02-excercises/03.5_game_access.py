# Tilgang til et spill

has_username = True
accepted_rules = True
is_blocked = False

if has_username and accepted_rules and not is_blocked:
    print("You are authorized! Access will commence")
else:
    print("You do not qualify to access the game")