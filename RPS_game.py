import random

# Game rules: Rock, Paper, Scissors
def rps_result(player_move, opponent_move):
    if player_move == opponent_move:
        return "Tie"
    elif (player_move == "R" and opponent_move == "S") or \
         (player_move == "S" and opponent_move == "P") or \
         (player_move == "P" and opponent_move == "R"):
        return "Player 1 Wins"
    else:
        return "Player 2 Wins"

# The play function that simulates a number of games
def play(player1, player2, num_games=1000, verbose=False):
    results = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Ties": 0}
    
    for _ in range(num_games):
        move1 = player1("")
        move2 = player2("")
        
        result = rps_result(move1, move2)
        
        if result == "Player 1 Wins":
            results["Player 1 Wins"] += 1
        elif result == "Player 2 Wins":
            results["Player 2 Wins"] += 1
        else:
            results["Ties"] += 1
            
        if verbose:
            print(f"Player 1: {move1}, Player 2: {move2} -> {result}")
    
    return results

# Define basic bots for testing

# Random bot
def random_player(_):
    return random.choice(["R", "P", "S"])

# Quincy bot: Always plays Rock
def quincy(_):
    return "R"

# Kris bot: Alternates between Rock and Paper
def kris(prev_play):
    return "P" if prev_play == "R" else "R"

# Abbey bot: Randomly plays Rock, Paper, or Scissors with a bias
def abbey(prev_play):
    return random.choices(["R", "P", "S"], weights=[0.4, 0.4, 0.2])[0]

# Your player AI (example that plays Rock)
def player(prev_play):
    return "R"

# Now let's run a test between your AI and the different bots
results = play(player, quincy, 1000, verbose=True)
print("\nResults vs Quincy:")
print(results)

results = play(player, kris, 1000, verbose=True)
print("\nResults vs Kris:")
print(results)

results = play(player, abbey, 1000, verbose=True)
print("\nResults vs Abbey:")
print(results)

results = play(player, random_player, 1000, verbose=True)
print("\nResults vs Random Player:")
print(results)
